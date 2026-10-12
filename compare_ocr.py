
import pytesseract
from PIL import Image
from pathlib import Path

# Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Image folders
original_folder = Path("converted_images")
processed_folder = Path("preprocessed_images")

# Output file
output_file = Path("ocr_comparison.txt")

with output_file.open("w", encoding="utf-8") as file:

    for original_path in sorted(original_folder.glob("*.png")):

        processed_path = processed_folder / original_path.name

        if not processed_path.exists():
            print(f"Missing processed image: {processed_path}")
            continue

        # OCR on original image
        original_image = Image.open(original_path)
        original_text = pytesseract.image_to_string(original_image)

        # OCR on preprocessed image
        processed_image = Image.open(processed_path)
        processed_text = pytesseract.image_to_string(processed_image)

        # Display results
        print(f"\nPage: {original_path.name}")

        print("\nOriginal OCR:")
        print(original_text)

        print("\nPreprocessed OCR:")
        print(processed_text)

        print("=" * 50)

        # Save comparison
        file.write(f"Page: {original_path.name}\n\n")

        file.write("ORIGINAL OCR:\n")
        file.write(original_text + "\n\n")

        file.write("PREPROCESSED OCR:\n")
        file.write(processed_text + "\n")

        file.write("=" * 50 + "\n\n")

print(f"\nComparison saved to: {output_file}")

