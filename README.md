# OCR Pipeline Using Python and Pytesseract

## Project Overview

This project demonstrates Optical Character Recognition (OCR) using Python and Pytesseract. It converts a PDF document into images, preprocesses the images to improve text readability, extracts text, and saves the results in a text file.

## Technologies Used

* Python
* Pytesseract
* Tesseract OCR Engine
* Pillow
* pdf2image
* Poppler

## Features

* Convert multi-page PDF documents into images.
* Extract text from images using Pytesseract.
* Convert images to grayscale.
* Resize images to improve text readability.
* Apply thresholding to separate text from the background.
* Compare OCR results before and after preprocessing.
* Clean common OCR spacing errors.
* Save extracted text to a text file.
* Process multiple pages automatically.

## Project Files

| File                   | Description                             |
| ---------------------- | --------------------------------------- |
| `ocr_pipeline.py`      | Complete PDF-to-text OCR pipeline       |
| `ocr_pdf.py`           | Extract text from converted PDF images  |
| `pdf_to_images.py`     | Convert PDF pages into images           |
| `preprocess_ocr.py`    | Resize, grayscale, and threshold images |
| `ocr_preprocessed.py`  | Extract text from preprocessed images   |
| `compare_ocr.py`       | Compare OCR results                     |
| `clean_ocr_text.py`    | Clean extracted OCR text                |
| `create_sample_pdf.py` | Create a sample PDF for testing         |
| `sample_document.pdf`  | Sample two-page PDF                     |
| `sample_image.png`     | Sample image for OCR testing            |

## Requirements

* Python
* Tesseract OCR
* Poppler for Windows

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Install Tesseract OCR and Poppler separately, and configure their executable paths in the Python scripts where required.

## How to Run

1. Clone or download this repository.
2. Install the required Python libraries.
3. Install Tesseract OCR and Poppler.
4. Make sure the executable paths are correctly configured.
5. Place your input PDF in the project folder.
6. Update the PDF filename in `ocr_pipeline.py` if necessary.
7. Run:

```bash
python ocr_pipeline.py
```

## Output

The pipeline converts PDF pages into images, preprocesses each page, extracts text, and saves the cleaned result in `cleaned_text.txt`.

## Learning Outcomes

This project provides practical experience with Python scripting, PDF processing, image preprocessing, OCR, text cleaning, and multi-page document automation.
