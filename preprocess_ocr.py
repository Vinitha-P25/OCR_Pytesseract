
from PIL import Image
from pathlib import Path

image_folder = Path("converted_images")
output_folder = Path("preprocessed_images")

output_folder.mkdir(exist_ok=True)

for image_path in sorted(image_folder.glob("*.png")):

    # Open image
    image = Image.open(image_path)

    # Resize to twice the original dimensions
    new_width = image.width * 2
    new_height = image.height * 2

    image = image.resize(
        (new_width, new_height),
        Image.Resampling.LANCZOS
    )

    # Convert to grayscale
    gray_image = image.convert("L")

    # Apply thresholding
    threshold = 150

    binary_image = gray_image.point(
        lambda pixel: 0 if pixel < threshold else 255
    )

    # Save processed image
    output_path = output_folder / image_path.name
    binary_image.save(output_path)

    print(f"Processed: {image_path.name}")
    print(f"Original size: {Image.open(image_path).size}")
    print(f"New size: {new_width} x {new_height}")
    print(f"Saved to: {output_path}")
