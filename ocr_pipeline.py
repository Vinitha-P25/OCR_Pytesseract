
from pathlib import Path
import re

import pytesseract
from PIL import Image
from pdf2image import convert_from_path


# Step 1: Configure Tesseract
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Step 2: Define paths
pdf_path = Path("sample_document.pdf")
image_folder = Path("converted_images")
output_folder = Path("preprocessed_images")
text_file = Path("cleaned_text.txt")

# Step 3: Check whether the PDF exists
if not pdf_path.exists():
    raise FileNotFoundError(
        f"PDF not found: {pdf_path.resolve()}"
    )

# Create output folders
image_folder.mkdir(exist_ok=True)
output_folder.mkdir(exist_ok=True)

# Step 4: Convert PDF pages into images
print("Converting PDF pages into images...")

pages = convert_from_path(
    str(pdf_path),
    poppler_path=(
        r"C:\Users\Aadi Rhythm\Downloads"
        r"\Release-26.09.0-0\poppler-26.09.0\Library\bin"
    )
)

all_text = []

# Step 5: Process each page
for page_number, page in enumerate(pages, start=1):

    print(f"\nProcessing page {page_number}...")

    # Save the original image
    original_path = image_folder / f"page_{page_number}.png"
    page.save(original_path, "PNG")

    # Resize the image
    width, height = page.size

    resized = page.resize(
        (width * 2, height * 2),
        Image.Resampling.LANCZOS
    )

    # Convert to grayscale
    gray = resized.convert("L")

    # Apply thresholding
    binary = gray.point(
        lambda pixel: 0 if pixel < 150 else 255
    )

    # Save the preprocessed image
    processed_path = output_folder / f"page_{page_number}.png"
    binary.save(processed_path)

    # Step 6: Extract text using OCR
    extracted_text = pytesseract.image_to_string(binary)

    # Step 7: Correct known spacing errors
    extracted_text = extracted_text.replace(
        "toOCR", "to OCR"
    )

    extracted_text = extracted_text.replace(
        "Itconverts", "It converts"
    )

    # Remove repeated spaces
    extracted_text = re.sub(
        r"[ \t]+", " ", extracted_text
    )

    print(f"Extracted text from page {page_number}:")
    print(extracted_text)

    all_text.append(
        f"--- Page {page_number} ---\n{extracted_text.strip()}"
    )

# Step 8: Save the complete text
final_text = "\n\n".join(all_text)

text_file.write_text(
    final_text + "\n",
    encoding="utf-8"
)

print("\nOCR pipeline completed successfully!")
print(f"Pages processed: {len(pages)}")
print(f"Final text saved to: {text_file.resolve()}")
