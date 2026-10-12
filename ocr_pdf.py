
import pytesseract
from PIL import Image
from pathlib import Path

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Folder containing converted PDF pages
image_folder = Path("converted_images")

# File to save extracted text
output_file = Path("extracted_text.txt")

# Store text from all pages
all_text = []

# Process each page image
for image_path in sorted(image_folder.glob("page_*.png")):
    print(f"\nProcessing: {image_path.name}")

    # Open the image
    image = Image.open(image_path)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    # Store page number and extracted text
    page_text = (
        f"\n--- {image_path.name} ---\n"
        f"{extracted_text}\n"
    )

    all_text.append(page_text)

    # Display extracted text
    print(extracted_text)

# Save all extracted text to a file
output_file.write_text(
    "\n".join(all_text),
    encoding="utf-8"
)

print(f"\nOCR completed! Text saved to: {output_file}")
