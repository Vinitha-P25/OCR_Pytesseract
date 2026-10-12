
from pdf2image import convert_from_path
from pathlib import Path

# PDF file path
pdf_path = "sample_document.pdf"

# Poppler executable directory
poppler_path = (
    r"C:\Users\Aadi Rhythm\Downloads\Release-26.09.0-0"
    r"\poppler-26.09.0\Library\bin"
)

# Folder to save converted images
output_folder = Path("converted_images")
output_folder.mkdir(exist_ok=True)

# Convert PDF pages into images
pages = convert_from_path(
    pdf_path,
    dpi=200,
    poppler_path=poppler_path
)

# Save each page as an image
for page_number, page in enumerate(pages, start=1):
    image_path = output_folder / f"page_{page_number}.png"
    page.save(image_path, "PNG")
    print(f"Saved: {image_path}")

print(f"\nTotal pages converted: {len(pages)}")