# Football-Video-Analysis-System-with-YOLO-OpenCV-and-Python

##  Project Overview
This project is a comprehensive football analysis system that uses state-of-the-art machine learning, computer vision, and deep learning techniques to track players, calculate ball possession, and analyze player performance in real-time. The system leverages YOLOv8 for object detection, custom-trained models, KMeans clustering for team assignment, and advanced techniques like optical flow and perspective transformation.

## Output Showcase
Witness the power of this system with real-time statistics overlaid on the video, offering a comprehensive view of player dynamics and team analysis
![Screenshot](Screenshot 2025-03-02 031358.PNG)

## Watch The Output 
[![Watch the video]](https://www.youtube.com/watch?v=0uYj7tGOSAA)


## Features
- **Object Detection**: Utilizes YOLOv8 to detect players, referees, and the football in real-time.
- **Custom YOLO Model**: Fine-tuned and trained a custom object detection model for enhanced accuracy.
- **Team Assignment**: Uses KMeans clustering to segment player t-shirt colors and automatically assign players to teams.
- **Real-Time Ball Possession**: Tracks player-ball interactions to calculate real-time ball possession for each team.
- **Optical Flow**: Measures camera movement between frames to ensure accurate player tracking.
- **Perspective Transformation**: Converts player movement from pixel distances to real-world meters, providing more meaningful performance data.
- **Player Performance Analysis**: Calculates player speed and total distance covered during the match.

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenCV
- YOLOv11 (Ultralytics)
- NumPy
- SciKit-Learn
- Pandas
- Matplotlib
