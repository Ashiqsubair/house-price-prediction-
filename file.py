
import streamlit as st
import seaborn as sns
import pickle
import base64

#Creating Background

main_bg = "backgroundnew.jpg"
main_bg_ext = "jpg"

side_bg = "backgroundnew.jpg"
side_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)


#calling model

pickle_in = open('linear_project.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:


st.title('Delhi House Price Prediction')

Name = st.text_input("Name:")

area=st.number_input("Area in Sq.ft:")

bhk = st.selectbox('No: BHK[Bedroom,Hall,Kitchen:',('1', '2', '3','4','5','6','7'))

bathroom=st.selectbox('Bathroom:',('1', '2', '3','4','5','6','7'))

furnishing=st.selectbox('0-Furnished,1-Semi Furnished,2-Unfurnished:',('0','1','2'))

parking=st.selectbox("No: of vehicles can be parked:",('1', '2', '3','4','5','6','7'))

status=st.selectbox('0-Almost Ready,1-Ready to move',('0','1'))

transaction=st.selectbox('0-New property,1-Resale',('0','1'))

type=st.selectbox('0-Apartment,1-Builder floor',('0','1'))

Phone=st.text_input("Mobile Number:")

topredict=[area,bhk,bathroom,furnishing,parking,status,
transaction,type]
submit = st.button('Predict')
if submit:
    if area<250 :
        st.error("Area Should not be less than 250!")
    elif Name=="" or Name=="null":
        st.error("Name Should not be Blank")
    elif len(Phone)<10:
        st.error("Enter a valid Phone Number")
    else:
        prediction = classifier.predict([topredict])
        st.write('Estimated Price of Your House is ',prediction)
        st.balloons()
#Creating Sidebar


st.sidebar.image(image='ICFOSS_logo.png',width=200)

st.sidebar.subheader('Dataset Used')
st.sidebar.write("Kaggle [link](https://www.kaggle.com/neelkamal692/delhi-house-price-prediction)")
st.sidebar.select_slider(label='Feedback',options=['poor','average','good','excellent'])

if st.sidebar.button(label="Submit"):
    st.sidebar.success("Thank you for your Feedback")
    st.sidebar.balloons()
st.sidebar.subheader('About')
st.sidebar.write('Project Of Machine Learning with ICFOSS')
