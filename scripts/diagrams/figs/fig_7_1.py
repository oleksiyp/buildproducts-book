"""Figure 7.1: the subway's signs from the 1904 tablets to the 2014 reissue, drawn as a route with stations."""
from html import escape

from dg import Diagram
from registry import figure

R = 8


@figure
def fig_7_1():
    d = Diagram("fig-7-1", 864, 424, "The subway's signs, 1904 to 2014",
                "A schematic timeline, not to scale, drawn as a subway route with one station per event, in two "
                "rows. First row, three systems with one name and a standard built twice: 1904, the IRT's ceramic "
                "mosaic tablets, with no common typeface, arrows or borders; 1940, the IRT, BMT and IND unified "
                "under city ownership but still signed three ways; 1966, the Transit Authority engages Unimark and "
                "Bob Noorda studies how passengers move; November 1967, the Chrystie Street Connection joins IND and "
                "BMT services and the confusion becomes a public complaint; before 1968, the Authority's Bergen "
                "Street sign shop builds signs from Unimark's proposal with no instruction and no inspection, the "
                "result Vignelli called the biggest mess in the world; 1968, Unimark is rehired; 1970, the Graphics "
                "Standards Manual is issued, with Standard Medium type, the black band and modular panels in "
                "one-foot units. Second row, two decades of drift, then an owner and a migration: around 1973 the "
                "signs switch to white on black against graffiti; through the 1970s fiscal crisis the standard is "
                "applied piecemeal; 1979, Paul Goldberger in the New York Times judges the signs confusing; "
                "December 1989, the MTA makes Helvetica its official typeface and hires Michael Hertz Associates "
                "to update the manual; the 1990s capital programs make the stations coherent. Afterlife: 2012, a "
                "copy is found in the basement of Pentagram's New York office; 2014, the reissue's Kickstarter "
                "raises $802,812 from about 6,700 backers. The 1970 manual and the 1989 owner are highlighted; "
                "the route between them is dashed, for the piecemeal years.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="24" style="text-anchor:start">'
                   'NEW YORK SUBWAY SIGNS · SCHEMATIC TIMELINE, STATIONS NOT TO SCALE</text>')
    XS = [80 + 116 * i for i in range(7)]          # 80 … 776
    L1, L2 = 96, 284                               # the two route lines
    row1 = [
        ("1904", ["IRT mosaic", "tablets: no", "common type,", "arrows or borders"], "backend"),
        ("1940", ["IRT, BMT and IND", "unified; still", "signed three ways"], "backend"),
        ("1966", ["TA engages", "Unimark; Noorda", "studies passengers"], "backend"),
        ("Nov 1967", ["Chrystie Street", "joins IND and BMT;", "public complaint"], "backend"),
        ("Bergen St", ["shop builds from", "the proposal: no", "instruction or", "inspection"], "backend"),
        ("1968", ["Unimark", "rehired"], "backend"),
        ("1970", ["Graphics Standards", "Manual issued:", "Standard Medium,", "black band, 1-ft", "panels"], "focal"),
    ]
    row2 = [
        ("c. 1973", ["white on black,", "against graffiti"], "backend"),
        ("1970s", ["fiscal crisis:", "standard applied", "piecemeal"], "backend"),
        ("1979", ["Goldberger, in", "the NYT, judges", "signs confusing"], "backend"),
        ("Dec 1989", ["MTA: Helvetica", "official; Hertz", "Associates update", "the manual"], "focal"),
        ("1990s", ["capital programs", "make stations", "coherent"], "backend"),
        ("2012", ["copy found in", "Pentagram's", "basement"], "backend"),
        ("2014", ["reissue on", "Kickstarter:", "$802,812, about", "6,700 backers"], "backend"),
    ]
    # phase zones
    d.zone(24, 48, 456, 164, "THREE SYSTEMS, ONE NAME")
    d.zone(488, 48, 352, 164, "A STANDARD, BUILT TWICE")
    d.zone(24, 236, 340, 136, "TWO DECADES OF DRIFT")
    d.zone(372, 236, 228, 136, "AN OWNER, A MIGRATION")
    d.zone(608, 236, 232, 136, "AFTERLIFE")
    # the route: solid to 1970, dashed through the drift to 1989, solid after
    route = ' style="stroke-width:3"'
    d.zones.append(f'<path class="dg-ill-ink"{route} d="M {XS[0]},{L1} L {XS[6]},{L1}"/>')
    wrap = (f"M {XS[6]},{L1} L {848 - R},{L1} Q 848,{L1} 848,{L1 + R} L 848,{224 - R} Q 848,224 {848 - R},224 "
            f"L {16 + R},224 Q 16,224 16,{224 + R} L 16,{L2 - R} Q 16,{L2} {16 + R},{L2} L {XS[3]},{L2}")
    d.zones.append(f'<path class="dg-ill-soft"{route} stroke-dasharray="6 5" d="{wrap}"/>')
    d.zones.append(f'<path class="dg-ill-ink"{route} d="M {XS[3]},{L2} L {XS[6]},{L2}"/>')
    for rowy, row in ((L1, row1), (L2, row2)):
        for x, (year, lines, kind) in zip(XS, row):
            d.extra.append(f'<text class="dg-name" x="{x}" y="{rowy - 16}">{escape(year)}</text>')
            cls = "dg-ill-fill-accent" if kind == "focal" else "dg-ill-fill"
            d.nodes.append(f'<circle class="{cls}" cx="{x}" cy="{rowy}" r="{8 if kind == "focal" else 6}"/>')
            for i, ln in enumerate(lines):
                d.note(x, rowy + 24 + 13 * i, ln, anchor="middle")
    d.legend([("backend", "Event"), ("focal", "The standard issued; the owner hired to keep it"),
              ("arrow:muted:dashed", "Piecemeal years")])
    return d
