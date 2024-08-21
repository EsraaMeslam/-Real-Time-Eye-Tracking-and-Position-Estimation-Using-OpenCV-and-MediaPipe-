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

## Installation

1. **Clone the Repository:**
   ```bash
  git clone <repository-url>



