import cv2
import numpy as np
import pytesseract

# Read the image containing circled answers
image = cv2.imread('img.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Detect circles using HoughCircles
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=100, param2=30, minRadius=20, maxRadius=40)

# Ensure circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    # Loop over detected circles and extract text inside each circle
    for (x, y, r) in circles:
        # Ensure circle coordinates are within image boundaries
        if x - r >= 0 and y - r >= 0 and x + r < image.shape[1] and y + r < image.shape[0]:
            # Crop circle area from image
            crop_img = image[y-r:y+r, x-r:x+r]
            
            # Perform OCR on cropped image
            text = pytesseract.image_to_string(crop_img, config='--psm 6')  # PSM 6 assumes a single uniform block of text
            # if text.strip() in string.digits:
            print("Answer:", text.strip())
            
            # check if there is digit in the text
            # if any(char.isdigit() for char in text):
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            # else:
            #     print("Answer: Not detected")

    # Show the image with detected circles
    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()