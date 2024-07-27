# Motion_Detection_Using_python-OpenCV
This project demonstrates a basic motion detection system using OpenCV, a powerful computer vision library
Techniques Used

# OpenCV Library:

A popular computer vision library used to process images and videos.

# Background Subtraction:

We use a static background image and compare it to each frame of the video to detect changes or motion.

# Grayscale Conversion:

Converts color images to grayscale to simplify processing by reducing the amount of data.

# Gaussian Blur:

Applies a blur effect to the images to reduce noise and improve the accuracy of motion detection.

# Absolute Difference:

Computes the difference between the background and the current frame to highlight areas of change.

# Thresholding:

Creates a binary image where significant changes are highlighted, making it easier to detect motion.

# Contour Detection:

Finds and outlines the shapes of moving objects based on the thresholded image.

# Drawing Rectangles:

Marks detected moving objects with rectangles for visualization.

# Knowledge Gained

# Image Preprocessing:

Understanding how to convert images to grayscale and apply blurring to prepare for motion detection.
Motion Detection Basics:

Learning how to compare images to detect changes and isolate moving objects.
Contour and Shape Detection:

Gaining skills in finding and drawing contours to highlight objects of interest.
Video Processing:

Handling video frames and applying image processing techniques in real-time.

##  Conclusion
This project showcases the fundamental techniques of motion detection and provides a practical understanding of how to use OpenCV for real-time video analysis. By combining grayscale conversion, blurring, thresholding, and contour detection, you can identify and highlight moving objects effectively.
