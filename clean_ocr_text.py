
from pathlib import Path
import re

# Input and output files
input_file = Path("extracted_text.txt")
output_file = Path("cleaned_text.txt")

# Read extracted OCR text
text = input_file.read_text(encoding="utf-8")

# Correct known OCR spacing errors
corrections = {
    "toOCR": "to OCR",
    "Itconverts": "It converts"
}

for wrong, correct in corrections.items():
    text = text.replace(wrong, correct)

# Remove unnecessary spaces
text = re.sub(r"[ \t]+", " ", text)

# Reduce excessive blank lines
text = re.sub(r"\n{3,}", "\n\n", text)

# Save cleaned text
output_file.write_text(text.strip() + "\n", encoding="utf-8")

print("OCR text cleaned successfully!")
print(f"Cleaned text saved to: {output_file}")

print("\nCleaned OCR Text:")
print("-" * 40)
print(text)
print("-" * 40)
