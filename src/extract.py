import argparse
import csv
import re
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
import pytesseract

# A documented baseline heuristic; adapt only using development data.
TAG_PATTERN = re.compile(r"\b[A-Z]{1,4}[-–]\d{2,5}[A-Z]?\b")

def extract_tags(path):
    image = Image.open(path).convert("RGB")
    gray = ImageOps.grayscale(image)
    gray = ImageEnhance.Contrast(gray).enhance(1.8)
    text = pytesseract.image_to_string(gray, config="--psm 11")
    return [m.group().upper().replace("–", "-") for m in TAG_PATTERN.finditer(text.upper())]

def run(input_dir, output_file):
    images = sorted(p for p in Path(input_dir).iterdir() if p.suffix.lower() in {".png",".jpg",".jpeg",".tif",".tiff"})
    if not images:
        raise ValueError("No supported image files found.")
    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["drawing_id","tag"])
        writer.writeheader()
        for image in images:
            for tag in extract_tags(image):
                writer.writerow({"drawing_id": image.stem, "tag": tag})
    print(f"Processed {len(images)} drawing(s); predictions: {output_file}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    run(args.input, args.output)

if __name__ == "__main__":
    main()
