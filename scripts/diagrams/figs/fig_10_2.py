"""Figure 10.2: one decision through 18 months, the bet memo reread at five checkpoints."""
from dg import Diagram
from registry import figure


@figure
def fig_10_2():
    d = Diagram("fig-10-2", 864, 448, "The memo at five checkpoints",
                "Five checkpoints left to right, each a rereading of the Verified Resale bet memo. "
                "Section 10.1, the bet: month 0, late winter of year 9, revision 0; memo written, first tranche "
                "funds discovery; kill criteria K1 and K2 written; taught in this book's Chapters 1 to 5 and the "
                "Software book's Sections 10.4 and 9.2 to 9.3. Section 10.2, designing it: month 4, late spring, "
                "revision 1; K1 passed; discovery done, decision to build, Resale team formed, 23 dependencies; "
                "this book's Chapters 6 to 9, the Software book's Sections 9.5, 7.3 and 8.2 to 8.3. Section 10.3, "
                "building it: month 9, autumn, revision 2; walking skeleton on the golden path, Rowmate certifying, "
                "14 dependencies; this book's Sections 2.5, 3.1 and 3.4, the Software book's Sections 11.1 to 11.3. "
                "Section 10.4, launching it: month 12, winter of year 10, revision 3; three organizers, Rowmate, "
                "one market (France); this book's Section 4.5 and Chapters 8 and 9, the Software book's Section 11.4. "
                "Section 10.5, what Encore learned: month 18, summer of year 10, the memo's review; K2 not "
                "triggered; Rowmate and Tessera live; this book's Sections 3.1 and 5.5, the Software book's "
                "Section 11.5. A bracket over the first four marks the appetite: 12 months from the memo to "
                "the first resold ticket scanned at a gate.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'VERIFIED RESALE · ONE BET MEMO, REREAD AT FIVE CHECKPOINTS</text>')
    W, GAP, X0, NY, NH = 152, 12, 28, 84, 64
    xs = [X0 + i * (W + GAP) for i in range(5)]
    cols = [
        ("10.1 · MONTH 0", "The bet", "late winter, year 9", "focal", "REVISION 0", "K1, K2 written",
         ["Memo written;", "first tranche funds", "discovery"], ["Chapters 1–5"], ["Sections 10.4, 9.2–9.3"]),
        ("10.2 · MONTH 4", "Designing it", "late spring", "backend", "REVISION 1", "K1 passed",
         ["Discovery done;", "decision to build;", "Resale team formed;", "23 dependencies"],
         ["Chapters 6–9"], ["Sections 9.5, 7.3,", "8.2–8.3"]),
        ("10.3 · MONTH 9", "Building it", "autumn", "backend", "REVISION 2", "",
         ["Walking skeleton on", "the golden path;", "Rowmate certifying;", "14 dependencies"],
         ["Sections 2.5, 3.1, 3.4"], ["Sections 11.1–11.3"]),
        ("10.4 · MONTH 12", "Launching it", "winter, year 10", "backend", "REVISION 3", "",
         ["Three organizers,", "Rowmate, one market", "(France)"], ["Section 4.5,", "Chapters 8–9"], ["Section 11.4"]),
        ("10.5 · MONTH 18", "What Encore learned", "summer, year 10", "focal", "THE REVIEW", "K2 not triggered",
         ["The memo's review;", "Rowmate and Tessera", "live"], ["Sections 3.1, 5.5"], ["Section 11.5"]),
    ]
    # appetite bracket over months 0 to 12
    a, b, by = xs[0] + W // 2, xs[3] + W // 2, 56
    d.zones.append(f'<path class="dg-ill-soft" d="M {a},{by + 8} V {by} H {b} V {by + 8}"/>')
    d.label_at("APPETITE · 12 MONTHS TO THE FIRST RESOLD TICKET SCANNED AT A GATE", (a + b) / 2, by + 4, side="above")
    for x1, x2 in zip(xs, xs[1:]):
        d.path([(x1 + W, NY + NH // 2), (x2, NY + NH // 2)])
    ZY1, ZY2 = 300, 360
    d.zone(20, ZY1, 824, 44, "WHERE THIS BOOK TEACHES IT")
    d.zone(20, ZY2, 824, 44, "WHERE THE SOFTWARE BOOK TELLS IT")
    for x, (tag, name, sub, kind, rev, kill, state, here, sw) in zip(xs, cols):
        d.node(x, NY, W, NH, name, sub, kind, tag=tag)
        # a memo glyph: a page with a folded corner
        gx, gy = x + 8, NY + NH + 16
        d.nodes.append(f'<path class="dg-ill-ink" d="M {gx},{gy} h 12 l 6,6 v 18 h -18 z M {gx + 12},{gy} v 6 h 6"/>'
                       f'<path class="dg-ill-soft" d="M {gx + 4},{gy + 12} h 10 M {gx + 4},{gy + 16} h 10 M {gx + 4},{gy + 20} h 6"/>')
        d.extra.append(f'<text class="dg-label" x="{gx + 28}" y="{gy + 10}" style="text-anchor:start">{rev}</text>')
        if kill:
            d.note(gx + 28, gy + 23, kill)
        for i, t in enumerate(state):
            d.note(x + 8, NY + NH + 72 + 14 * i, t)
        for i, t in enumerate(here):
            d.note(x + 8, ZY1 + 18 + 13 * i, t)
        for i, t in enumerate(sw):
            d.note(x + 8, ZY2 + 18 + 13 * i, t)
    d.legend([("focal", "Where the bet is made and judged"), ("backend", "Checkpoint, by section of this chapter"),
              ("arrow:muted", "Time")])
    return d
