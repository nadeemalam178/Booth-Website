"""
Full extraction pipeline:
1. Parse booth→ward mapping from PDF 2 (text-based, clean)
2. Use the page PNG images + OCR to extract Form 20 booth-wise votes
3. Aggregate by ward
4. Output JSON for website
"""
import pymupdf
import re
import json
from collections import defaultdict

MAPPING_PDF = r"c:\Users\alamn\Downloads\Antigravity\Booth Wise Team Mapping Bankipur - Cleaned_Data (1).pdf"
FORM20_PDF  = r"c:\Users\alamn\Downloads\Antigravity\Form 20_182-Bankipur Assembly Election.pdf"

# ═══════════════════════════════════════════════════════════
# STEP 1: Parse booth→ward mapping from PDF 2
# ═══════════════════════════════════════════════════════════
print("STEP 1: Parsing booth mapping PDF...")

doc2 = pymupdf.open(MAPPING_PDF)
booth_to_ward = {}   # booth_num (int) -> ward_num (int)
ward_booth_list = defaultdict(list)  # ward -> [booth numbers]

for pg in range(len(doc2)):
    page = doc2[pg]
    text = page.get_text("text")
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    
    # The structure per entry is:
    # Ward No (number)
    # Booth No (number)
    # Station name (multiple lines)
    # Repeated...
    
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip header row
        if line in ('Ward No', 'Booth No', 'Polling_Station_Name'):
            i += 1
            continue
        # Check if this line is a ward number
        if re.match(r'^\d+$', line):
            ward_num = int(line)
            # Next line should be booth number
            if i + 1 < len(lines) and re.match(r'^\d+$', lines[i+1]):
                booth_num = int(lines[i+1])
                booth_to_ward[booth_num] = ward_num
                ward_booth_list[ward_num].append(booth_num)
                i += 2
                continue
        i += 1

doc2.close()

print(f"  Mapped {len(booth_to_ward)} booths across {len(ward_booth_list)} wards")
print(f"  Wards found: {sorted(ward_booth_list.keys())}")
for ward in sorted(ward_booth_list.keys()):
    booths = sorted(ward_booth_list[ward])
    print(f"    Ward {ward}: {len(booths)} booths → {booths[:5]}{'...' if len(booths)>5 else ''}")

# ═══════════════════════════════════════════════════════════
# STEP 2: Parse Form 20 using coordinate-based extraction
# The PDF is a scanned/image PDF but PyMuPDF can still extract
# text if it's embedded (as OCR layer). Let's try with tables.
# ═══════════════════════════════════════════════════════════
print("\nSTEP 2: Parsing Form 20 PDF for booth-wise votes...")

doc1 = pymupdf.open(FORM20_PDF)

# The Form 20 has these candidates in columns (from visual inspection of page images):
# Col order (left to right from the table image):
# SerialNo | TanvirAlam(RLJP) | NeerajKumar(BJP) | RekhKumari(RJD) | AshokKumar |
# UpendraSahani | JitendraDubey | NiranjanAcharya | PradeepKumar(???) | PrashantKishor(JSP) |
# PreshankarPrasad | BinodhRay | ManishaSharmha | ManoranjKumar | SurajKumarYadav |
# MirtunjayKumar | SurajKumarYadav | AbhayChoudhary | NitishKumar | BagishNandan |
# BajinathPrasad | RekhKumari(again?) | PremShankar | BrajeshPatel | SikandarKumar |
# NOTA | Total Valid | Rejected | Total | Tendered

# From the verified internet data:
# Prashant Kishor (JSP) = Winner with 64,151 votes  → appears as "PRASHANT KISHOR" column
# Neeraj Kumar (BJP) = Runner-up with 44,827 votes
# Rekha Kumari (RJD) = 3rd with 14,273 votes

# Let's extract all text rows from each page
all_booth_data = []  # list of dicts

for pg_idx in range(doc1.page_count - 1):  # skip last summary page
    page = doc1[pg_idx]
    
    # Use "words" for positional data
    words = page.get_text("words")  # (x0, y0, x1, y1, text, block, line, word_idx)
    
    if not words:
        print(f"  Page {pg_idx+1}: No text words extracted (pure image page)")
        continue
    
    # Group words by approximate y-position (row)
    rows_by_y = defaultdict(list)
    for (x0, y0, x1, y1, text, block_no, line_no, word_no) in words:
        y_bucket = round(y0 / 5) * 5
        rows_by_y[y_bucket].append((x0, text))
    
    # Sort rows by y, then words by x within row
    row_data = []
    for y in sorted(rows_by_y.keys()):
        row_words = sorted(rows_by_y[y], key=lambda w: w[0])
        row_text = [w[1] for w in row_words]
        # Only keep rows that look like data (start with a number)
        if row_text and re.match(r'^\d+$', row_text[0]):
            row_data.append(row_text)
    
    print(f"  Page {pg_idx+1}: {len(row_data)} data rows found")
    for r in row_data[:3]:
        print(f"    {r[:10]}")

doc1.close()
