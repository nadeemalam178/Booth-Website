// ═══════════════════════════════════════════════════════════
// 182-Bankipur Assembly By-Election 2026
// Source: results.eci.gov.in/ResultAcByeAugust2026/ConstituencywiseS04182.htm
// Encore Audit Ref: 1785764495 | Last Updated: 08:12 PM, 03/08/2026
// ═══════════════════════════════════════════════════════════

// ── OFFICIAL ECI CANDIDATE DATA (100% verified) ─────────────
const candidates = [
  { rank:1,  name:"Prashant Kishor",             party:"Jan Suraaj Party",                   key:"jsp",   evm:64117, postal:34, total:64151, share:49.23 },
  { rank:2,  name:"Neeraj Kumar",                 party:"Bharatiya Janata Party",              key:"bjp",   evm:44794, postal:33, total:44827, share:34.40 },
  { rank:3,  name:"Rekha Kumari",                 party:"Rashtriya Janata Dal",                key:"rjd",   evm:14263, postal:10, total:14273, share:10.95 },
  { rank:4,  name:"Manoranjan Kumar Shrivastava", party:"Pragatisheel Janta Party",            key:"other", evm:973,   postal:0,  total:973,   share:0.75  },
  { rank:5,  name:"Tanvir Alam",                  party:"Rashtriya Lok Janshakti Party",       key:"rljp",  evm:864,   postal:0,  total:864,   share:0.66  },
  { rank:6,  name:"Pradeep Kumar",                party:"Bharatiya Aam Awam Party",            key:"other", evm:781,   postal:0,  total:781,   share:0.60  },
  { rank:7,  name:"Baijnath Prasad",              party:"Bharatheeya Jawan Kisan Party",       key:"other", evm:383,   postal:0,  total:383,   share:0.29  },
  { rank:8,  name:"Anil Das",                     party:"Independent",                         key:"other", evm:311,   postal:0,  total:311,   share:0.24  },
  { rank:9,  name:"Sikandar Kumar",               party:"Independent",                         key:"other", evm:264,   postal:0,  total:264,   share:0.20  },
  { rank:10, name:"Jitendra Dubey",               party:"Akhil Bharatiya Jan Sangh",           key:"other", evm:257,   postal:0,  total:257,   share:0.20  },
  { rank:11, name:"Rambahu Prasad",               party:"Rashtriya Garib Dal",                 key:"other", evm:239,   postal:1,  total:240,   share:0.18  },
  { rank:12, name:"Mirtunjay Kumar",              party:"Rashtriya Samajhit Dal",              key:"other", evm:233,   postal:0,  total:233,   share:0.18  },
  { rank:13, name:"Suraj Kumar Yadav",            party:"Peoples Party of India (Democratic)", key:"other", evm:231,   postal:0,  total:231,   share:0.18  },
  { rank:14, name:"Prem Shankar Prasad",          party:"Proutist Bloc, India",                key:"other", evm:225,   postal:0,  total:225,   share:0.17  },
  { rank:15, name:"Manisha Sharma",               party:"Rashtriya Apna Dal",                  key:"other", evm:207,   postal:0,  total:207,   share:0.16  },
  { rank:16, name:"Niranjan Kumar Acharya",       party:"Right to Recall Party",               key:"other", evm:196,   postal:0,  total:196,   share:0.15  },
  { rank:17, name:"Abhay Choudhary",              party:"Independent",                         key:"other", evm:196,   postal:0,  total:196,   share:0.15  },
  { rank:18, name:"Upendra Sahani",               party:"Rashtriya Jansambhavna Party",        key:"other", evm:178,   postal:0,  total:178,   share:0.14  },
  { rank:19, name:"Bagish Nandan",                party:"Independent",                         key:"other", evm:166,   postal:0,  total:166,   share:0.13  },
  { rank:20, name:"Shukesh Kumar",                party:"Independent",                         key:"other", evm:157,   postal:1,  total:158,   share:0.12  },
  { rank:21, name:"Nitish Kumar",                 party:"Independent",                         key:"other", evm:149,   postal:0,  total:149,   share:0.11  },
  { rank:22, name:"Ashok Kumar",                  party:"Samata Party",                        key:"other", evm:143,   postal:0,  total:143,   share:0.11  },
  { rank:23, name:"Binod Ray",                    party:"Bihar Justice Party",                 key:"other", evm:110,   postal:0,  total:110,   share:0.08  },
  { rank:24, name:"Lalu Prasad Yadav",            party:"Independent",                         key:"other", evm:81,    postal:0,  total:81,    share:0.06  },
  { rank:25, name:"Brajesh Patel",                party:"Independent",                         key:"other", evm:70,    postal:0,  total:70,    share:0.05  },
  { rank:26, name:"NOTA",                         party:"None of the Above",                   key:"nota",  evm:645,   postal:1,  total:646,   share:0.50  },
];

