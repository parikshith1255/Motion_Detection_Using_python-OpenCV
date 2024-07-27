import cv2

# Load and preprocess background image
background = cv2.imread(r"C:\Users\91630\Downloads\background.png")
background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
background = cv2.GaussianBlur(background, (21, 21), 0)

# Open video file or capture device
video = cv2.VideoCapture(r"C:\Users\91630\Downloads\istockphoto-1336889543-640_adpp_is.mp4")

# Get video frame width and height
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Resize background to match video frame size
background = cv2.resize(background, (frame_width, frame_height))

while True:
    status, frame = video.read()
    if not status:
        break  # Exit loop if video ends or cannot read frame

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Compute the absolute difference between background and frame
    diff = cv2.absdiff(background, gray)
    
    # Reduce the background noise using threshold function
    thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    # Use the contour tool to find contours in the threshold image
    cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) <7000:
              continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the result
    cv2.imshow('All Count Show', frame)
    # Uncomment the following lines if you want to see additional outputs
    # cv2.imshow('Threshold Video', thresh)
    # cv2.imshow('Diff Video', diff)
    # cv2.imshow('Gray Video', gray)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy all windows
video.release()
cv2.destroyAllWindows()

