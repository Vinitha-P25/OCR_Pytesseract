import pytesseract
from PIL import Image
from pathlib import Path

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Folder containing preprocessed images
image_folder = Path("preprocessed_images")

# Extract text from each image
for image_path in sorted(image_folder.glob("*.png")):

    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    print(f"\nProcessing: {image_path.name}")
    print("-" * 40)
    print(text)
    print("-" * 40)