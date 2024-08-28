import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure Google Gemini Pro API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Define the prompt for summarization
prompt = """You are YouTube video summarizer. You will take the youtube transcript and display summary in 3 points 100 words"""

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        raise e
# Function to generate summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


# Header with YouTube logo
st.markdown(
    """
    <style>
    .header {
        display: flex;
        align-items: center;
        text-align:center;
        justify-content: center;
        font-family: 'Courier New', Courier, monospace;
        color: #4B0082;
    }
    .header img {
        height: 40px;
        margin-right: 10px;
    }
    .header h1 {
        font-size: 2rem;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube Logo"/>
        <h1>YouTube Video Summarizer</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("Convert YouTube video transcripts into detailed, concise notes.")

# Input field for YouTube link
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display video thumbnail if link is provided
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to generate detailed notes
if st.button("Get Detailed Notes"):
    with st.spinner("Extracting transcript and generating summary..."):
        try:
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                summary = generate_gemini_content(transcript_text, prompt)
                st.markdown("## Detailed Notes:")
                st.write(summary)
        except Exception as e:
            st.error(f"An error occurred: {e}")

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
        font-family: 'Times New Roman', Courier, monospace;
        font-size: 100px;
        color: #4B0082;
        text-align: center;
    }
    .subtitle {
        font-family: 'Times New Roman', Courier, monospace;
        font-size: 100px;
        color: #4B0082;
    }
    </style>
    """,
    unsafe_allow_html=True
)

