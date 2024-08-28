# youtube_summerizer_powered_by_giminipro
A Streamlit-based app that extracts and summarizes YouTube video transcripts in English using Google Gemini Pro, providing concise and detailed summaries. It offers a quick and efficient way to grasp video content in just a few clicks.
This project is a Streamlit-based web application designed to extract and summarize YouTube video transcripts in English. By utilizing Google Gemini Pro, the app generates concise and detailed summaries, helping users quickly understand the content of YouTube videos. Simply input a YouTube video link, and the app will fetch the transcript, process it, and deliver a clear summary, all within an easy-to-use interface. The project supports only English-language content.

Features:
YouTube Transcript Extraction: Automatically fetches transcripts from YouTube videos.
English-Only Summarization: Generates detailed summaries for English transcripts using Google Gemini Pro.
User-Friendly Interface: Simple and intuitive design built with Streamlit.
Requirements:
Python 3.8 or higher
Streamlit
Google Gemini Pro API key
Additional Python libraries: dotenv, google-generativeai, youtube-transcript-api
Installation:
Clone the repository.
Install the required libraries using pip install -r requirements.txt.
Set up your Google Gemini Pro API key in a .env file.
Run the app with streamlit run app.py.
Usage:
Enter the YouTube video link in the input field.
Click "Get Detailed Notes" to generate the summary.
View the summary and video thumbnail directly in the app.
