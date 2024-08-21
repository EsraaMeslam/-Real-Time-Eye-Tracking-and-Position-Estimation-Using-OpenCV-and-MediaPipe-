# Real-Time Eye Tracking and Position Estimation

## Overview
This project implements a real-time eye-tracking system using OpenCV and MediaPipe. The code tracks the user's eye position (left, right, or center) and displays it on the screen. The system works by detecting facial landmarks, extracting eye regions, and estimating the eye's position based on pixel analysis.

## Files
Eye_Tracking.py: Main script that captures video input, processes each frame to detect eyes, and estimates eye position.
utils.py: Utility functions for drawing colored backgrounds and text on images.

## Features

- **Real-Time Tracking**: Detects eye landmarks using MediaPipe Face Mesh.
- **Eye Region Extraction**: Extracts and displays regions of interest from the eyes.
- **Position Estimation**: Classifies eye position (CENTER, LEFT, RIGHT) based on pupil location.
- **Live Visualization**: Displays eye tracking and position estimation on the video feed.

## Dependencies

Ensure you have Python 3.x installed. The following packages are required:

- OpenCV
- MediaPipe
- NumPy

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/EsraaMeslam/-Real-Time-Eye-Tracking-and-Position-Estimation-Using-OpenCV-and-MediaPipe-.git
    cd Real-Time-Eye-Tracking-and-Position-Estimation-Using-OpenCV-and-MediaPipe
    ```


2. **Install Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare Your Video File:**
   
   Place your video file in the project directory and name it `eye.mp4`. Alternatively, update the `cv2.VideoCapture("eye.mp4")` line in `Eye_Tracking.py` with the path to your video file.

2. **Run the Script:**

    ```bash
    python Eye_Tracking.py
    ```

3. **View Results:**
   
   The application will open a window showing the real-time video feed with eye tracking and position estimation. Press `q` to quit the application.

## File Descriptions

- **`Eye_Tracking.py`**: Main script for eye tracking. Captures video, processes frames to detect facial landmarks, extracts eye regions, estimates eye position, and displays results.
- **`utils.py`**: Utility functions for text rendering and color management used in the eye tracking script.
- **`requirements.txt`**: Lists the required Python packages for the project.

## Example Output

- **Real-Time Eye Tracking Window**: Shows the original video with outlined eye regions and estimated eye position.
- **Eye Region Windows**: Displays cropped regions of the left and right eyes.

## Notes

- Ensure that the video file is in a compatible format and accessible from the script.
- Adjust script parameters as needed for better accuracy or different video resolutions.


## Acknowledgments

- **MediaPipe**: For providing a powerful library for facial landmark detection.
- **OpenCV**: For its robust image processing capabilities.

For issues or contributions, please open an issue or pull request on the [GitHub repository]([https://github.com/yourusername/eye-tracking](https://github.com/EsraaMeslam/-Real-Time-Eye-Tracking-and-Position-Estimation-Using-OpenCV-and-MediaPipe-)).

