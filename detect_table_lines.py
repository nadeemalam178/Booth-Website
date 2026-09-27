"""
Use RapidOCR + OpenCV on the already-rendered Form 20 PNG images
to extract booth-wise vote data row by row.

Column order from Form 20 (verified visually from page_1_rot270.png):
0:  Serial No of Polling Station
1:  Tanvir Alam (RLJP)
2:  Neeraj Kumar (BJP) 
3:  Rekha Kumari (RJD/INC?)
4:  Ashok Kumar (Samata Party)
5:  Upendra Sahani
6:  Jitendra Dubey
7:  Niranjan Kumar Acharya
8:  Pradeep Kumar (???)  -- CHECK
9:  Prashant Kishor (JSP) -- WINNER
10: Prem Shankar Prasad
11: Binod Ray
12: Manisha Sharma
13: Manoranjan Kumar Shrivastava
14: Suraj Kumar Yadav
15: Mirtunjay Kumar
16: (another candidate)
17: Abhay Choudhary
18: Nitish Kumar
19: Bagish Nandan
20: Baijnath Prasad
21: Rekha Kumari (duplicate?)
22: Prem Shankar
23: Brajesh Patel
24: Sikandar Kumar
25: NOTA
26: Total Valid Votes
27: Rejected Postal
28: Total Polled
29: Tendered Votes

We need col 0 (booth), col 2 (BJP/Neeraj), col 3 (RJD/Rekha), col 9 (JSP/Prashant)
"""
import cv2
import numpy as np
import json
from collections import defaultdict
import re
import os

# Try to use RapidOCR
try:
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    USE_OCR = True
    print("RapidOCR available")
except:
    USE_OCR = False
    print("RapidOCR not available")

IMG_DIR = r"c:\Users\alamn\Downloads\Antigravity"

# Pages 1-7 have booth data (page 8 is summary)
PAGE_IMAGES = [
    os.path.join(IMG_DIR, f"page_{i}_rot270.png")
    for i in range(1, 8)
]

def extract_rows_from_image(img_path, page_num):
    """
    Extract data rows from a Form 20 page image using OpenCV.
    The table has horizontal lines separating rows.
    """
    print(f"\nProcessing {img_path}...")
    img = cv2.imread(img_path)
    if img is None:
        print(f"  ERROR: Could not load image")
        return []
    
    h, w = img.shape[:2]
    print(f"  Image size: {w}x{h}")
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Binarize
    _, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
    
    # Detect horizontal lines to find row boundaries
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (w//6, 1))
    detect_horizontal = cv2.morphologyEx(binary, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    
    # Find contours of horizontal lines
    contours, _ = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get y-coordinates of horizontal lines
    h_lines = []
    for c in contours:
        x, y, cw, ch = cv2.boundingRect(c)
        if cw > w * 0.3:  # significant horizontal line
            h_lines.append(y + ch // 2)
    
    h_lines = sorted(set(h_lines))
    print(f"  Found {len(h_lines)} horizontal lines")
    
    # Detect vertical lines to find column boundaries
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, h//10))
    detect_vertical = cv2.morphologyEx(binary, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
    
    contours_v, _ = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    v_lines = []
    for c in contours_v:
        x, y, cw, ch = cv2.boundingRect(c)
        if ch > h * 0.05:  # significant vertical line
            v_lines.append(x + cw // 2)
    
    v_lines = sorted(set(v_lines))
    print(f"  Found {len(v_lines)} vertical lines")
    
    return h_lines, v_lines, img, gray

# Process one page first to understand structure
if os.path.exists(PAGE_IMAGES[0]):
    result = extract_rows_from_image(PAGE_IMAGES[0], 1)
    if result:
        h_lines, v_lines, img, gray = result
        print(f"\nHorizontal lines (y-coords): {h_lines[:20]}")
        print(f"Vertical lines (x-coords): {v_lines[:15]}")
        
        # Visualize
        debug_img = img.copy()
        for y in h_lines:
            cv2.line(debug_img, (0, y), (img.shape[1], y), (0, 255, 0), 1)
        for x in v_lines:
            cv2.line(debug_img, (x, 0), (x, img.shape[0]), (255, 0, 0), 1)
        
        out_path = os.path.join(IMG_DIR, "debug_lines_p1.png")
        # Save small version
        small = cv2.resize(debug_img, (1200, 900))
        cv2.imwrite(out_path, small)
        print(f"  Saved debug image: {out_path}")
else:
    print(f"Image not found: {PAGE_IMAGES[0]}")
