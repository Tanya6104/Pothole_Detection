import cv2
import numpy as np

def restore(image):
    if image is None or not isinstance(image, np.ndarray):
        print("Restoration Error: Invalid input image!")
        return None
    
    # Ensure image has valid channels
    if len(image.shape) == 3:  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    try:
        restored_image = cv2.GaussianBlur(image, (5,5), 0)
    except Exception as e:
        print(f"GaussianBlur Failed: {e}")
        return None
    
    print(" Restoration Successful - Shape:", restored_image.shape, "Type:", restored_image.dtype)
    return restored_image
