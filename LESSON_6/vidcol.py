import os
import cv2
from PIL import Image  # Import Pillow library for image processing

# Set your working directory where images are stored
path = r'C:\Users\Snehpreet\OneDrive\Desktop\Jetlearn\Open CV\photos'
os.chdir(path)

mean_height = 0
mean_width = 0

# Collect all image files (jpg, jpeg, png) in the directory
image_files = [file for file in os.listdir('.') if file.endswith(('.jpg', '.jpeg', '.png'))]
num_of_images = len(image_files)

# Step 1: Calculate the average width and height of all images
for file in image_files:
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width += width
    mean_height += height

# Find mean dimensions
mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(f"Mean Width: {mean_width}, Mean Height: {mean_height}")

# Step 2: Resize all images to the mean dimensions
for file in image_files:
    img = Image.open(os.path.join(path, file))
    # Resize using LANCZOS resampling for high-quality downsampling
    img_resized = img.resize((mean_width, mean_height), Image.LANCZOS)
    img_resized.save(file, 'JPEG', quality=95)  # Save resized image
    print(f"{file} is resized.")

# Step 3: Create a function to generate a video from the images
def videoGenerator():
    video_name = "MyFirstVideo.avi"  # Name of the output video

    # Get a sorted list of images to maintain order
    images = sorted([img for img in os.listdir('.') if img.endswith(('.jpg', '.jpeg', '.png'))])
    
    # Read the first image to get frame size
    frame = cv2.imread(os.path.join(".", images[0]))
    height, width, layers = frame.shape

    # Define the codec and create the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for AVI files
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))  # fps=1 (frames per second)

    # Add each image as a frame into the video
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))

    # Release the video writer and close windows
    video.release()
    cv2.destroyAllWindows()
    print("Video creation completed.")

# Call the function to create video
videoGenerator()