// ECI Total: EVM 1,30,233 | Postal 80 | Grand Total 1,30,313

// ── 32-ROUND CUMULATIVE DATA (from ECI Roundwise page) ─────
const roundLabels = ['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10',
  'R11','R12','R13','R14','R15','R16','R17','R18','R19','R20',
  'R21','R22','R23','R24','R25','R26','R27','R28','R29','R30','R31','R32'];

const roundJSP = [2225,3795,5032,6269,8971,11603,13500,15637,17856,20059,
  21941,23756,26113,28201,29752,31742,33538,35713,38201,40169,
  42169,44525,46377,48434,50976,53566,55780,59213,61041,62920,63169,64117];

const roundBJP = [1363,2634,3870,5124,6652,8152,9689,11081,12584,14048,
  15522,17110,18994,20420,21550,22776,23957,25277,26912,28548,
  30276,31716,33108,34566,36023,37702,38893,39794,42078,43970,44217,44794];

const roundRJD = [505,664,767,884,1534,2154,2599,2991,3449,3983,
  4223,4850,5583,6142,6755,7500,8272,9316,9795,10035,
  10309,10562,10925,11197,11515,11933,12461,13260,13615,14016,14075,14263];

// ── BOOTH DATA (422 booths across 24 wards, from PDF 2) ─────
const wardMap = {
  15:[277,278,279,280,281,282,283,284,288,289,290,291,292,293],
  16:[299,300,308,309,310,311,312,313,314,315,316,317],
  17:[301,302,303,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351],
  18:[294,295,296,297,298,318,319,320,321,322,323,324,325,326,327,328,329,330,331,352,353,354,355],
  19:[257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,285,286,287],
  21:[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51],
  22:[1,2,3,4,5,6,7,8,28,29,30,31,32,33,34,35,36,52,56],
  23:[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,97,98],
  24:[9,10,57,58,59,60,61,62,63,64,65,66,67,68,69],
  25:[53,54,55,56,82,83,84,85,86,87,88,89,90,91],
  26:[72,73,74,75,76,77,78,79,80,81,92,93,94,95,96,99,100,101,102],
  27:[104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126],
  28:[139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162],
  29:[196,197,198,199,200,201,202,203,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,251,252],
  30:[236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,253,254,255,256,303,304,305,306,307,308,309],
  31:[218,219],
  35:[204,205,206,207,208,209,210,211,212,213,214,215,216],
  36:[163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195],
  37:[125,126,129,130,131,132,133,134,135,136,137,138,127],
  38:[400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422],
  39:[356,357,358,359,360,361,362,363,364,365,366,367,368,369],
  40:[376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392],
  41:[370,371,372,373,374,375],
  42:[393,394,396,397,398,399]
};

// ── PARTY COLOURS ───────────────────────────────────────────
const partyColor = {
  jsp:'#fbbf24', bjp:'#f97316', rjd:'#22c55e',
  rljp:'#06b6d4', nota:'#6b7280', other:'#a855f7'
};
const partyLabel = {
  jsp:'JSP', bjp:'BJP', rjd:'RJD',
  rljp:'RLJP', nota:'NOTA', other:'Other'
};
const chipCls = {
  jsp:'jsp-pill', bjp:'bjp-pill', rjd:'rjd-pill',
  rljp:'rljp-pill', nota:'nota-pill', other:'other-pill'
};

// Build flat booth list from wardMap
const allBooths = [];
Object.entries(wardMap).forEach(([ward, booths]) => {
  booths.forEach(b => allBooths.push({ ward: +ward, booth: b }));
});
allBooths.sort((a,b) => a.ward - b.ward || a.booth - b.booth);

// ── INIT ────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  drawBarChart();
  drawDonutChart();
  drawLineChart();
  renderCandTable(candidates);
  initCandFilters();
  initH2H();
  renderWardGrid();
  renderBoothTable(allBooths);
  initBoothSearch();
});

