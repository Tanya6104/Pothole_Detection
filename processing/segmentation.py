import cv2
import numpy as np

def segment(image):
    if image is None or not isinstance(image, np.ndarray):
        print("Segmentation Error: Invalid input image!")
        return None
    
    # Convert image to grayscale if needed
    if len(image.shape) == 3:  
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        image_gray = image.copy()

    # Apply Edge Detection (Canny)
    edges = cv2.Canny(image_gray, 100, 200)

    # Apply Otsu Thresholding
    _, otsu_thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if edges is None or otsu_thresh is None:
        print("Error: Segmentation failed!")
        return None

    print("Segmentation Successful - Shape:", edges.shape, "Type:", edges.dtype)
    return edges, otsu_thresh  # Return both images
