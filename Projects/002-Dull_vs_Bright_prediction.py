# Dull images tend to have low saturation and value (brightness), while bright images have higher values for both. We can use thresholds to classify an image as dull or bright based on these properties.

import numpy as np
import cv2

def predict_dull_vs_bright(image_path):
    # Load the image and convert to HSV
    image = cv2.imread(image_path)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Get the saturation and value (brightness) channels
    saturation = image_hsv[:, :, 1]
    value = image_hsv[:, :, 2]
    
    # Define thresholds for dull (low saturation and brightness)
    dull_saturation_threshold = 80
    dull_value_threshold = 100
    
    # Calculate the percentage of dull pixels
    dull_mask = (saturation < dull_saturation_threshold) & (value < dull_value_threshold)
    dull_percentage = np.sum(dull_mask) / saturation.size * 100
    
    # Decide whether the image is dull or bright
    if dull_percentage > 50:  # If more than 50% of the image is dull
        prediction = "Dull"
    else:
        prediction = "Bright"
    
    print(f"Dull Pixels: {dull_percentage:.2f}%")
    
    return prediction

predict_dull_vs_bright('./Data/beach.jpg')