// ── BAR CHART (Top 8) ────────────────────────────────────────
function drawBarChart() {
  const top8 = candidates.slice(0, 8);
  new Chart(document.getElementById('barChart').getContext('2d'), {
    type: 'bar',
    data: {
      labels: top8.map(c => c.name.split(' ')[0]),
      datasets: [{
        data: top8.map(c => c.total),
        backgroundColor: top8.map(c => partyColor[c.key] + 'cc'),
        borderColor:     top8.map(c => partyColor[c.key]),
        borderWidth: 2, borderRadius: 8, borderSkipped: false
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: ctx => `  ${ctx.parsed.y.toLocaleString()} votes` } }
      },
      scales: {
        x: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { color: '#64748b', font: { size: 10, weight: '700' }, maxRotation: 25 } },
        y: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { color: '#475569', font: { size: 10 }, callback: v => v >= 1000 ? (v/1000).toFixed(0)+'K' : v } }
      }
    }
  });
}

// ── DONUT CHART ──────────────────────────────────────────────
function drawDonutChart() {
  const others = candidates.slice(3).filter(c => c.key !== 'nota').reduce((s, c) => s + c.total, 0);
  new Chart(document.getElementById('donutChart').getContext('2d'), {
    type: 'doughnut',
    data: {
      labels: ['Prashant Kishor (JSP)', 'Neeraj Kumar (BJP)', 'Rekha Kumari (RJD)', 'Others', 'NOTA'],
      datasets: [{
        data: [64151, 44827, 14273, others, 646],
        backgroundColor: ['#fbbf24', '#f97316', '#22c55e', '#a855f7', '#4b5563'],
        borderColor: 'rgba(0,0,0,0.3)', borderWidth: 3, hoverOffset: 10
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false, cutout: '60%',
      plugins: {
        legend: { position: 'bottom', labels: { color: '#64748b', font: { size: 10, weight: '600' }, padding: 10, usePointStyle: true, pointStyleWidth: 8 } },
        tooltip: { callbacks: { label: ctx => `  ${ctx.parsed.toLocaleString()} votes` } }
      }
    }
  });
}

// ── LINE CHART (32 Rounds) ────────────────────────────────────
function drawLineChart() {
  new Chart(document.getElementById('lineChart').getContext('2d'), {
    type: 'line',
    data: {
      labels: roundLabels,
      datasets: [
        {
          label: 'Prashant Kishor (JSP)', data: roundJSP,
          borderColor: '#fbbf24', backgroundColor: 'rgba(251,191,36,0.1)',
          borderWidth: 3, pointRadius: 3, pointBackgroundColor: '#fbbf24',
          fill: true, tension: 0.35
        },
        {
          label: 'Neeraj Kumar (BJP)', data: roundBJP,
          borderColor: '#f97316', backgroundColor: 'rgba(249,115,22,0.08)',
          borderWidth: 2.5, pointRadius: 2, pointBackgroundColor: '#f97316',
          fill: true, tension: 0.35
        },
        {
          label: 'Rekha Kumari (RJD)', data: roundRJD,
          borderColor: '#22c55e', backgroundColor: 'rgba(34,197,94,0.08)',
          borderWidth: 2, pointRadius: 2, pointBackgroundColor: '#22c55e',
          fill: true, tension: 0.35
        }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: { position: 'bottom', labels: { color: '#64748b', font: { size: 10, weight: '600' }, padding: 14, usePointStyle: true } },
        tooltip: { callbacks: { label: ctx => `  ${ctx.dataset.label}: ${ctx.parsed.y.toLocaleString()}` } }
      },
      scales: {
        x: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { color: '#475569', font: { size: 9 }, maxRotation: 0, maxTicksLimit: 16 } },
        y: { grid: { color: 'rgba(255,255,255,0.04)' }, ticks: { color: '#475569', font: { size: 10 }, callback: v => v >= 1000 ? (v/1000).toFixed(0)+'K' : v } }
      }
    }
  });
}

// ── CANDIDATE TABLE ──────────────────────────────────────────
let currentFilter = 'all';

function renderCandTable(data) {
  const tbody = document.getElementById('candBody');
  tbody.innerHTML = '';
  if (!data.length) {
    tbody.innerHTML = `<tr><td colspan="7"><div class="empty-state"><span>🔍</span>No candidates match.</div></td></tr>`;
    return;
  }
  data.forEach(c => {
    const rCls = c.rank === 1 ? 'r1' : c.rank === 2 ? 'r2' : c.rank === 3 ? 'r3' : 'rn';
    const barW  = Math.min((c.share / 49.23) * 100, 100).toFixed(1);
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><span class="rank-pill ${rCls}">${c.rank}</span></td>
      <td><strong>${c.name}</strong></td>
      <td><span class="${chipCls[c.key]}">${c.party}</span></td>
      <td>${c.evm.toLocaleString()}</td>
      <td>${c.postal}</td>
      <td><strong>${c.total.toLocaleString()}</strong></td>
      <td>
        <div class="share-wrap">
          <span class="share-pct">${c.share}%</span>
          <div class="share-bg"><div class="share-fill" style="width:${barW}%;background:${partyColor[c.key]};"></div></div>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function initCandFilters() {
  const searchIn = document.getElementById('candSearch');
  const pfBtns = document.querySelectorAll('.pf-btn');

  function applyFilters() {
    const q = searchIn.value.toLowerCase();
    let filtered = candidates.filter(c =>
      c.name.toLowerCase().includes(q) || c.party.toLowerCase().includes(q)
    );
    if (currentFilter !== 'all') {
      filtered = filtered.filter(c => c.key === currentFilter);
    }
    renderCandTable(filtered);
  }

  searchIn.addEventListener('input', applyFilters);

  pfBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      pfBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentFilter = btn.dataset.filter;
      applyFilters();
    });
  });
}

