from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas

# Create the first image
image1 = Image.new("RGB", (800, 300), "white")
draw1 = ImageDraw.Draw(image1)

draw1.text(
    (40, 80),
    "Page 1: Welcome to OCR Learning!",
    fill="black"
)

draw1.text(
    (40, 140),
    "Python helps us extract text from images.",
    fill="black"
)

image1.save("page1.png")


# Create the second image
image2 = Image.new("RGB", (800, 300), "white")
draw2 = ImageDraw.Draw(image2)

draw2.text(
    (40, 80),
    "Page 2: OCR means Optical Character Recognition.",
    fill="black"
)

draw2.text(
    (40, 140),
    "It converts image text into machine-readable text.",
    fill="black"
)

image2.save("page2.png")


# Create a PDF containing both images
pdf = canvas.Canvas("sample_document.pdf", pagesize=(800, 300))

pdf.drawImage("page1.png", 0, 0, width=800, height=300)
pdf.showPage()

pdf.drawImage("page2.png", 0, 0, width=800, height=300)
pdf.showPage()

pdf.save()

print("PDF created successfully!")
print("File name: sample_document.pdf")
print("Number of pages: 2")

