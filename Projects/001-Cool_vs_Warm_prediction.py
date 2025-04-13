# Cool colors are typically in the blue and green range (hue values between 90-180 in HSV), while warm colors are in the red, orange, and yellow range (hue values between 0-60).

import cv2
import numpy as np

def predict_cool_vs_warm(image_path):
    # Load the image and convert to HSV
    image = cv2.imread(image_path)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Get the hue channel (0 index)
    hue = image_hsv[:, :, 0]
    
    # Define warm (0-60) and cool (90-180) ranges
    warm_mask = (hue >= 0) & (hue <= 60)
    cool_mask = (hue >= 90) & (hue <= 180)
    
    print(hue.size)
    
    # Calculate the percentage of warm and cool pixels
    warm_percentage = np.sum(warm_mask) / hue.size * 100
    cool_percentage = np.sum(cool_mask) / hue.size * 100
    
    # Decide which is dominant
    if warm_percentage > cool_percentage:
        prediction = "Warm"
    else:
        prediction = "Cool"
    
    print(f"Warm Pixels: {warm_percentage:.2f}%")
    print(f"Cool Pixels: {cool_percentage:.2f}%")
    
    return prediction

predict_cool_vs_warm('./Data/beach.jpg')
