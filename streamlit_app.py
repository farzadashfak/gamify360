import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import tempfile
import requests

# Pexels API for video download
API_KEY = 'JNq2AWIyrTyFr1O5uh9fuhQ36vD0bD1yQkjIK4ZGgI4M0hYT1pr3fPB9'
SEARCH_TERM = 'yoga'

# Function to download the first video from Pexels
def download_first_video(search_term, api_key):
    url = f'https://api.pexels.com/videos/search?query={search_term}&per_page=1'
    headers = {'Authorization': api_key}
    response = requests.get(url, headers=headers)
    
    # Check for HTTP errors
    if response.status_code != 200:
        print(f'Failed to fetch videos. HTTP Error Code: {response.status_code}')
        return None

    # Parse JSON response
    data = response.json()

    # Debugging: print the data to see what's received
    print(data)

    # Check if 'videos' key is in the response
    if 'videos' not in data:
        print('No videos found in the response.')
        return None

    video_url = data['videos'][0]['video_files'][0]['link']
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    video_response = requests.get(video_url, stream=True)

    if video_response.status_code == 200:
        for chunk in video_response.iter_content(chunk_size=1024):
            temp_file.write(chunk)
        print('Video downloaded successfully.')
        return temp_file.name
    else:
        print('Failed to download video.')
        return None

# Streamlit layout
st.title("Gamify360")

# Initialize MediaPipe pose detection
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=False)

# Download benchmark video
downloaded_video_path = download_first_video(SEARCH_TERM, API_KEY)

# Use OpenCV to capture video from the webcam
cap_user = cv2.VideoCapture(0)  # 0 corresponds to the default webcam

if 'playing' not in st.session_state:
    st.session_state.playing = False

start_button, clear_button = st.columns(2)
if not st.session_state.playing:
    if start_button.button('Start'):
        st.session_state.playing = True
else:
    if clear_button.button('Clear'):
        st.session_state.playing = False

def cosine_distance(landmarks1, landmarks2):
    if landmarks1 and landmarks2:
        points1 = np.array([(lm.x, lm.y, lm.z) for lm in landmarks1.landmark])
        points2 = np.array([(lm.x, lm.y, lm.z) for lm in landmarks2.landmark])
        dot_product = np.dot(points1.flatten(), points2.flatten())
        norm_product = np.linalg.norm(points1.flatten()) * np.linalg.norm(points2.flatten())
        similarity = dot_product / norm_product
        return 1 - similarity
    else:
        return 1

if st.session_state.playing and downloaded_video_path:
    cap_benchmark = cv2.VideoCapture(downloaded_video_path)
    
    if not cap_benchmark.isOpened():
        st.error("Failed to open video stream. Please check the video file.")
        st.session_state.playing = False
    else:
        col1, col2, col3 = st.columns([2, 1, 1])  # Adjust the column ratios as needed
        benchmark_video_placeholder = col1.empty()
        user_video_placeholder = col2.empty()
        stats_placeholder = col3.empty()

        correct_steps = 0
        total_frames = 0
        frame_skip_rate = 1  # Process every n'th frame

        while st.session_state.playing:
            for _ in range(frame_skip_rate):
                cap_benchmark.read()

            ret_benchmark, frame_benchmark = cap_benchmark.read()
            ret_user, frame_user = cap_user.read()

            if not ret_benchmark or not ret_user:
                break

            total_frames += 1

            # Pose detection and drawing
            image_benchmark = cv2.cvtColor(frame_benchmark, cv2.COLOR_BGR2RGB)
            image_user = cv2.cvtColor(frame_user, cv2.COLOR_BGR2RGB)
            results_user = pose.process(image_user)
            results_benchmark = pose.process(image_benchmark)

            if results_user.pose_landmarks:
                mp_drawing.draw_landmarks(image_user, results_user.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Display videos
            benchmark_video_placeholder.image(image_benchmark, channels="RGB", use_column_width=True)
            user_video_placeholder.image(image_user, channels="BGR", use_column_width=True)

            error = cosine_distance(results_user.pose_landmarks, results_benchmark.pose_landmarks) * 100
            correct_step = error < 30
            correct_steps += correct_step

            stats = f"""
                Frame Error: {error:.2f}%\n
                Step: {'CORRECT STEP' if correct_step else 'WRONG STEP'}\n
                Cumulative Accuracy: {(correct_steps / total_frames) * 100:.2f}%
            """
            stats_placeholder.markdown(stats)

        cap_benchmark.release()
        cap_user.release()