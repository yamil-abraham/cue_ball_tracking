import cv2
import numpy as np
from kalmanfilter import KalmanFilter # import Kalman Filter from kalmanfilter.py file

# Past the path video
cap = cv2.VideoCapture("\path...\shot.mp4")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

''' Adjust this value according to the size of the ball. Particularly for this video I got some issues. 
- If the value is <14 the tip of the cue stick could be detected
- If the value is >14 I lost accuracy to detect the cue ball
'''
min_area = 14  

# Create Kalman Filter instance
kf = KalmanFilter()

# Main loop that runs as long as the video is open
while cap.isOpened():
    ret, frame = cap.read() # Read the next frame from the video
    if not ret: # If there is not frame, break the loop
        break

    # Convert the frame to greyscale for processing 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply a Gaussian blur to smooth the frame and reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply a threshold to create a binary image where the cue ball will be highlighted
    ret, thresh = cv2.threshold(blurred, 245, 255, cv2.THRESH_BINARY)

    # Find the contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Iterate on each contour found
    for contour in contours:
        if cv2.contourArea(contour) > min_area: # If the contour area is largar than the minimum defined area, process the contour
            (x, y), radius = cv2.minEnclosingCircle(contour) # Find the minimum circle enclosing the contour
            x, y, radius = int(x), int(y), int(radius) # Make sure that the coordinates and radius are integers so that they can be drawn
            cv2.circle(frame, (x, y), radius, (0, 255, 0), 2) # Draw a green circle around the detected outline

            # Apply the Kalman filter to predict the position/trajectory
            predicted = kf.predict(x, y)
            # Draw a red circle at the current position
            cv2.circle(frame, (x, y), 20, (0, 0, 255), 4)

            # Extract the predicted coordinates and ensure they are integers
            predicted_coords = (predicted[0][0], predicted[0][1])
            # Draw a blue circle at the position predicted by the Kalman filter
            cv2.circle(frame, predicted_coords, 20, (255, 0, 0), 4)

    # Write the frame with circles
    out.write(frame)

    # Display the processed frame through a window
    cv2.imshow('Frame', frame)

    # Wait for a key for 10ms and if 'q' is pressed, break the loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Free the video and destroy all windows opened by OpenCV
cap.release()
out.release()  # Do not forget to release the VideoWriter
cv2.destroyAllWindows()
