

!pip install PyMuPDF
from google.colab import files
uploaded = files.upload()
# ✅ Full Title + Heading extractor using PyMuPDF
import fitz  # PyMuPDF
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = {"Title": "", "Headings": []}
    max_font_size = 0
    title = ""
    all_lines = []

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" in b:
                for l in b["lines"]:
                    for s in l["spans"]:
                        text = s["text"].strip()
                        size = s["size"]
                        if len(text) > 1:
                            all_lines.append((text, size))
                            if size > max_font_size:
                                max_font_size = size
                                title = text

    outline["Title"] = title

    for text, size in all_lines:
        if size == max_font_size:
            continue
        elif size > max_font_size * 0.85:
            outline["Headings"].append({"H1": text})
        elif size > max_font_size * 0.70:
            outline["Headings"].append({"H2": text})
        elif size > max_font_size * 0.50:
            outline["Headings"].append({"H3": text})

    return outline

if __name__ == "__main__":
    pdf_file = "/content/sample_data/ai.pdf"
    output = extract_outline(pdf_file)
    with open("output_outline.json", "w") as f:
        json.dump(output, f, indent=4)
    print("✅ Round 1A Output saved to output_outline.json")
files.download("output_outline.json")