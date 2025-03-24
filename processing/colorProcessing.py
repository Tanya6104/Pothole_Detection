import cv2
import numpy as np

def highlight_potholes(image, edges):
    """
    Highlights detected pothole regions using color overlays.
    
    Parameters:
    - image: Original image (BGR format).
    - edges: Edge-detected image from segmentation (grayscale).

    Returns:
    - Image with pothole regions highlighted in yellow.
    """
    # Validate inputs
    if image is None or edges is None:
        print("Error: Image or edges is None")
        return None
    
    if not isinstance(image, np.ndarray) or not isinstance(edges, np.ndarray):
        print("Error: Inputs must be NumPy arrays")
        return None

    if len(image.shape) != 3 or image.shape[2] != 3:
        print("Error: Image must be a BGR color image")
        return None
    
    if len(edges.shape) != 2:
        print("Error: Edges must be a grayscale image")
        return None

    # Convert the image to HSV for better color handling
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Find contours from the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Highlight detected potholes in yellow
    for cnt in contours:
        cv2.drawContours(hsv, [cnt], 0, (30, 255, 255), -1)  # Yellow in HSV

    # Convert back to BGR
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

