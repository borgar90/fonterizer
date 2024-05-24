import cv2
import pytesseract
from PIL import Image

def preprocess_image(image_path):
    """ Load the image and convert it to grayscale for better OCR accuracy. """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Optionally, you can apply thresholding, dilation, or erosion here if needed
    return gray

def extract_text_from_image(image):
    """ Use pytesseract to extract text from the processed image. """
    # Configure tesseract to recognize only letters
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(image, config=custom_config)
    return text

def main():
    image_path = 'path_to_your_image.png'
    processed_image = preprocess_image(image_path)
    text = extract_text_from_image(processed_image)
    print("Recognized Text:", text)

if __name__ == "__main__":
    main()
