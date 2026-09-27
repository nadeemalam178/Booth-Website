"""
Extract booth-wise vote data from Form 20 page images using RapidOCR.
The Form 20 table has booth number in col 0, and vote columns for each candidate.
From visual inspection of page_1_rot270.png, the table columns are:
Col 0: Serial/Booth No
Col 1: Tanvir Alam (RLJP)
Col 2: Neeraj Kumar (BJP)  
Col 3: Rekha Kumari (RJD)
...
Col 8: Prashant Kishor (JSP)  <-- Winner
...
Col 24: NOTA
Col 25: Total Valid Votes
Col 26: Rejected
Col 27: Total Polled

Strategy: OCR each page, group text by y-coordinate into rows,
then by x-coordinate into columns. Use known totals to validate.
"""
import cv2
import numpy as np
import json
import re
import os
from collections import defaultdict
from rapidocr_onnxruntime import RapidOCR

ocr = RapidOCR()
IMG_DIR = r"c:\Users\alamn\Downloads\Antigravity"

# Process all 7 data pages (page 8 is summary)
page_images = [os.path.join(IMG_DIR, f"page_{i}_rot270.png") for i in range(1, 8)]

# Known column count from Form 20: 29 columns total
# We need col 0 (booth), col 2 (BJP), col 3 (RJD), col 8 (JSP), col 25 (Total)
# But col indices may shift - we'll detect by looking at header row first

def extract_table_from_image(img_path, page_num):
    """Extract table data using RapidOCR"""
    img = cv2.imread(img_path)
    if img is None:
        print(f"Could not load {img_path}")
        return []
    
    h, w = img.shape[:2]
    print(f"\nPage {page_num}: {w}x{h}")
    
    result, _ = ocr(img)
    if not result:
        print(f"  No OCR results")
        return []
    
    print(f"  Got {len(result)} text regions")
    
    # Collect all text with center positions
    items = []
    for item in result:
        box  = item[0]  # [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
        text = item[1].strip()
        conf = item[2]
        
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        cx = sum(xs) / 4
        cy = sum(ys) / 4
        
        # Only keep items that look like numbers or short text
        items.append({'text': text, 'x': cx, 'y': cy, 'conf': conf})
    
    # Group into rows by y-coordinate (within 8px bands)
    rows_by_y = defaultdict(list)
    for item in items:
        y_bucket = round(item['y'] / 8) * 8
        rows_by_y[y_bucket].append(item)
    
    # Sort rows by y, items within row by x
    sorted_rows = []
    for y in sorted(rows_by_y.keys()):
        row_items = sorted(rows_by_y[y], key=lambda i: i['x'])
        row_vals  = [i['text'] for i in row_items]
        row_xs    = [i['x']    for i in row_items]
        sorted_rows.append({'y': y, 'vals': row_vals, 'xs': row_xs})
    
    # Find data rows: rows where first element is a 1-3 digit number (booth no)
    data_rows = []
    for row in sorted_rows:
        if not row['vals']:
            continue
        first = row['vals'][0]
        # Clean common OCR errors for numbers
        first_clean = re.sub(r'[oO]', '0', first).strip()
        first_clean = re.sub(r'[lI]', '1', first_clean).strip()
        if re.match(r'^\d{1,3}$', first_clean):
            data_rows.append({
                'booth': int(first_clean),
                'vals': row['vals'],
                'xs': row['xs'],
                'y': row['y']
            })
    
    print(f"  Found {len(data_rows)} data rows")
    
    return data_rows, sorted_rows

# Process page 1 to understand structure
all_pages_data = {}
for i, img_path in enumerate(page_images):
    if not os.path.exists(img_path):
        print(f"Missing: {img_path}")
        continue
    result = extract_table_from_image(img_path, i+1)
    if result:
        data_rows, all_rows = result
        all_pages_data[i+1] = {'data': data_rows, 'all': all_rows}
        
        # Print first few data rows
        for r in data_rows[:5]:
            print(f"  Booth {r['booth']}: {r['vals'][:10]}")

# Now figure out column layout from page 1
if 1 in all_pages_data:
    print("\n\n=== COLUMN ANALYSIS (Page 1) ===")
    data = all_pages_data[1]['data']
    if data:
        # Look at x-positions of first row to understand column layout
        first_row = data[0]
        print(f"First data row booth {first_row['booth']}:")
        for j, (v, x) in enumerate(zip(first_row['vals'], first_row['xs'])):
            print(f"  Col {j:2d}: x={x:6.1f}  '{v}'")
