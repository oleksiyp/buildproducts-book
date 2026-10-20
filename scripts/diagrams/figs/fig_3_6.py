"""Figure 3.6: the story map for Verified Resale, a backbone of six activities cut into three release slices."""
import textwrap
from html import escape

from dg import Diagram, SUB_CH, NAME_CH
from registry import figure

BACKBONE = [["Organizer", "sets rules"], ["Fan lists", "through a", "partner"], ["Another fan", "buys"],
            ["Ticket is", "reissued"], ["Buyer enters"], ["Money is", "paid out"]]
SLICES = [
    ("FIRST SLICE", [["window and per-fan limits", "face-value cap only"],
                     ["Rowmate only", "one organizer's events"],
                     ["Bot Screening and per-buyer limits"],
                     ["new barcode issued, old one revoked"],
                     ["one venue in Lyon"],
                     ["split recorded", "payouts after the event"]]),
    ("LAUNCH SLICE", [["off switch", "lower cap"],
                      ["Encore's own app as well"],
                      ["all-in price with fee shown up front"],
                      ["wallet pass replaced", '"your ticket sold" message'],
                      ["three organizers' venues in France"],
                      ["organizer share on every tier"]]),
    ("LATER", [["plain-language rule assistant"], ["Tessera"], [], [], ["more markets"], []]),
]


@figure
def fig_3_6():
    X0, CW, G = 104, 116, 8
    WRAP = int((CW - 16) / SUB_CH)
    xs = [X0 + i * (CW + G) for i in range(6)]
    parts = []  # svg chunks, laid out first so the height is known
    nodes, extra, zones = [], [], []
    # backbone
    BY, BH = 56, 64
    for x, lines in zip(xs, BACKBONE):
        for ln in lines:
            assert len(ln) * NAME_CH <= CW - 12, ln
        nodes.append(f'<rect class="dg-n dg-n-backend" x="{x}" y="{BY}" width="{CW}" height="{BH}" rx="6" stroke-width="1.4"/>')
        y0 = BY + BH // 2 - (len(lines) - 1) * 7 + 4
        for i, ln in enumerate(lines):
            extra.append(f'<text class="dg-name" x="{x + CW // 2}" y="{y0 + i * 14}">{escape(ln)}</text>')
    y = BY + BH + 16
    rules = []
    for si, (label, cells) in enumerate(SLICES):
        rules.append((y, label, si == 0))
        top = y + 16
        heights = []
        for x, items in zip(xs, cells):
            cy = top
            for item in items:
                lines = textwrap.wrap(item, WRAP)
                h = 12 * len(lines) + 12
                h += -h % 4
                nodes.append(f'<rect class="dg-n dg-n-input" x="{x}" y="{cy}" width="{CW}" height="{h}" rx="4"/>')
                for i, ln in enumerate(lines):
                    extra.append(f'<text class="dg-sub" x="{x + 8}" y="{cy + 15 + i * 12}" '
                                 f'style="text-anchor:start;fill:var(--dg-ink)">{escape(ln)}</text>')
                cy += h + 8
            if not items:
                extra.append(f'<text class="dg-note" x="{x + CW // 2}" y="{top + 15}" text-anchor="middle">—</text>')
                cy = top + 24 + 8
            heights.append(cy - 8 - top)
        y = top + max(heights) + 16
    H = y + 48
    H += -H % 4
    d = Diagram("fig-3-6", 864, H, "The story map for Verified Resale",
                "A story map. Across the top runs the backbone, six activities in the order the journey happens: "
                "organizer sets rules; fan lists through a partner; another fan buys; ticket is reissued; buyer "
                "enters; money is paid out. Beneath each activity its details sit in three release slices, each a "
                "complete journey. First slice: a resale window and per-fan limits with the face-value cap only; "
                "Rowmate only, for one organizer's events; Bot Screening and per-buyer limits; a new barcode issued "
                "and the old one revoked; one venue in Lyon; the fee split recorded, with payouts after the event. "
                "Launch slice: an off switch and a lower cap; Encore's own app as well; the all-in price with the "
                "fee shown up front; the wallet pass replaced and a 'your ticket sold' message; three organizers' "
                "venues in France; the organizer share on every tier. Later: a plain-language rule assistant; "
                "Tessera; nothing further for buying or reissue; more markets; nothing further for payouts.")
    d.extra.append('<text class="dg-eyebrow" x="104" y="40" style="text-anchor:start">'
                   'BACKBONE · THE JOURNEY, READ LEFT TO RIGHT</text>')
    d.extra.append('<text class="dg-eyebrow" x="24" y="40" style="text-anchor:start">SLICE ↓</text>')
    for ry, label, first in rules:
        cls = "dg-series dg-s-accent" if first else "dg-series dg-s-soft"
        d.zones.append(f'<line class="{cls}" x1="24" y1="{ry}" x2="840" y2="{ry}" stroke-dasharray="5 4"/>')
        tcls = "dg-eyebrow dg-l-accent" if first else "dg-eyebrow"
        d.extra.append(f'<text class="{tcls}" x="24" y="{ry + 26}" style="text-anchor:start">{label}</text>')
    d.zones.extend(zones)
    d.nodes.extend(nodes)
    d.extra.extend(extra)
    d.legend([("backend", "Activity on the backbone"), ("input", "Detail, most essential first"),
              ("arrow:accent:dashed", "First slice: the walking skeleton"), ("arrow:muted:dashed", "Later slices")])
    return d
