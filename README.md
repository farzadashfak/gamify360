# Gamify 360

## Inspiration
Inspired by the dedication of gamers, Gamify 360 aims to channel this commitment into achieving real-life goals. Observing gamers' year-long streaks, we envisioned utilizing this "stickiness" to motivate daily activities, allowing users to earn real money through Solana NFTs by completing real-life challenges.

## What It Does
Gamify 360 uses state-of-the-art computer vision, generative AI, and pose estimation technology to transform everyday activities like yoga, sketching, and working out into thrilling adventures. Activities such as cooking and cleaning become competitive games, with users earning coins for their engagement and accuracy. These coins can then be converted into NFTs, offering real value for traditionally mundane tasks and inviting users to transform ordinary moments into extraordinary opportunities.

## How We Built It
The project, a web-based application with an intuitive UI, integrates camera-based models for different activities. Our team split the work: handling OpenCV models and Solana, front-end development, and integrating Python scripts into the webpage. Despite challenges with Flask and React integration leading to lag, we discovered Streamlit, an open-source framework ideal for our needs, allowing us to embed Python scripts onto webpages efficiently.

## Challenges We Ran Into
The main challenge was the lag caused by integrating heavy OpenCV models on a Flask-based webpage. After attempting different Python frameworks, we turned to Streamlit, which proved to be a game-changer for embedding scripts into webpages.

## Accomplishments That We're Proud Of
We are particularly proud of employing generative AI to detect the interactions of objects with a 78% accuracy rate, a significant achievement in computer vision technology. This capability allows our model to track a wide range of activities without compromising accuracy.

## What We Learned
The development process highlighted the challenges of integrating computer vision and machine learning models into applications. The need to pivot to new technologies like Streamlit emphasized the importance of adaptability and leveraging team expertise for effective problem-solving.

## What's Next for Gamify 360
We plan to expand Gamify 360 by creating virtual worlds tailored to various interests, enhancing social features for community building, and introducing AI to personalize user experiences. Our goal is to make daily routines more enjoyable and rewarding, turning productivity into an innovative and fun adventure.

## Built With
- CSS3
- cv2
- Flask
- HTML
- JavaScript
- MediaPipe
- NumPy
- PoseNet
- Python
- React
- Rust
- Solana
- Streamlit
