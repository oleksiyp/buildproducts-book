"""Figure 6.1: the Palm Beach County butterfly ballot, November 2000: two facing pages, one column of holes."""
from dg import Diagram
from registry import figure


@figure
def fig_6_1():
    d = Diagram("fig-6-1", 864, 484, "The butterfly ballot",
                "A schematic of the presidential page of the Palm Beach County punch-card ballot of 7 November "
                "2000, after the photograph reproduced by Wand et al. (2001). Ten tickets are split across two "
                "facing pages with one column of punch holes down the spine between them. The left page lists, "
                "in order, Bush (Republican), Gore (Democratic), Browne (Libertarian), Nader (Green), Harris "
                "(Socialist Workers) and Hagelin (Natural Law); their arrows point right to holes 3, 5, 7, 9, 11 "
                "and 13. The right page lists Buchanan (Reform), McReynolds (Socialist), Phillips (Constitution) "
                "and Moorehead (Workers World), whose arrows point left to holes 4, 6, 8 and 10, followed by a "
                "write-in box; position 12, beside it, has no arrow. The holes alternate between the pages. "
                "Gore is the second name on "
                "the left, but the second hole, number 4, is Buchanan's; Gore's is the third, number 5. A voter "
                "who counted down the left page and punched the second hole voted for Buchanan.")
    Y0, P, BH = 72, 48, 40           # first box top, ticket pitch, box height
    SX = 432                         # spine centre
    LX, RX, BW = 40, 512, 312        # box lefts and width
    hole_y = lambda k: Y0 + BH // 2 + (k - 3) * (P // 2)  # noqa: E731

    # the two pages and the spine
    d.zone(24, 48, 368, 324, "LEFT PAGE")
    d.zone(472, 48, 368, 324, "RIGHT PAGE")
    d.zones.append(f'<rect class="dg-ill-soft" x="{SX - 16}" y="{Y0 - 8}" width="32" height="{hole_y(13) - Y0 + 32}" rx="4"/>')
    d.note(SX, Y0 - 16, "HOLES", anchor="middle")

    left = [("George W. Bush", "REPUBLICAN"), ("Al Gore", "DEMOCRATIC"), ("Harry Browne", "LIBERTARIAN"),
            ("Ralph Nader", "GREEN"), ("James Harris", "SOCIALIST WORKERS"), ("John Hagelin", "NATURAL LAW")]
    right = [("Pat Buchanan", "REFORM"), ("David McReynolds", "SOCIALIST"), ("Howard Phillips", "CONSTITUTION"),
             ("Monica Moorehead", "WORKERS WORLD")]

    for i, (name, party) in enumerate(left):
        y, k = Y0 + i * P, 3 + 2 * i
        d.path([(LX + BW, hole_y(k)), (SX - 10, hole_y(k))], label=f"#{k}")
        d.node(LX, y, BW, BH, name, party, "focal" if name == "Al Gore" else "backend")
    for j, (name, party) in enumerate(right):
        y, k = Y0 + P // 2 + j * P, 4 + 2 * j
        d.path([(RX, hole_y(k)), (SX + 10, hole_y(k))], label=f"#{k}")
        d.node(RX, y, BW, BH, name, party, "backend")
    d.node(RX, Y0 + P // 2 + 4 * P, BW, BH, "Write-in candidate", "NO ARROW", "optional")

    for k in range(3, 14):
        cls = "dg-ill-fill-accent" if k == 4 else "dg-ill-soft" if k == 12 else "dg-ill-fill"
        d.nodes.append(f'<circle class="{cls}" cx="{SX}" cy="{hole_y(k)}" r="{7 if k == 4 else 6}"/>')

    d.note(24, 400, "READ DOWN THE LEFT PAGE: BUSH IS THE 1ST NAME AND HAS THE 1ST HOLE (#3).")
    d.note(24, 416, "GORE IS THE 2ND NAME, BUT THE 2ND HOLE (#4) IS BUCHANAN'S. GORE'S IS THE 3RD (#5).")
    d.note(24, 432, "THE ARROWS ARE CORRECT; THE READING ORDER CONTRADICTS THEM.")
    d.note(840, 432, "SCHEMATIC, AFTER WAND ET AL. 2001, FIG. 1", anchor="end")
    d.legend([("backend", "Ticket, arrow to its hole"), ("focal", "Gore: 2nd name, 3rd hole"),
              ("optional", "Write-in, no hole")])
    return d
