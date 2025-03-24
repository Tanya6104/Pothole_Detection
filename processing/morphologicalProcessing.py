import cv2
import numpy as np

def process(image):
    if image is None or not isinstance(image, np.ndarray):
        print("Morphological Processing Error: Invalid input image!")
        return None

    # Convert image to grayscale if it has color channels
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ensure image is binary for morphological operations
    _, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Define kernel for morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    try:
        # Apply morphological operations
        erosion = cv2.erode(binary, kernel, iterations=1)
        dilation = cv2.dilate(binary, kernel, iterations=1)
        opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)
        top_hat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
        bottom_hat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)

    except Exception as e:
        print(f"Morphological Processing Failed: {e}")
        return None

    print("Morphological Processing Successful")
    
    return {
        "erosion": erosion,
        "dilation": dilation,
        "opening": opening,
        "closing": closing,
        "gradient": gradient,
        "top_hat": top_hat,
        "bottom_hat": bottom_hat
    }
