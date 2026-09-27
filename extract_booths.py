"""
Extract booth-wise votes from Form 20 PDF and map to wards from booth mapping PDF.
Uses PyMuPDF text extraction to read tabular data.
"""
import fitz  # PyMuPDF
import re
import json
from collections import defaultdict

FORM20_PDF   = r"c:\Users\alamn\Downloads\Antigravity\Form 20_182-Bankipur Assembly Election.pdf"
MAPPING_PDF  = r"c:\Users\alamn\Downloads\Antigravity\Booth Wise Team Mapping Bankipur - Cleaned_Data (1).pdf"

# ─── STEP 1: Extract ward→booth mapping from PDF 2 ───────────────────────────
print("=" * 60)
print("STEP 1: Parsing Booth Mapping PDF")
print("=" * 60)

doc2 = fitz.open(MAPPING_PDF)
booth_to_ward = {}   # booth_number -> ward_number

for page_num in range(len(doc2)):
    page = doc2[page_num]
    text = page.get_text("text")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    # Look for patterns like:
    # "Ward No. 15" or "Ward 15" followed by booth numbers
    # or booth number followed by ward info
    
    current_ward = None
    for line in lines:
        # Detect ward header
        ward_match = re.search(r'[Ww]ard\s*[Nn]o\.?\s*(\d+)', line)
        if ward_match:
            current_ward = int(ward_match.group(1))
        
        # Look for booth numbers in lines
        if current_ward:
            # Detect patterns like "Booth 277" or just standalone numbers
            booth_matches = re.findall(r'\b(\d{1,3})\b', line)
            for b in booth_matches:
                bnum = int(b)
                if 1 <= bnum <= 500:  # reasonable booth range
                    if bnum not in booth_to_ward:
                        booth_to_ward[bnum] = current_ward

doc2.close()
print(f"  Found {len(booth_to_ward)} booth-to-ward mappings")
print(f"  Sample: {dict(list(booth_to_ward.items())[:10])}")

# ─── STEP 2: Extract raw text from Form 20 PDF pages ────────────────────────
print("\n" + "=" * 60)
print("STEP 2: Parsing Form 20 PDF")
print("=" * 60)

doc1 = fitz.open(FORM20_PDF)
total_pages = len(doc1)
print(f"  Total pages in Form 20: {total_pages}")

# Extract text from each page with word positions
all_page_texts = []
for pg in range(total_pages):
    page = doc1[pg]
    # Use "words" to get precise x,y coordinates
    words = page.get_text("words")  # list of (x0, y0, x1, y1, word, block, line, word_num)
    all_page_texts.append(words)
    text_sample = page.get_text("text")[:300].replace('\n', ' ')
    print(f"  Page {pg+1}: {len(words)} words | Sample: {text_sample[:120]}")

doc1.close()
print(f"\n  Pages loaded successfully.")

# ─── STEP 3: Parse vote rows from Form 20 ───────────────────────────────────
print("\n" + "=" * 60)
print("STEP 3: Parsing vote rows from Form 20")
print("=" * 60)

# Strategy: Re-open and use structured text blocks with blocks
doc1 = fitz.open(FORM20_PDF)
all_rows = []  # list of {booth: int, votes: {candidate_col: int}}

for pg in range(total_pages - 1):  # skip last summary page
    page = doc1[pg]
    
    # Get text as plain with positions grouped by line
    blocks = page.get_text("rawdict", flags=fitz.TEXT_PRESERVE_WHITESPACE)
    
    # Extract all words with their y-coordinates (to group by row)
    words_by_y = defaultdict(list)
    for block in blocks.get('blocks', []):
        if block.get('type') != 0:
            continue
        for line in block.get('lines', []):
            y_center = round((line['bbox'][1] + line['bbox'][3]) / 2, 0)
            y_key = round(y_center / 4) * 4  # bucket into 4px bands
            for span in line.get('spans', []):
                for char_info in [span]:
                    txt = span['text'].strip()
                    if txt:
                        words_by_y[y_key].append((span['bbox'][0], txt))
    
    # Sort each row by x-coordinate
    for y_key in sorted(words_by_y.keys()):
        row_words = sorted(words_by_y[y_key], key=lambda w: w[0])
        row_text = ' '.join(w[1] for w in row_words)
        # Look for rows that start with a booth/station number
        # These rows contain: StationNo | votes per candidate...
        nums = re.findall(r'\d+', row_text)
        if len(nums) >= 5:
            all_rows.append({
                'page': pg + 1,
                'y': y_key,
                'text': row_text,
                'nums': [int(n) for n in nums]
            })

doc1.close()
print(f"  Extracted {len(all_rows)} potential data rows")
# Show sample rows
for r in all_rows[:5]:
    print(f"    P{r['page']} y={r['y']}: {r['text'][:100]}")

# ─── STEP 4: Use direct text extraction per page ─────────────────────────────
print("\n" + "=" * 60)
print("STEP 4: Direct text line extraction from Form 20")
print("=" * 60)

doc1 = fitz.open(FORM20_PDF)
booth_votes = {}  # booth_num -> {jsp, bjp, rjd, tanvir}

for pg in range(total_pages):
    page = doc1[pg]
    text = page.get_text("text")
    lines = text.splitlines()
    print(f"\n--- Page {pg+1} ({len(lines)} lines) ---")
    for i, line in enumerate(lines[:30]):
        print(f"  [{i:03d}] {repr(line)}")

doc1.close()
