import streamlit as st

# Title of the app
st.title("Summerizer")

# User input
question = st.text_input("Enter:")

# Convert the question to lowercase for consistency
question = question.lower()

# Responses based on the question
if question in ['hi','hola','hey']:
    st.write("Hello")
elif question in ['how to use', 'i cant use','guide']:
    st.write("step1: Go to the YouTube video you want to summarize.")
    st.write("step2: Ensure the video you want to summarize is in English only!")
    st.write("step3: Copy the link of the YouTube video.")
    st.write("Log on to YouTube summarizer, paste the link, and press 'Get Details'.")
    st.write("There you go, you will get detailed notes of that video.")
elif question in ['i cant translate', 'i am getting an error', 'error']:
    st.write("Sorry for that. I can't summarize other languages. We are working on that. Ensure the subtitles are on and the video is in English!")
elif question in ['what is your name?', 'who are you?','your name?']:
    st.write("My name is Sammy.")
    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Nice name and nice meeting you, {name}.")
elif question in ['quit']:
    st.write("Goodbye!")
else:
    st.write("I don't understand what you said.")

# Add a button to reset the input field
if st.button('Clear'):
     st.query_params # This will reset the input field

# Footer
st.markdown("---")
st.markdown("### In Life, Time Is Short for Long Videos!!!!.......")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
        background-size: cover;
    }
    .title {
        font-family: 'Courier New', Courier, monospace;
        color: #4B0082;
        text-align: center;
    }
    .subtitle {
        font-family: 'Courier New', Courier, monospace;
        color: #4B0082;
    }
    </style>
    """,
    unsafe_allow_html=True
)
