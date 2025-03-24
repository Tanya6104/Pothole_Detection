import tkinter as tk
from tkinter import filedialog, Label, Button, Frame, ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

# Import processing modules (Ensure these exist and return images)
import processing.imageEnhancement as imgEnh
import processing.imageRestoration as imgRest
import processing.morphologicalProcessing as imgMorph
import processing.segmentation as imgSeg
import processing.objectRecognition as objRec
import processing.representation as imgRep

# Initialize Tkinter window
root = tk.Tk()
root.title("Pothole Detection System")
root.geometry("1000x700")
root.configure(bg="#2C3E50")  # Dark Blue-Grey Background

# Global variables to store images
original_img = None
processed_img = None

# Function to open an image
def open_image():
    global original_img, processed_img
    
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (400, 300))

    original_img = img
    processed_img = img.copy()
    
    display_image(original_img, panel_original)

# Function to display an image on a label
def display_image(image, panel):
    if image is None:
        print("No image to display.")
        return
    
    img_pil = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(img_pil)
    panel.config(image=img_tk)
    panel.image = img_tk

def display_multiple_images(image_dict, function_name):
    """
    Displays multiple images in a scrollable new window.
    :param image_dict: Dictionary containing multiple output images.
    :param function_name: Name of the processing function.
    """
    top = tk.Toplevel(root)
    top.title(f"{function_name} Results")
    top.geometry("600x400")  # Set initial window size

    # Create a Canvas for scrolling
    canvas = tk.Canvas(top)
    scrollbar = tk.Scrollbar(top, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    # Configure scrollbar
    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    row, col = 0, 0
    for name, img in image_dict.items():
        img_pil = Image.fromarray(img)
        img_tk = ImageTk.PhotoImage(img_pil)

        panel = Label(scroll_frame, text=name, font=("Arial", 12, "bold"), bg="#222", fg="white")
        panel.grid(row=row, column=col, padx=10, pady=10, sticky="w")

        image_label = Label(scroll_frame, image=img_tk, bg="#333")
        image_label.image = img_tk  # Keep reference to avoid garbage collection
        image_label.grid(row=row+1, column=col, padx=10, pady=10, sticky="w")

        col += 1
        if col > 2:  # Arrange in rows of 3 images
            col = 0
            row += 2  # Move to next row


# Function to apply processing
def apply_processing(process_function, function_name, multiple_outputs=False):
    global processed_img
    if processed_img is None:
        print(f"Error: No image loaded before applying {function_name}.")
        return
    
    try:
        print(f"Applying {function_name}...")
        result = process_function(processed_img)
        
        if multiple_outputs and isinstance(result, dict):
            display_multiple_images(result, function_name)
        else:
            processed_img = result
            display_image(processed_img, panel_processed)
    except Exception as e:
        print(f"Error in {function_name}: {e}")
# Function to apply segmentation separately
def apply_segmentation():
    global processed_img
    if processed_img is None:
        print("Error: No image loaded before applying Segmentation.")
        return
    
    try:
        print(f"Applying Segmentation... Input type: {type(processed_img)} Shape: {processed_img.shape if isinstance(processed_img, np.ndarray) else 'N/A'}")

        # Expecting a tuple (edges, otsu_thresh)
        result = imgSeg.segment(processed_img)

        if result is None or not isinstance(result, tuple) or len(result) != 2:
            print("Error: Segmentation did not return valid images.")
            return

        edges, otsu = result  # Extract both outputs

        if edges is None or otsu is None or not isinstance(edges, np.ndarray) or not isinstance(otsu, np.ndarray):
            print("Error: Segmentation did not return valid images.")
            return

        print("Segmentation successful! Displaying results...")

        # Display both images in a new window
        display_multiple_images({"Canny Edges": edges, "Otsu Threshold": otsu}, "Segmentation")

    except Exception as e:
        print(f"Error in Segmentation: {e}")

# Processing functions for buttons
def apply_enhancement():
    apply_processing(imgEnh.enhance, "Enhancement")

def apply_restoration():
    apply_processing(imgRest.restore, "Restoration")

def apply_morphology():
    apply_processing(imgMorph.process, "Morphological Processing", multiple_outputs=True)

def apply_object_recognition():
    apply_processing(objRec.detect_objects, "Object Recognition")

def apply_representation():
    apply_processing(imgRep.detect_pothole, "Representation")

def apply_segmentation():
    global processed_img
    if processed_img is None:
        print("Error: No image loaded before applying Segmentation.")
        return
    
    try:
        result = imgSeg.segment(processed_img)
        edges, otsu = result
        display_multiple_images({"Canny Edges": edges, "Otsu Threshold": otsu}, "Segmentation")
    except Exception as e:
        print(f"Error in Segmentation: {e}")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5, background="white", foreground="black")  # Change text color to black
style.map("TButton", foreground=[("active", "black")], background=[("active", "lightgray")])  # Keep text black when hovered

# UI Layout
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

buttons = [
    ("Enhancement", apply_enhancement),
    ("Restoration", apply_restoration),
    ("Morphological Processing", apply_morphology),
    ("Segmentation", apply_segmentation),
    ("Object Recognition", apply_object_recognition),
    ("Representation", apply_representation)
]

for i, (text, command) in enumerate(buttons):
    btn = ttk.Button(frame_buttons, text=text, command=command, style="TButton")
    btn.grid(row=i//3, column=i%3, padx=10, pady=10)

# Button to open an image
btn_open = ttk.Button(root, text="Open Image", command=open_image, style="TButton")
btn_open.pack(pady=10)

# Image panels
panel_original = Label(root, text="Original Image", fg="white", bg="#2C3E50", font=("Arial", 12, "bold"))
panel_original.pack()

panel_processed = Label(root, text="Processed Image", fg="white", bg="#2C3E50", font=("Arial", 12, "bold"))
panel_processed.pack()

# Run Tkinter event loop
root.mainloop()