# Round1A

# Round 1A – Understand Your Document
Adobe India Hackathon – Connecting the Dots Challenge

## Problem Statement
Build a system that extracts a **structured outline (Title, H1, H2, H3 headings)** from a given PDF and outputs it as a clean JSON file. This will act as the foundation for semantic document understanding.

---

## Input / Output
**Input:**  
- PDF file(s) (up to 50 pages) placed in `/app/input`

**Output:**  
- JSON files in `/app/output`, matching the format:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}

Approach
PDF Parsing

Use a PDF parsing library (e.g., PyMuPDF or pdfplumber) to extract text, fonts, and positions.

Heading Detection

Identify headings based on:

Font size and style patterns

Text positioning and whitespace analysis

Heuristic rules for distinguishing titles vs sections

Hierarchy Assignment

Apply clustering of styles to determine levels: Title > H1 > H2 > H3.

Output Generation

Store the extracted structure in JSON format.

Constraints handled:

Offline execution (no internet)

≤10s runtime for 50-page PDFs

No GPU dependencies

Libraries / Tools
Python 3.x

PyMuPDF (fitz) / pdfplumber

json

Docker (for containerization)

How to Build & Run
Build Docker Image
bash
Copy
Edit
docker build --platform linux/amd64 -t pdf_outline_extractor:latest .
Run the Container
bash
Copy
Edit
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none pdf_outline_extractor:latest
Notes
All PDFs from /app/input will be processed and corresponding JSON files will be saved in /app/output.

No internet access required.
