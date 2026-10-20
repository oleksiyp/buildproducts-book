"""Figure 4.1: a field arranged by hand against Fisher's randomized blocks (schematic)."""
import random

from dg import Diagram
from registry import figure

COLS, ROWS, CW, RH, GAP = 6, 4, 52, 40, 8


def _field(d, x0, y0, fert, gaps, block_labels):
    """Draw a 6 x 4 field: soft plot outlines, fertilized plots as one accent path, 'F' marks."""
    ys = [y0 + r * (RH + (GAP if gaps else 0)) for r in range(ROWS)]
    # the richer strip: the bottom row of ground, wider than the plots
    d.zones.append(f'<rect class="dg-ill-fill" x="{x0 - 8}" y="{ys[3] - 4}" width="{COLS * CW + 16}" '
                   f'height="{RH + 8}" rx="4" stroke-opacity="0.35"/>')
    acc = []
    for r in range(ROWS):
        for c in range(COLS):
            x, y = x0 + c * CW, ys[r]
            if (r, c) in fert:
                acc.append(f"M {x + 6},{y + 4} h {CW - 12} a 2 2 0 0 1 2 2 v {RH - 12} a 2 2 0 0 1 -2 2 "
                           f"h -{CW - 12} a 2 2 0 0 1 -2 -2 v -{RH - 12} a 2 2 0 0 1 2 -2 z")
                d.extra.append(f'<text class="dg-sub" x="{x + CW // 2}" y="{y + RH // 2 + 3}">F</text>')
            d.nodes.append(f'<rect class="dg-ill-soft" x="{x + 4}" y="{y + 2}" width="{CW - 8}" height="{RH - 4}" rx="3"/>')
    d.nodes.append(f'<path class="dg-ill-fill-accent" d="{" ".join(acc)}"/>')
    # the damp corner: top-left two plots, outlined dashed
    d.extra.append(f'<rect class="dg-ill-ink" x="{x0}" y="{ys[0] - 2}" width="{2 * CW}" height="{RH + 4}" '
                   f'rx="6" stroke-dasharray="3 3"/>')
    for r, lab in enumerate(block_labels):
        if lab:
            d.note(x0 - 72, ys[r] + RH // 2 + 3, lab)
    return ys


@figure
def fig_4_1():
    d = Diagram("fig-4-1", 864, 376, "Two ways to lay out a field trial",
                "A schematic, not a plan of any real Rothamsted trial. The same field is drawn twice as six "
                "columns by four rows of plots, with soil that varies in ways no one could list: a damp corner "
                "at the top left and a richer strip along the bottom. Plots given the fertilizer are marked F. "
                "Left, arranged by the experimenter: the fertilized plots fill the bottom two rows and so sit on "
                "the richer strip, and the fertilizer would be credited for what the soil did. Right, Fisher's "
                "randomized blocks (1926): the field is divided into four blocks of similar ground, and within "
                "each block three of the six plots are given the fertilizer independently and wholly at random. "
                "The random plots fall unevenly, but that unevenness is the kind probability can measure.")
    LX, RX = 48, 500
    d.zone(LX - 24, 40, 360, 280, "ARRANGED BY THE EXPERIMENTER")
    d.zone(416, 40, 424, 280, "RANDOMIZED BLOCKS · FISHER, 1926")
    left = {(r, c) for r in (2, 3) for c in range(COLS)}
    rnd = random.Random(1926)
    right = set()
    for r in range(ROWS):
        for c in rnd.sample(range(COLS), 3):
            right.add((r, c))
    ys = _field(d, LX, 72, left, False, ["", "", "", ""])
    yr = _field(d, RX, 64, right, True, ["BLOCK I", "BLOCK II", "BLOCK III", "BLOCK IV"])
    # annotations under each field
    d.note(LX, ys[3] + RH + 24, "A DAMP CORNER (TOP LEFT) · A RICHER STRIP (BOTTOM)")
    d.note(LX, ys[3] + RH + 40, "The fertilized plots line up with the richer strip:")
    d.note(LX, ys[3] + RH + 54, "the fertilizer is credited for what the soil did.")
    d.note(RX, yr[3] + RH + 24, "Each block is ground of one kind; within it, treatments")
    d.note(RX, yr[3] + RH + 38, "are assigned “independently, and wholly at random”.")
    d.note(RX, yr[3] + RH + 52, "Uneven by chance, but chance can be measured.")
    d.legend([("focal", "Plot given the fertilizer (F)"), ("backend", "Richer ground"),
              ("optional", "A damp corner")])
    return d
