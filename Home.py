import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import cv2
import gtts
from playsound import playsound

hide_streamlit_style = """
            <style>
            MainMenu {
            visibility: show;
            }
            footer {
            visibility: show;
            }
            .subheader {
            font-size: 20px;  /* Adjust the font size as needed */
            font-weight: none;
            color: #A3A3A3;  /* Adjust the text color as needed */
            margin-top: 0px;
            margin-bottom: 5px;
    }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.title("\t SIGN CONNECT ")
st.sidebar.markdown("<p class='subheader' style = 'font-size : 14px; '> Connecting through Signs.   </p> <br \>", unsafe_allow_html=True)
st.title(' SIGN CONNECT \n ')
st.markdown("<p class='subheader'> Connecting through Signs.   </p> <br \>", unsafe_allow_html=True)

def main():


    st.subheader("Start Communicating! \n")
    res = ""
    # Display a file uploader that accepts multiple files
    uploaded_files = st.file_uploader("Upload one or multiple files", accept_multiple_files=True)
    li = ['']
    # Process the uploaded files
    if uploaded_files:
        st.write("\n\n Uploaded files :")
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            imga = np.array(img)
            image = cv2.cvtColor(imga, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, (50, 50))
            result = predict_class(image)
            res = res+str(result)
            li.append(str(result))
            st.image(uploaded_file, caption=result, use_column_width=False)

        t1 = gtts.gTTS(res,lang='en', tld = 'co.in')
        t1.save("Pred(2).mp3")


    st.write("\n\n\n\n\n\n")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('\n\n  Prediction : ')
        st.title("--- " + res + " ---")
    with col2:
        st.title("")
        st.subheader("")
        st.subheader("")
        if st.button("Play Predicted Word"):
            playsound("Pred(2).mp3")



def predict_class(image):
    with st.spinner('Loading Model...'):
        classifier_model = keras.models.load_model(r'final_model_img.h5', compile=False)
    shape = ((50, 50, 1))
    model = keras.Sequential([hub.KerasLayer(classifier_model, input_shape=shape)])


    test_image = image
    test_image = keras.preprocessing.image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    class_name = ['', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
    prediction = model.predict(test_image)
    final_pred = class_name[np.argmax(prediction)]
    return final_pred


footer = """
        <style>
        a:link , a:visited{
        color: white;
        background-color: transparent;
        text-decoration: None;
        }

        a:hover,  a:active {
        color: green;
        background-color: transparent;
        text-decoration: None;
        }

        footer {
	    visibility: hidden;
	    }
	    
        footer:after {
	    content:"Made by Sneha using Streamlit 🍁"; 
	    visibility: visible;
	    display: block;
	    position: relative;
	    #background-color: red;
	    padding: 5px;
	    top: 2px;
        }
        </style>
"""

st.markdown(footer, unsafe_allow_html = True)
if __name__ == '__main__' :
    main()