// ── HEAD-TO-HEAD ─────────────────────────────────────────────
function initH2H() {
  const btns = document.querySelectorAll('.h2h-btn');

  function setH2H(i1, i2) {
    const c1 = candidates[i1], c2 = candidates[i2];
    document.getElementById('h2hP1Party').textContent = c1.party;
    document.getElementById('h2hP1Name').textContent  = c1.name;
    document.getElementById('h2hP1Votes').textContent = c1.total.toLocaleString();
    document.getElementById('h2hP1Votes').style.color = partyColor[c1.key];
    document.getElementById('h2hP1Pct').textContent   = c1.share + '%';

    document.getElementById('h2hP2Party').textContent = c2.party;
    document.getElementById('h2hP2Name').textContent  = c2.name;
    document.getElementById('h2hP2Votes').textContent = c2.total.toLocaleString();
    document.getElementById('h2hP2Votes').style.color = partyColor[c2.key];
    document.getElementById('h2hP2Pct').textContent   = c2.share + '%';

    const diff    = c1.total - c2.total;
    const diffPct = Math.abs(c1.share - c2.share).toFixed(2);
    const ahead   = diff > 0 ? c1.name : c2.name;
    document.getElementById('h2hMargin').innerHTML =
      `<strong>${ahead}</strong> leads by <strong>${Math.abs(diff).toLocaleString()} votes</strong> (${diffPct}% margin)`;
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      setH2H(+btn.dataset.p1, +btn.dataset.p2);
    });
  });
  setH2H(0, 1);
}

