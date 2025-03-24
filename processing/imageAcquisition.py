import cv2
from tkinter import filedialog

def acquire_image():
    """
    Opens a file dialog to let the user select an image.
    Loads the selected image using OpenCV.
    Returns the loaded image and its file path.
    """
    image_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    
    if not image_path:
        print("No image selected.")
        return None, None
    
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error loading image: {image_path}")
        return None, None

    return image, image_path

# **Test the function (Uncomment if running standalone)**
# image, path = acquire_image()
# if image is not None:
#     cv2.imshow("Acquired Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
