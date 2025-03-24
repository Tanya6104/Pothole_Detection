import cv2
import numpy as np

def detect_objects(image):
    if image is None or not isinstance(image, np.ndarray):
        print("Object Recognition Error: Invalid input image!")
        return None

    # Convert to grayscale if image has color channels
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, 50, 150)

    # Apply morphological closing to remove gaps
    kernel = np.ones((3, 3), np.uint8)
    closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(closed_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area (ignore small detections)
    min_contour_area = 100  # Adjust as needed
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Convert grayscale to BGR to draw colored contours
    output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output, filtered_contours, -1, (0, 255, 0), 2)  # Green contours

    print(f"Object Recognition Successful - {len(filtered_contours)} objects detected")

    return output
