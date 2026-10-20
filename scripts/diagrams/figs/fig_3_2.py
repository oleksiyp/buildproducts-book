"""Figure 3.2: the upper branches of the resale trio's opportunity solution tree, end of month two."""
from html import escape

from dg import Diagram, SUB_CH
from registry import figure

EY_CH = 5.2  # 7px eyebrow, tracked


def _box(d, x, y, w, h, lines, kind, eyebrow=None, dash=False):
    """A card with an optional eyebrow and left-aligned mono lines."""
    assert all(v % 4 == 0 for v in (x, y, w, h)), (lines, x, y, w, h)
    for ln in lines:
        assert len(ln) * SUB_CH <= w - 16, f"line too wide: {ln!r} in {w}px"
    if eyebrow:
        assert len(eyebrow) * EY_CH <= w - 16, f"eyebrow too wide: {eyebrow!r}"
    da = ' stroke-dasharray="4,3"' if dash else ""
    out = [f'<rect class="dg-mask" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>',
           f'<rect class="dg-n dg-n-{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"{da}/>']
    ty = y + 16
    if eyebrow:
        cls = "dg-eyebrow dg-l-accent" if kind == "focal" else "dg-eyebrow"
        out.append(f'<text class="{cls}" x="{x + 8}" y="{ty - 1}" style="text-anchor:start">{escape(eyebrow)}</text>')
        ty += 14
    for ln in lines:
        out.append(f'<text class="dg-sub" x="{x + 8}" y="{ty}" style="text-anchor:start;fill:var(--dg-ink)">{escape(ln)}</text>')
        ty += 12
    d.nodes.append("\n".join(out))


