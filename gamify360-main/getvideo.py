import requests
import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import tempfile

API_KEY = 'FT5wLemOnkgMcOU2cdSLxmUP30oX2b9l9Tb7ZkpEWigWvf3FtGmW6VXX'
SEARCH_TERM = 'dance'

# Define the path for the downloaded video
downloaded_video_path = '/content/sample_data/downloaded_video.mp4'

def download_first_video(search_term, api_key, filename):
    url = f'https://api.pexels.com/videos/search?query={search_term}&per_page=1'  # Pexels API endpoint
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers).json()
    
    video_url = response['videos'][0]['video_files'][0]['link']

    video_response = requests.get(video_url)
    if video_response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(video_response.content)
        print('Video downloaded successfully.')
    else:
        print('Failed to download video.')

# Download the video and provide the path
download_first_video(SEARCH_TERM, API_KEY, downloaded_video_path)

# Continue with the rest of your script...
