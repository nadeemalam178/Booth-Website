"""
Extract booth mapping from PDF 2 using text extraction
and inspect its structure.
"""
import pymupdf
import re

MAPPING_PDF = r"c:\Users\alamn\Downloads\Antigravity\Booth Wise Team Mapping Bankipur - Cleaned_Data (1).pdf"

doc = pymupdf.open(MAPPING_PDF)
print(f"Total pages: {len(doc)}")

# Print first 3 pages text
for pg in range(min(3, len(doc))):
    page = doc[pg]
    text = page.get_text("text")
    print(f"\n{'='*60}")
    print(f"PAGE {pg+1}")
    print('='*60)
    print(text[:3000])

doc.close()
