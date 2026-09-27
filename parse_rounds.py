"""Parse all 32 rounds from ECI roundwise page and ward mapping"""
import re
import json
from collections import defaultdict

# Read the roundwise file
with open(r"C:\Users\alamn\.gemini\antigravity-ide\brain\b5728cd1-ee7d-4e2c-8140-ebb5506fe19d\.system_generated\steps\371\content.md", 'r', encoding='utf-8') as f:
    html = f.read()

# Extract all round tables
# Pattern: Round N (EVM Votes)...rows...Total = X
round_data = {}

# Find each round block
round_blocks = re.findall(r'Round (\d+) \(EVM Votes\)(.*?)(?=Round \d+|$)', html, re.DOTALL)

for rnum, block in round_blocks:
    rnum = int(rnum)
    # Extract rows: candidate, party, prev, current, total
    rows = re.findall(r"<td align='left'>([^<]+)</td><td align='left'>([^<]+)</td><td>(\d+)</td><td>(\d+)</td><td>(\d+)</td>", block)
    total_match = re.search(r"<th>(\d+)</th>\s*</tr></tfoot>", block)
    
    candidates_in_round = {}
    for cand, party, prev, curr, tot in rows:
        candidates_in_round[cand.strip()] = {
            'prev': int(prev), 'current': int(curr), 'total': int(tot)
        }
    
    if total_match:
        round_total = int(total_match.group(1))
    else:
        round_total = sum(v['total'] for v in candidates_in_round.values())
    
    round_data[rnum] = {
        'candidates': candidates_in_round,
        'total': round_total
    }

print(f"Parsed {len(round_data)} rounds")

# Extract Prashant Kishor (JSP), Neeraj Kumar (BJP), Rekha Kumari (RJD) per round
key_candidates = ['PRASHANT KISHOR', 'NEERAJ KUMAR', 'REKHA KUMARI']

round_progression = {}
for rnum in sorted(round_data.keys()):
    rd = round_data[rnum]
    round_progression[rnum] = {
        'total_evm': rd['total'],
        'jsp': rd['candidates'].get('PRASHANT KISHOR', {}).get('total', 0),
        'bjp': rd['candidates'].get('NEERAJ KUMAR', {}).get('total', 0),
        'rjd': rd['candidates'].get('REKHA KUMARI', {}).get('total', 0),
    }

print("\nRound-by-round progression (JSP, BJP, RJD):")
for r, d in round_progression.items():
    print(f"  R{r:2d}: Total={d['total_evm']:6d} | JSP={d['jsp']:6d} | BJP={d['bjp']:6d} | RJD={d['rjd']:6d}")

# Save as JSON
out = {
    'rounds': round_progression,
    'round_labels': [f"R{i}" for i in sorted(round_progression.keys())],
    'jsp_cumulative': [round_progression[r]['jsp'] for r in sorted(round_progression.keys())],
    'bjp_cumulative': [round_progression[r]['bjp'] for r in sorted(round_progression.keys())],
    'rjd_cumulative': [round_progression[r]['rjd'] for r in sorted(round_progression.keys())],
    'total_cumulative': [round_progression[r]['total_evm'] for r in sorted(round_progression.keys())],
}

with open(r"c:\Users\alamn\Downloads\Antigravity\round_data.json", 'w') as f:
    json.dump(out, f, indent=2)

print("\nSaved round_data.json")
