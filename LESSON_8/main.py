# Creating a Face Dataset using OpenCV
# This captures images and stores them in 'datasets' folder under the name 'sub_data'

import cv2
import os

# Load Haarcascade face detection model
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Folder where datasets will be saved
datasets = 'datasets'
sub_data = 'sneha'  # You can change this to your name or any label

# Create the path where photos will be stored
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)  # Create the folder if it does not exist

# Set the size of the face images
(width, height) = (130, 100)

# Open the webcam (0 for default webcam)
webcam = cv2.VideoCapture(0)

# Counter to keep track of how many images captured
count = 1

# Loop until 30 images are captured
while count <= 30:
    success, frame = webcam.read()
    if not success:
        print("Failed to capture image")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)  # Detect faces
    
    for (x, y, w, h) in faces:
        # Draw rectangle around detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Extract and resize the face region
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        
        # Save the captured face image
        file_path = os.path.join(path, f'{count}.png')
        cv2.imwrite(file_path, face_resize)
        print(f"Saved {file_path}")
        
        count += 1  # Increment only when a face is found
    
    # Show the current frame
    cv2.imshow('Capturing Faces', frame)
    
    # Press 'ESC' key to exit early
    key = cv2.waitKey(10)
    if key == 27:  # ASCII for ESC key
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
print("Dataset creation completed.")
