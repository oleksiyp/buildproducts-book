"""Figure 5.3: one resale at face value, three ways — the buyer's payment and the 10% fee's split."""
from html import escape

from dg import Diagram
from registry import figure

EUR = 4          # px per euro in the payment bar
PT = 24          # px per point of the fee in the enlarged fee bar
BX, ZX = 208, 552  # payment bar and enlarged fee bar


def _seg(d, x, y, w, h, kind, top, bottom, top_cls="dg-sub", bottom_cls="dg-name"):
    d.nodes.append(f'<rect class="dg-n dg-n-{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>')
    cx = x + w // 2
    if top:
        d.extra.append(f'<text class="{top_cls}" x="{cx}" y="{y + 15}">{escape(top)}</text>')
    if bottom:
        d.extra.append(f'<text class="{bottom_cls}" x="{cx}" y="{y + 31}">{escape(bottom)}</text>')


@figure
def fig_5_3():
    d = Diagram("fig-5-3", 864, 416, "One resale, three ways",
                "Three rows, each a €60 ticket resold at its face value, the original price the seller paid with "
                "primary fees included. Left of each row, a bar of what the buyer pays; right, the 10% fee "
                "enlarged and split in points of the resale price. Row one, bought through a partner: the buyer "
                "pays €66.00, the seller receives €60.00, and the €6.00 fee splits into €2.40 for the partner "
                "(four points), €1.80 for the organizer (three) and €1.80 for Encore (three). Row two, bought in "
                "Encore's own app: the buyer pays €66.00, the seller receives €60.00, there is no partner, and "
                "Encore keeps the partner's four points, so the organizer receives €1.80 and Encore €4.20. Row "
                "three, an event designated under Ireland's Sale of Tickets Act, bought through a partner: the "
                "buyer's total is held at the €60 face value, the fee comes out of the seller's proceeds, so the "
                "seller receives €54.00, and the fee splits €2.40, €1.80 and €1.80 as in row one. A dashed line "
                "marks face value, the cap. The seller is paid five days after the event; the split is the same "
                "for every organizer on every tier.")
    d.extra.append(f'<text class="dg-eyebrow" x="{BX}" y="36" style="text-anchor:start">WHAT THE BUYER PAYS</text>')
    d.extra.append(f'<text class="dg-eyebrow" x="{ZX}" y="36" style="text-anchor:start">'
                   'THE 10% FEE, ENLARGED · IN POINTS OF THE RESALE PRICE</text>')
    fv = BX + 60 * EUR
    rows = [
        ("Through a partner", "a partner brings the buyer", 66, 60, False,
         [("PARTNER", "€2.40", 4), ("ORGANIZER", "€1.80", 3), ("ENCORE", "€1.80", 3)]),
        ("In Encore's app", "no partner to pay", 66, 60, False,
         [("ORGANIZER", "€1.80", 3), ("ENCORE · 4 + 3 POINTS", "€4.20", 7)]),
        ("Irish designated event", "through a partner · s.15", 60, 54, True,
         [("PARTNER", "€2.40", 4), ("ORGANIZER", "€1.80", 3), ("ENCORE", "€1.80", 3)]),
    ]
    Y0, STEP, H = 72, 100, 40
    bottom = Y0 + 2 * STEP + H
    # face value: the cap
    d.zones.append(f'<line class="dg-series dg-s-soft" x1="{fv}" y1="56" x2="{fv}" y2="{bottom + 8}" '
                   f'stroke-dasharray="5 4"/>')
    d.label_at("FACE VALUE €60 · THE CAP", fv, 60, horizontal=True, side="above")
    for i, (name, sub, pays, seller, irish, shares) in enumerate(rows):
        y = Y0 + i * STEP
        d.extra.append(f'<text class="dg-name" x="24" y="{y + 18}" style="text-anchor:start">{escape(name)}</text>'
                       f'<text class="dg-sub" x="24" y="{y + 33}" style="text-anchor:start">{escape(sub)}</text>')
        d.note(BX, y - 6, f"BUYER PAYS €{pays:.2f}")
        _seg(d, BX, y, seller * EUR, H, "backend", "SELLER RECEIVES", f"€{seller:.2f}")
        fx = BX + seller * EUR
        d.nodes.append(f'<rect class="dg-n dg-n-{"focal" if irish else "input"}" x="{fx}" y="{y}" '
                       f'width="{6 * EUR}" height="{H}" rx="3"/>')
        # guides from the fee to its enlargement
        for gy in (y, y + H):
            d.zones.append(f'<line class="dg-ill-soft" x1="{fx + 6 * EUR}" y1="{gy}" x2="{ZX}" y2="{gy}" '
                           f'stroke-dasharray="3 3"/>')
        d.label_at("FEE €6.00", (fx + 6 * EUR + ZX) / 2 + 8, y + H / 2 + 6, horizontal=True, side="above")
        x = ZX
        for party, amount, pts in shares:
            _seg(d, x, y, pts * PT, H, "input", party, amount)
            x += pts * PT
        for k in range(1, 10):  # point ticks under the enlarged fee
            d.zones.append(f'<line class="dg-axis" x1="{ZX + k * PT}" y1="{y + H}" x2="{ZX + k * PT}" '
                           f'y2="{y + H + 4}"/>')
        if irish:
            d.note(BX, y + H + 16, "fee taken from the seller's proceeds;")
            d.note(BX, y + H + 29, "the buyer's total stays at face value")
    d.note(ZX, bottom + 24, "seller paid five days after the event;")
    d.note(ZX, bottom + 37, "one split for every organizer, on every tier")
    d.legend([("backend", "Seller's proceeds"), ("input", "The 10% fee and its shares"),
              ("focal", "Fee taken from the seller (Ireland's designated events)")])
    return d