def _h(n_lines, eyebrow=False):
    """Card height, a multiple of 8 so that its middle sits on the 4px grid."""
    base = 12 * n_lines + 12 + (14 if eyebrow else 0)
    return -(-base // 8) * 8


ROWS = [  # eyebrow, opportunity lines, kind, solutions (each a list of lines), test lines
    ("ORGANIZER · 19 OF 22 · ALL SIX PROMOTERS",
     ['"I want to decide when and whether', 'my shows are resold"'], "focal",
     [["rules console: window, per-fan", "limits, off switch"], ["rules set by account managers", "on request"]],
     ["clickable rules screen", "with six promoters"]),
    ("ORGANIZER · 14 OF 22", ['"Touts end up in my front rows"'], "backend",
     [["resale buyers pass Bot Screening"], ["per-buyer limits"]],
     ["count rule breaches in", "the hand-run pilot"]),
    ("ORGANIZER · 8 OF 22", ['"I get nothing when my tickets', 'are resold"'], "backend",
     [["a share of the resale fee"]],
     ["willingness-to-pay", "talks (Chapter 5)"]),
    ("SELLER · 17 OF 31", ['"I\'m afraid of being blamed if', 'the ticket fails"'], "backend",
     [["reissue under a new barcode"], ['"your ticket sold" confirmation']],
     ["hand-run reissue at", "four shows"]),
    ("BUYER · 21 OF 31", ['"I\'m afraid the ticket won\'t', 'open the gate"'], "backend",
     [["Verified badge"], ["guarantee wording"]],
     ["entry refusals in", "the pilot"]),
    ("PARTNER · ALL SIX ROWMATE TALKS", ['"Duplicated tickets cost me', 'chargebacks"'], "external",
     [["reissue, so a ticket exists once"]],
     ["Rowmate's chargeback", "data from Partner", "Listings"]),
]


@figure
def fig_3_2():
    rx, rw = 24, 120
    ox, ow = 172, 248
    sx, sw = 456, 204
    tx, tw = 692, 148
    SG, RG, Y0 = 8, 16, 64
    # lay out rows
    rows, y = [], Y0
    for eb, opp, kind, sols, test in ROWS:
        sh = [_h(len(s)) for s in sols]
        stack = sum(sh) + SG * (len(sols) - 1)
        oh, th = _h(len(opp), True), _h(len(test))
        rh = max(stack, oh, th)
        rows.append((y, rh, sh, stack, oh, th))
        y += rh + RG
    bottom = y - RG
    H = bottom + 72
    d = Diagram("fig-3-2", 864, H, "The resale trio's opportunity solution tree",
                "A tree read from left to right, as it stood at the end of month two. The root is the product "
                "outcome: verified resales completed per eligible event. It branches into six opportunities, each "
                "with whose need it is and how many interviews raised it, out of 22 organizer and 31 fan interviews. "
                "Organizer: 'I want to decide when and whether my shows are resold', raised unprompted in 19 of 22 "
                "and by all six design-partner promoters, the strongest finding; solutions are a rules console with "
                "a window, per-fan limits and an off switch, or rules set by account managers on request; first test "
                "a clickable rules screen with six promoters. Organizer: 'Touts end up in my front rows', 14 of 22; "
                "solutions: resale buyers pass Bot Screening, per-buyer limits; test: count rule breaches in the "
                "hand-run pilot. Organizer: 'I get nothing when my tickets are resold', 8 of 22; solution: a share "
                "of the resale fee; test: willingness-to-pay talks in Chapter 5. Seller: 'I'm afraid of being "
                "blamed if the ticket fails', 17 of 31; solutions: reissue under a new barcode, a 'your ticket sold' "
                "confirmation; test: hand-run reissue at four shows. Buyer: 'I'm afraid the ticket won't open the "
                "gate', 21 of 31; solutions: a Verified badge, guarantee wording; test: entry refusals in the pilot. "
                "Partner, Rowmate, in all six conversations: 'Duplicated tickets cost me chargebacks'; solution: "
                "reissue, so a ticket exists once; test: Rowmate's chargeback data from Partner Listings.")
    for x, label in [(rx, "OUTCOME"), (ox, "OPPORTUNITY · WHOSE · INTERVIEWS"),
                     (sx, "CANDIDATE SOLUTIONS"), (tx, "FIRST ASSUMPTION TEST")]:
        d.extra.append(f'<text class="dg-eyebrow" x="{x}" y="44" style="text-anchor:start">{label}</text>')
    # root
    rh = 108
    ry = (Y0 + bottom) // 2 - rh // 2 // 4 * 4
    ry -= ry % 4
    rmid = ry + rh // 2
    d.nodes.append(f'<rect class="dg-mask" x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="6"/>'
                   f'<rect class="dg-n dg-n-backend" x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="6" stroke-width="1.6"/>')
    d.extra.append(f'<text class="dg-eyebrow" x="{rx + rw // 2}" y="{ry + 22}">PRODUCT OUTCOME</text>')
    for i, ln in enumerate(["Verified resales", "completed per", "eligible event"]):
        d.extra.append(f'<text class="dg-name" x="{rx + rw // 2}" y="{ry + 48 + i * 16}">{ln}</text>')
    jx1, jx2, jx3 = ox - 16, sx - 16, tx - 16
    for (eb, opp, kind, sols, test), (y, rhh, sh, stack, oh, th) in zip(ROWS, rows):
        cy = y + rhh // 2
        cy -= cy % 4
        oy = cy - oh // 2
        omid = oy + oh // 2
        d.path([(rx + rw, rmid), (jx1, rmid), (jx1, omid), (ox, omid)] if omid != rmid else [(rx + rw, rmid), (ox, omid)])
        _box(d, ox, oy, ow, oh, opp, kind, eyebrow=eb)
        sy = cy - stack // 2
        ty = cy - th // 2
        tmid = ty + th // 2
        for s, hgt in zip(sols, sh):
            smid = sy + hgt // 2
            d.path([(ox + ow, omid), (jx2, omid), (jx2, smid), (sx, smid)] if smid != omid else [(ox + ow, omid), (sx, smid)])
            d.path([(sx + sw, smid), (jx3, smid), (jx3, tmid), (tx, tmid)] if smid != tmid else [(sx + sw, smid), (tx, tmid)],
                   arrow=False)
            _box(d, sx, sy, sw, hgt, s, "input")
            sy += hgt + SG
        d.path([(jx3, tmid), (tx, tmid)])
        _box(d, tx, ty, tw, th, test, "optional", dash=True)
    d.legend([("focal", "Strongest finding: control"), ("backend", "Customer opportunity"),
              ("external", "Partner opportunity"), ("input", "Candidate solution"),
              ("optional", "Assumption test")])
    return d
