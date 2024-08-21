# -Real-Time-Eye-Tracking-and-Position-Estimation-Using-OpenCV-and-MediaPipe-

# Real-Time Eye Tracking and Position Estimation

## Overview

This project is a real-time eye tracking and position estimation application that utilizes computer vision techniques. By employing OpenCV for image processing and MediaPipe for face mesh detection, the application can accurately estimate eye positions and display them in real-time. It is useful for various applications such as user interaction systems and eye-tracking studies.

## Features

- **Real-Time Eye Tracking:** Tracks and detects eye landmarks using MediaPipe's Face Mesh.
- **Eye Position Estimation:** Estimates the position of the eye (Left, Right, Center) based on detected landmarks.
- **Visual Feedback:** Displays eye tracking results and position estimation on the video feed.
- **Customizable Output:** Draws detected eye regions and provides visual feedback using color-coded text.

## Requirements

The application requires the following Python packages:

- `numpy`
- `opencv-python`
- `mediapipe`
- `utils` (Ensure `utils.py` is available in your project directory)

Install the dependencies using the following command:

```bash
pip install -r requirements.txt




Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
Navigate to the Project Directory:

bash
Copy code
cd <project-directory>
Install Dependencies:

Make sure you have Python installed. If not, download and install it from python.org. Install the required dependencies using:

bash
Copy code
pip install -r requirements.txt
Add the utils.py File:

Ensure you have a utils.py file in your project directory. This file should contain utility functions referenced in the code.

Prepare Your Video File:

Ensure that you have a video file named eye.mp4 in your project directory, or modify the cv2.VideoCapture path in the code to point to your video file.

Run the Application:

Execute the script to start the application:

bash
Copy code
python main.py
The application will open a window displaying the video feed with real-time eye tracking and position estimation.
