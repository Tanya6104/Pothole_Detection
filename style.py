import tkinter as tk
from tkinter import ttk
from main import open_image, apply_enhancement, apply_restoration, apply_morphology, apply_segmentation, apply_object_recognition, apply_representation

def create_ui():
    root = tk.Tk()
    root.title("Pothole Detection System")
    root.geometry("1100x750")
    root.configure(bg="#2c3e50")  # Dark background

    # Style configuration
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10, background="#3498db", foreground="white")
    style.configure("TLabel", font=("Arial", 12), background="#2c3e50", foreground="white")

    # Frame for buttons
    frame_buttons = ttk.Frame(root)
    frame_buttons.pack(pady=20)

    buttons = [
        ("Enhancement", apply_enhancement),
        ("Restoration", apply_restoration),
        ("Morphology", apply_morphology),
        ("Segmentation", apply_segmentation),
        ("Object Recognition", apply_object_recognition),
        ("Representation", apply_representation)
    ]

    # Create buttons dynamically
    for i, (text, command) in enumerate(buttons):
        ttk.Button(frame_buttons, text=text, command=command).grid(row=i // 3, column=i % 3, padx=10, pady=10)

    # Open Image Button
    ttk.Button(root, text="Open Image", command=open_image).pack(pady=20)

    # Image panels
    panel_original = ttk.Label(root, text="Original Image", anchor="center")
    panel_original.pack(pady=10)

    panel_processed = ttk.Label(root, text="Processed Image", anchor="center")
    panel_processed.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
