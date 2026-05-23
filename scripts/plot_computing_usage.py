#!/usr/bin/env python3
"""
plot_computing_usage.py
=======================
Generates the ePIC computing-usage as 3 pie charts (one per year).

Usage
-----
    python scripts/plot_computing_usage.py [--output assets/computing_usage.png] [--dpi 150] [--show]

Requirements
------------
    pip install matplotlib numpy
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Data ──────────────────────────────────────────────────────────────────────
YEARS = ['2024', '2025', '2026\n(YTD)']
TOTALS_LABEL = ['14.9M core-hours', '14.0M core-hours', '4.3M core-hours']

DATA = {
    'OSG Opportunistic': [12900, 10700, 2200],
    'JLab':              [942,   2000,  623],
    'Digital Research Alliance Canada': [1000,  864,   438],
    'INFN-T1':           [38,    470,   101],
    'Perlmutter':        [0,     0,     728],
    'BNL SCDF':          [0,     0,     40],
    'HPCC (UManitoba)':  [0,     0,     157],
}

# ── Colors ────────────────────────────────────────────────────────────────────
COLORS = {
    'OSG Opportunistic': '#0072B2',
    'JLab':              '#D55E00',
    'Digital Research Alliance Canada': '#009E73',
    'INFN-T1':           '#CC79A7',
    'Perlmutter':        '#E69F00',
    'BNL SCDF':          '#56B4E9',
    'HPCC (UManitoba)':  '#F0E442',
}


def plot(output='assets/computing_usage.png', dpi=150, show=False):
    sites = list(DATA.keys())
    values = np.array(list(DATA.values()))   # shape: (n_sites, n_years)
    colors = [COLORS[s] for s in sites]

    fig = plt.figure(figsize=(13, 5.5))
    fig.patch.set_facecolor('white')

    # Left: 3 pie charts in a 1x3 grid occupying left 72% of figure
    pie_axes = [fig.add_axes([0.02 + col * 0.23, 0.12, 0.21, 0.78]) for col in range(3)]

    for col, ax in enumerate(pie_axes):
        vals = values[:, col]
        mask = vals > 0
        sliced_vals = vals[mask]
        sliced_colors = [colors[i] for i, m in enumerate(mask) if m]

        wedges, texts, autotexts = ax.pie(
            sliced_vals,
            colors=sliced_colors,
            autopct=lambda p: f'{p:.0f}%' if p > 4 else '',
            pctdistance=0.72,
            startangle=90,
            wedgeprops=dict(linewidth=1.2, edgecolor='white'),
        )
        for at in autotexts:
            at.set_fontsize(12)
            at.set_fontweight('bold')
            at.set_color('white')

        ax.set_title(YEARS[col], fontsize=17, fontweight='bold', color='#1f2933', pad=6)
        ax.text(0, -1.25, TOTALS_LABEL[col], ha='center', va='top',
                fontsize=13, color='#2f6f8f', fontweight='bold')

    # Right: legend-only axis
    leg_ax = fig.add_axes([0.72, 0.05, 0.27, 0.90])
    leg_ax.axis('off')
    handles = [mpatches.Patch(color=COLORS[s], label=s) for s in sites]
    leg_ax.legend(handles=handles, loc='center left',
                  fontsize=15, framealpha=0.95, ncol=1,
                  edgecolor='#ccc', handlelength=1.8, handleheight=1.4,
                  labelspacing=1.1)

    plt.savefig(output, dpi=dpi, bbox_inches='tight')
    print(f"Saved: {output}")
    if show:
        plt.show()
    plt.close()


# ── CLI ───────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot ePIC computing usage')
    parser.add_argument('--output', default='assets/computing_usage.png',
                        help='Output image path (default: assets/computing_usage.png)')
    parser.add_argument('--dpi', type=int, default=150,
                        help='Image DPI (default: 150)')
    parser.add_argument('--show', action='store_true',
                        help='Display the plot interactively')
    args = parser.parse_args()
    plot(output=args.output, dpi=args.dpi, show=args.show)
