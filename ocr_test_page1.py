"""
Use RapidOCR on Form 20 page images to extract all numbers with positions.
Then reconstruct the table by grouping numbers into rows by y-coordinate
and columns by x-coordinate.
"""
import cv2
import numpy as np
import json
from collections import defaultdict
import re
import os

from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()

IMG_DIR = r"c:\Users\alamn\Downloads\Antigravity"

# Process page 1 first as a test
def ocr_page(img_path):
    img = cv2.imread(img_path)
    if img is None:
        return []
    
    result, elapse = ocr(img)
    if not result:
        return []
    
    items = []
    for item in result:
        box = item[0]   # [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
        text = item[1]  # recognized text
        conf = item[2]  # confidence
        
        # Get center of bounding box
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        cx = sum(xs) / 4
        cy = sum(ys) / 4
        
        items.append({
            'text': text.strip(),
            'x': cx,
            'y': cy,
            'conf': conf
        })
    
    return items

# Test on page 1
print("Testing OCR on page 1...")
items = ocr_page(os.path.join(IMG_DIR, "page_1_rot270.png"))
print(f"Found {len(items)} text regions")

# Show all items sorted by y then x
items_sorted = sorted(items, key=lambda i: (round(i['y']/10)*10, i['x']))
for it in items_sorted[:80]:
    print(f"  y={it['y']:6.0f} x={it['x']:6.0f}  '{it['text']}'  conf={it['conf']:.2f}")
