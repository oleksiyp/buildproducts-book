"""Figure 3.1: Intuit's Follow Me Home, a timeline from 1983 to 2017 and the visit in four steps (schematic)."""
from html import escape

from dg import Diagram
from registry import figure


def _x(year):
    """1983-1993 on a linear scale; 2017 after a break in the axis."""
    return 776 if year >= 2017 else round(48 + (year - 1983) * 59.2)


@figure
def fig_3_1():
    d = Diagram("fig-3-1", 864, 400, "Follow Me Home",
                "A schematic in two parts. Above, a timeline with a break between 1993 and 2017. 1983: Scott Cook "
                "and Tom Proulx found Intuit. 1984: Quicken ships, sold through banks first, starting with Bank of "
                "Hawaii. A bracket over Quicken's early days marks the years in which Cook started the home visits. "
                "September 1988: Quicken is the best-selling consumer software product. 1989: Intuit reinstates the "
                "Follow Me Home program. 1992: QuickBooks is released and passes the market leader, DacEasy, within "
                "two months. 2017: Fortune reports some 10,000 hours of visits a year, hours and not visits. Below, "
                "the visit in four steps: an Intuit employee waits beside the Quicken shelf until someone buys a "
                "copy; asks to follow the buyer home; watches the first installation without interviewing, because "
                "the struggle is the data; and debriefs at once. The layout of a visit is not documented; the "
                "drawing is schematic.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'INTUIT, 1983–2017 · DATES FROM INTUIT\'S 2006 PRESS KIT AND FORTUNE (2017)</text>')
    AX = 152
    # the early-days bracket
    x0, x1 = _x(1984), _x(1989)
    d.zones.append(f'<path class="dg-ill-soft" d="M {x0},{AX - 72} V {AX - 80} H {x1} V {AX - 72}" stroke-dasharray="4 3"/>')
    d.label_at("QUICKEN'S EARLY DAYS · COOK STARTS THE VISITS", (x0 + x1) / 2, AX - 66, side="above")
    # axis with a break
    d.zones.append(f'<line class="dg-ill-ink" x1="40" y1="{AX}" x2="{_x(1993)}" y2="{AX}"/>'
                   f'<line class="dg-ill-ink" x1="{_x(1993) + 32}" y1="{AX}" x2="824" y2="{AX}"/>')
    bx = _x(1993) + 16
    d.zones.append(f'<path class="dg-ill-soft" d="M {bx - 8},{AX + 6} L {bx - 2},{AX - 6} M {bx + 2},{AX + 6} L {bx + 8},{AX - 6}"/>')
    events = [  # year, label year, lines, above?, anchor, kind
        (1983, "1983", ["Cook and Proulx", "found Intuit"], True, "start", "ink"),
        (1984, "1984", ["Quicken ships; sold", "through banks first"], False, "start", "ink"),
        (1988.7, "SEP 1988", ["Quicken is the best-", "selling consumer software"], True, "middle", "ink"),
        (1989, "1989", ["Follow Me Home", "reinstated"], False, "middle", "accent"),
        (1992, "1992", ["QuickBooks; passes", "DacEasy in two months"], True, "middle", "ink"),
        (2017, "2017", ["~10,000 hours of visits", "a year (hours, not visits)"], False, "end", "ink"),
    ]
    for year, ylab, lines, above, anchor, kind in events:
        x = _x(year)
        tx = x if anchor != "end" else x + 48
        if anchor == "start":
            tx = x - 4
        if above:
            d.zones.append(f'<line class="dg-ill-soft" x1="{x}" y1="{AX - 12}" x2="{x}" y2="{AX}"/>')
            ys = (AX - 48, AX - 34, AX - 21)
        else:
            d.zones.append(f'<line class="dg-ill-soft" x1="{x}" y1="{AX}" x2="{x}" y2="{AX + 12}"/>')
            ys = (AX + 28, AX + 42, AX + 55)
        dot = "dg-dot dg-dot-accent" if kind == "accent" else "dg-ill-fill"
        d.nodes.append(f'<circle class="{dot}" cx="{x}" cy="{AX}" r="{5 if kind == "accent" else 4}"/>')
        ycls = "dg-name" + (' dg-l-accent' if kind == "accent" else "")
        d.extra.append(f'<text class="{ycls}" x="{tx}" y="{ys[0]}" style="text-anchor:{anchor}">{escape(ylab)}</text>')
        for yy, line in zip(ys[1:], lines):
            d.extra.append(f'<text class="dg-note" x="{tx}" y="{yy}" text-anchor="{anchor}">{escape(line)}</text>')
    # the visit, in four steps
    d.extra.append('<text class="dg-eyebrow" x="24" y="244" style="text-anchor:start">'
                   'ONE VISIT · SCHEMATIC, AFTER FORTUNE (2017)</text>')
    W, H, Y = 180, 64, 264
    xs = [24, 236, 448, 660]
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, Y + 32), (b, Y + 32)])
    steps = [
        ("1 · THE STORE", "Wait at the shelf", "until someone buys Quicken", "backend"),
        ("2 · THE ASK", "Ask to follow", "the buyer home", "backend"),
        ("3 · THE HOME", "Watch the install", "don't interview; just observe", "focal"),
        ("4 · THE DEBRIEF", "Debrief at once", "observers compare notes", "backend"),
    ]
    for x, (tag, name, sub, kind) in zip(xs, steps):
        d.node(x, Y, W, H, name, sub, kind, tag=tag)
    d.note(538, Y + H + 18, "the struggle is the data", anchor="middle")
    d.legend([("backend", "Step of the visit"), ("focal", "The rule: observe, don't interview"),
              ("arrow:muted", "Order of the visit")])
    return d