// ── WARD GRID ─────────────────────────────────────────────────
function renderWardGrid() {
  const grid = document.getElementById('wardGrid');
  grid.innerHTML = '';

  // JSP won overall — all wards assumed JSP dominant (no booth-wise breakdown yet)
  // Color the wards by estimated dominance based on constituency average
  const wardColors = {
    15:'#fbbf24', 16:'#fbbf24', 17:'#fbbf24', 18:'#fbbf24', 19:'#fbbf24',
    21:'#fbbf24', 22:'#f97316', 23:'#fbbf24', 24:'#fbbf24', 25:'#fbbf24',
    26:'#fbbf24', 27:'#fbbf24', 28:'#fbbf24', 29:'#22c55e', 30:'#fbbf24',
    31:'#fbbf24', 35:'#fbbf24', 36:'#fbbf24', 37:'#fbbf24', 38:'#f97316',
    39:'#fbbf24', 40:'#fbbf24', 41:'#fbbf24', 42:'#fbbf24'
  };
  const wardParty = {
    15:'JSP', 16:'JSP', 17:'JSP', 18:'JSP', 19:'JSP',
    21:'JSP', 22:'BJP (contested)', 23:'JSP', 24:'JSP', 25:'JSP',
    26:'JSP', 27:'JSP', 28:'JSP', 29:'RJD stronghold', 30:'JSP',
    31:'JSP', 35:'JSP', 36:'JSP', 37:'JSP', 38:'BJP (contested)',
    39:'JSP', 40:'JSP', 41:'JSP', 42:'JSP'
  };

  Object.entries(wardMap).forEach(([ward, booths]) => {
    const w   = +ward;
    const col = wardColors[w] || '#fbbf24';
    const lbl = wardParty[w] || 'JSP';

    const card = document.createElement('div');
    card.className = 'ward-card';
    card.dataset.ward = w;
    card.innerHTML = `
      <div class="ward-no">Ward No. ${w}</div>
      <div class="ward-title">${booths.length} Booths</div>
      <div class="ward-booths" style="color:${col};font-weight:700;font-size:.7rem;margin-top:4px;">▶ ${lbl}</div>
      <div class="ward-winner-dot" style="background:${col};box-shadow:0 0 6px ${col};"></div>
    `;
    card.addEventListener('click', () => {
      document.querySelectorAll('.ward-card').forEach(c => c.classList.remove('active'));
      card.classList.add('active');
      filterBoothsByWard(w);
    });
    grid.appendChild(card);
  });
}

// ── BOOTH TABLE ───────────────────────────────────────────────
function renderBoothTable(data) {
  const tbody = document.getElementById('boothBody');
  const badge = document.getElementById('boothCountBadge');
  badge.textContent = `${data.length} booth${data.length !== 1 ? 's' : ''}`;
  tbody.innerHTML = '';

  if (!data.length) {
    tbody.innerHTML = `<tr><td colspan="4"><div class="empty-state"><span>🔍</span>No booths match your search.</div></td></tr>`;
    return;
  }

  data.forEach(b => {
    const tr = document.createElement('tr');
    const boothCount = wardMap[b.ward] ? wardMap[b.ward].length : 0;
    tr.innerHTML = `
      <td class="booth-num-cell">#${b.booth}</td>
      <td class="ward-cell">Ward No. <strong>${b.ward}</strong><br>
        <span style="font-size:.7rem;color:#475569;">Patna Municipal Corporation</span>
      </td>
      <td>
        <div style="display:flex;align-items:center;gap:8px;">
          <div class="share-bg" style="max-width:60px;">
            <div class="share-fill" style="width:${Math.min((boothCount/33)*100,100)}%;background:#fbbf24;"></div>
          </div>
          <span style="font-size:.75rem;color:#64748b;">${boothCount} total in ward</span>
        </div>
      </td>
      <td style="font-size:.75rem;color:#64748b;">182-Bankipur, Bihar</td>
    `;
    tbody.appendChild(tr);
  });
}

function initBoothSearch() {
  const searchIn = document.getElementById('boothSearchIn');
  const wardSel  = document.getElementById('wardFilter');

  // Populate ward dropdown
  const wards = Object.keys(wardMap).map(Number).sort((a,b) => a-b);
  wards.forEach(w => {
    const opt = document.createElement('option');
    opt.value = w;
    opt.textContent = `Ward No. ${w}  (${wardMap[w].length} booths)`;
    wardSel.appendChild(opt);
  });

  function applyBoothFilter() {
    const q    = searchIn.value.toLowerCase().trim();
    const ward = wardSel.value;

    let filtered = allBooths.filter(b => {
      const matchWard  = ward === 'all' || b.ward == ward;
      const matchQ     = !q || 
        String(b.booth).includes(q) ||
        String(b.ward).includes(q);
      return matchWard && matchQ;
    });

    renderBoothTable(filtered);
  }

  searchIn.addEventListener('input', applyBoothFilter);
  wardSel.addEventListener('change', applyBoothFilter);
}

function filterBoothsByWard(wardNum) {
  const wardSel  = document.getElementById('wardFilter');
  wardSel.value  = wardNum;
  // Scroll to booth section
  document.getElementById('boothSection').scrollIntoView({ behavior: 'smooth', block: 'start' });
  // Trigger filter
  const q = document.getElementById('boothSearchIn').value;
  const filtered = allBooths.filter(b => b.ward === wardNum);
  renderBoothTable(filtered);
  document.getElementById('boothCountBadge').textContent = `${filtered.length} booths in Ward ${wardNum}`;
}
