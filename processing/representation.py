
import cv2
import numpy as np
def detect_pothole(original_image):
    if original_image is None or not isinstance(original_image, np.ndarray):
        print("Error: Invalid input image!")
        return None
    # Convert to grayscale
    gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Use adaptive thresholding or Otsu's thresholding for segmentation
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Initialize variable for largest contour (assuming it's the pothole)
    max_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:  # Find the largest contour
            max_area = area
            max_contour = contour
    if max_contour is not None:
        # Draw bounding box around the largest detected pothole
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Green box
        # Add "Pothole" label above the bounding box
        text_x = x  # Align text with the left of the bounding box
        text_y = y - 10 if y - 10 > 10 else y + 20  # Adjust to avoid going out of bounds
        cv2.putText(original_image, "Pothole", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.7, (0, 255, 0), 2, cv2.LINE_AA)  # Green text
        print(f"Pothole detected! Bounding box at (x={x}, y={y}, w={w}, h={h})")
    else:
        print("No pothole detected!")
    return original_image  # Return image with bounding box and label
