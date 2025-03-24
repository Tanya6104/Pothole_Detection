import cv2
import numpy as np

def enhance(image):
    if image is None or not isinstance(image, np.ndarray):
        print("Enhancement Error: Invalid input image!")
        return None

    # Convert to grayscale if necessary
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
    print("Grayscale Shape:", grayscale_image.shape, "Type:", grayscale_image.dtype)

    # Apply Histogram Equalization
    hist_eq_image = cv2.equalizeHist(grayscale_image)
    print("Histogram Equalized Shape:", hist_eq_image.shape, "Type:", hist_eq_image.dtype)

    if hist_eq_image is None or not isinstance(hist_eq_image, np.ndarray):
        print("Enhancement Error: Process failed!")
        return None

    return hist_eq_image  # Only returning histogram-equalized image
