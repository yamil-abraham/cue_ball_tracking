## cue_ball_tracking
Billiard Ball Trajectory Prediction with Kalman Filter

<p align="center">
  <img src="https://github.com/yamil-abraham/cue_ball_tracking/blob/main/shot_gif.gif" alt="GIF RESUME">
</p>

## Overview
This repository contains a Python script for real-time tracking and trajectory prediction of a cue ball in a billiard game using computer vision techniques and Kalman Filter. The script cue_ball_tracking.py captures the motion of the cue ball from video input, detects its current position, and predicts future movement to assist players or analysts in understanding the dynamics of the game.

## Features
1. Real-time detection of the cue ball using OpenCV contour analysis.
2. Application of the Kalman Filter to predict the ball's trajectory based on its current and previous positions.
3. Visualization of the current position, predicted trajectory, and motion path of the cue ball within the video feed.
4. Adjustable parameters for detection sensitivity and prediction accuracy.

## How It Works
The script utilizes OpenCV to process video frames and identify the cue ball based on color and size thresholds. Upon detection, the Kalman Filter is applied to the detected positions to forecast the cue ball's trajectory. The script overlays the real-time video with markers indicating the detected position (green circle), the predicted position by the Kalman Filter (blue circle), and the actual position (red circle) for visual reference.

## Usage
The project is straightforward to run; simply clone the repository,**ensure you have the required dependencies installed (cv2 and numpy)**, and execute the script with a video file of a billiard game. Adjust the min_area parameter to match the size of the cue ball in your video feed for optimal performance. You will find the video added in this repository.

## Applications
This tool can be useful for:

1. Billiard enthusiasts and professionals who want to analyze the physics of their shots.
2. Developers looking to implement trajectory prediction in sports analytics software.
3. Researchers in the field of computer vision and object tracking.
4. Feel free to fork, star, and contribute to this repository. Any feedback or contributions to improve the project are highly welcome.


