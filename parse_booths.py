"""
Build booth_data.json using the correct column positions.
Ward col: x ~ 57, Booth col: x ~ 203
Station name column has Hindi text - we'll use pre-defined English names from what we know
"""
import pymupdf, re, json
from collections import defaultdict

MAPPING_PDF = r"c:\Users\alamn\Downloads\Antigravity\Booth Wise Team Mapping Bankipur - Cleaned_Data (1).pdf"
doc = pymupdf.open(MAPPING_PDF)

booths = []
ward_map = defaultdict(list)

for pg in range(len(doc)):
    page = doc[pg]
    words = page.get_text("words")
    if not words:
        continue
    
    # Group by y-position
    rows_by_y = defaultdict(list)
    for (x0, y0, x1, y1, text, blk, line, wnum) in words:
        y_key = round(y0 / 12) * 12
        rows_by_y[y_key].append((x0, text))
    
    for y in sorted(rows_by_y.keys()):
        row_words = sorted(rows_by_y[y], key=lambda w: w[0])
        
        # Ward col: x < 100, Booth col: 150 < x < 280
        ward_words  = [w[1] for w in row_words if w[0] < 100]
        booth_words = [w[1] for w in row_words if 150 < w[0] < 280]
        
        ward_str  = ' '.join(ward_words).strip()
        booth_str = ' '.join(booth_words).strip()
        
        if re.match(r'^\d+$', ward_str) and re.match(r'^\d+$', booth_str):
            ward_num  = int(ward_str)
            booth_num = int(booth_str)
            # Skip header-like values
            if 1 <= ward_num <= 60 and 1 <= booth_num <= 500:
                booths.append({'ward': ward_num, 'booth': booth_num})
                ward_map[ward_num].append(booth_num)

doc.close()

# Remove duplicates while preserving order
seen = set()
unique_booths = []
for b in booths:
    key = (b['ward'], b['booth'])
    if key not in seen:
        seen.add(key)
        unique_booths.append(b)

unique_booths.sort(key=lambda x: (x['ward'], x['booth']))
print(f"Total unique booths: {len(unique_booths)}")
print(f"Wards: {sorted(set(b['ward'] for b in unique_booths))}")

# Save
out = {
    'booths': unique_booths,
    'ward_map': {},
    'total': len(unique_booths),
    'wards': sorted(set(b['ward'] for b in unique_booths))
}
for b in unique_booths:
    w = str(b['ward'])
    if w not in out['ward_map']:
        out['ward_map'][w] = []
    out['ward_map'][w].append(b['booth'])

with open(r"c:\Users\alamn\Downloads\Antigravity\booth_data.json", 'w') as f:
    json.dump(out, f, indent=2)
print("Saved!")
# Sample
for b in unique_booths[:5]:
    print(b)
