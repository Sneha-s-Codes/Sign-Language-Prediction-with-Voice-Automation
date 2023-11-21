import streamlit as st
import speech_recognition as sr

st.markdown(
    """
    <style>
    .subheader {
        font-size: 20px;  /* Adjust the font size as needed */
        font-weight: none;
        color: #D6DBDF;  /* Adjust the text color as needed */
        margin-top: 0px;
        margin-bottom: 10px;
}
    </style>
    """
    , unsafe_allow_html=True
)

st.sidebar.title("\t SIGN CONNECT ")
st.sidebar.markdown("<p class='subheader' style = 'font-size : 14px; '> Connecting through Signs.   </p> <br \>", unsafe_allow_html=True)

# Set up the SpeechRecognition recognizer
r = sr.Recognizer()


st.title("Voice to Text ")
st.markdown("<p class='subheader'> Ask the other person to speak!   </p> <br \>", unsafe_allow_html=True)

# Create a Streamlit button to start the voice input
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Speak now...")
        if st.button("Stop Recording"):
            try:
                r.__exit__()
            except TypeError:
                print("")

        audio = r.listen(source)

        st.write("Recording complete. Converting to text...")

        # Use Google Web Speech API to convert audio to text
        try:
            text = r.recognize_google(audio)
            st.subheader('\n\n  They said :  ')
            st.title("--- " + text + " ---")
        except sr.UnknownValueError:
            st.write("Google Web Speech API could not understand the audio.")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Web Speech API; {e}")


#Stop Button



