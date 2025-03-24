import cv2

def compress_image(image, output_path="compressed_pothole.jpg", quality=50):
    """
    Compresses the image to reduce file size while maintaining quality.
    
    Parameters:
    - image: Input image to compress.
    - output_path: Path where the compressed image will be saved.
    - quality: Compression quality (1-100, higher means better quality).
    
    Returns: Path to the compressed image.
    """
    cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
    return output_path

# **Test the function (Uncomment if running standalone)**
# from processing.imageAcquisition import acquire_image
# image, path = acquire_image()
# if image is not None:
#     compressed_path = compress_image(image)
#     print(f"Compressed image saved at: {compressed_path}")
