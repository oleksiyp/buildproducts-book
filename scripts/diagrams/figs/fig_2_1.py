"""Figure 2.1: Jobs's four-quadrant grid at Apple, 1997, and how it was filled (schematic)."""
from html import escape

from dg import Diagram
from registry import figure


def _t(d, x, y, text, cls, anchor="middle"):
    d.extra.append(f'<text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anchor}">{escape(text)}</text>')


@figure
def fig_2_1():
    d = Diagram("fig-2-1", 864, 440, "Apple's four-quadrant grid",
                "Schematic of the whiteboard grid Steve Jobs drew at an Apple product strategy session in 1997, "
                "as Walter Isaacson describes it: one horizontal and one vertical line, the columns headed "
                "Consumer and Pro, the rows labelled Desktop and Portable. The quadrants show the product that "
                "filled each: consumer desktop, the iMac, announced May 1998 and shipped August 1998; pro desktop, "
                "the Power Macintosh G3, announced November 1997; pro portable, the PowerBook G3; consumer "
                "portable, the iBook, unveiled at Macworld New York on 21 July 1999 at $1,599, highlighted because "
                "the slot stayed empty for more than a year. A timeline at the right lists the events in order: "
                "September 1997, Jobs becomes interim chief executive; November 1997, Power Macintosh G3 announced; "
                "May 1998, iMac announced, and TidBITS describes the four-slot strategy with the consumer portable "
                "slot empty; August 1998, iMac ships; July 1999, iBook unveiled and the grid is full. A highlighted "
                "bar marks the empty slot from the TidBITS report to the iBook. Notes give the results: a loss of "
                "about $1.05 billion in fiscal 1997 and a profit of $309 million on $5.94 billion of revenue in "
                "fiscal 1998. The layout of the whiteboard is schematic; only its lines and four words are documented.")
    # the whiteboard
    d.zones.append('<rect class="dg-ill-fill" x="24" y="40" width="520" height="352" rx="6"/>')
    d.extra.append('<text class="dg-eyebrow" x="44" y="64" style="text-anchor:start">'
                   'THE WHITEBOARD, 1997 · SCHEMATIC</text>')
    # the consumer portable slot, empty until July 1999 (accent 1)
    d.zones.append('<rect class="dg-ill-fill-accent" x="156" y="256" width="168" height="108" rx="4"/>')
    # two marker lines
    d.zones.append('<line class="dg-ill-ink" x1="336" y1="88" x2="336" y2="376" stroke-width="2.4"/>')
    d.zones.append('<line class="dg-ill-ink" x1="56" y1="244" x2="528" y2="244" stroke-width="2.4"/>')
    _t(d, 240, 104, "Consumer", "dg-name")
    _t(d, 432, 104, "Pro", "dg-name")
    _t(d, 96, 182, "Desktop", "dg-name")
    _t(d, 96, 314, "Portable", "dg-name")
    # quadrants
    _t(d, 240, 168, "iMac", "dg-name")
    _t(d, 240, 186, "announced May 1998", "dg-sub")
    _t(d, 240, 200, "shipped August 1998", "dg-sub")
    _t(d, 432, 174, "Power Macintosh G3", "dg-name")
    _t(d, 432, 192, "announced November 1997", "dg-sub")
    _t(d, 432, 314, "PowerBook G3", "dg-name")
    _t(d, 240, 296, "iBook", "dg-name")
    _t(d, 240, 314, "unveiled 21 July 1999", "dg-sub")
    _t(d, 240, 328, "Macworld New York · $1,599", "dg-sub")
    _t(d, 240, 350, "EMPTY FOR MORE THAN A YEAR", "dg-label")
    # timeline of how the grid was filled
    TX = 616
    d.extra.append(f'<text class="dg-eyebrow" x="{TX - 24}" y="52" style="text-anchor:start">'
                   'HOW THE GRID WAS FILLED</text>')
    d.zones.append(f'<line class="dg-ill-soft" x1="{TX}" y1="72" x2="{TX}" y2="312"/>')
    events = [(80, "Sep 1997", ["Jobs becomes interim CEO"]),
              (136, "Nov 1997", ["Power Macintosh G3 announced"]),
              (192, "May 1998", ["iMac announced; TidBITS reports", "the consumer portable slot empty"]),
              (248, "Aug 1998", ["iMac ships"]),
              (304, "Jul 1999", ["iBook unveiled: the grid is full"])]
    # the empty slot, from the TidBITS report to the iBook (accent 2)
    d.zones.append(f'<line class="dg-ill-accent" x1="{TX - 16}" y1="192" x2="{TX - 16}" y2="304" stroke-width="3"/>')
    for y, date, lines in events:
        d.nodes.append(f'<circle class="dg-ill-fill" cx="{TX}" cy="{y}" r="5"/>')
        _t(d, TX + 16, y + 4, date, "dg-name", "start")
        for i, line in enumerate(lines):
            d.note(TX + 16, y + 19 + 13 * i, line)
    d.note(TX - 24, 356, "FY1997: a loss of about $1.05 billion")
    d.note(TX - 24, 372, "FY1998: $309 million profit on $5.94 billion")
    d.legend([("backend", "Quadrant filled by a product"),
              ("focal", "Consumer portable: empty until the iBook")])
    return d
