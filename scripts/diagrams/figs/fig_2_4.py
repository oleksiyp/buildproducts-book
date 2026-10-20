"""Figure 2.4: the Wardley map of Verified Resale, as Encore's trio placed its components."""
from html import escape

from dg import Diagram
from registry import figure


def _t(d, x, y, text, cls, anchor="start"):
    d.extra.append(f'<text class="{cls}" x="{x}" y="{y}" style="text-anchor:{anchor}">{escape(text)}</text>')


@figure
def fig_2_4():
    d = Diagram("fig-2-4", 864, 648, "Verified Resale on a Wardley map",
                "A Wardley map. The vertical axis is visibility to the fan, from the need at the top through "
                "components the fan sees, those met at the door, those seen by organizers, to those nobody sees; "
                "the horizontal axis is evolution, from genesis through custom and product to commodity. The anchor "
                "is the need: a fan holds a guaranteed ticket. Seen by the fan, in product: listing and storefront "
                "(partners already run good ones; leave them open), checkout with the all-in price (reuse the "
                "primary checkout) and wallet passes (Apple and Google supply them). At the door: rotating "
                "barcodes and gate revocation lists, custom and moving toward product (own them now and watch them "
                "evolve). Seen by organizers: organizer resale rules, between genesis and custom (own them and "
                "expect to learn fast). Unseen: reissue under a new ticket identity, custom and highlighted as "
                "Encore's advantage (own it); buyer screening, custom on rented signals (reuse Bot Screening as "
                "it is); the fee split in the finance ledger, custom on a commodity ledger (extend what exists); "
                "and payments with split payouts, spanning product and commodity (the primary PSP's marketplace "
                "product carries it). The placements are the trio's judgments.")
    X0, X1, Y0, Y1 = 136, 840, 44, 552  # y label sits above the axis
    stages = ["GENESIS", "CUSTOM", "PRODUCT (+RENTAL)", "COMMODITY (+UTILITY)"]
    CW = (X1 - X0) // 4  # 176
    # bands of visibility
    bands = [(44, 100, "THE NEED"), (104, 244, "SEEN BY THE FAN"), (248, 296, "AT THE DOOR"),
             (300, 352, "SEEN BY ORGANIZERS"), (356, 552, "NOBODY SEES")]
    for top, bot, name in bands:
        d.note(124, (top + bot) // 2 + 3, name, anchor="end")
        if top > Y0:
            d.zones.append(f'<line class="dg-grid" x1="{X0}" y1="{top - 2}" x2="{X1}" y2="{top - 2}"/>')
    for k in range(1, 4):
        x = X0 + k * CW
        d.zones.append(f'<line class="dg-ill-soft" x1="{x}" y1="{Y0}" x2="{x}" y2="{Y1}" stroke-dasharray="4 4"/>')
    for k, s in enumerate(stages):
        d.extra.append(f'<text class="dg-tick" x="{X0 + k * CW + CW // 2}" y="{Y1 + 20}" '
                       f'text-anchor="middle">{s}</text>')
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}"/>')
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{Y1}" x2="{X0}" y2="{Y0}"/>')
    d.extra.append(f'<text class="dg-axis-label" x="{X1}" y="{Y1 + 40}" text-anchor="end">EVOLUTION →</text>')
    d.extra.append(f'<text class="dg-axis-label" x="{X0}" y="{Y0 - 16}" text-anchor="start">'
                   '↑ VISIBLE TO THE FAN</text>')
    # the anchor
    d.node(296, 52, 256, 40, "A fan holds a guaranteed ticket", "the need: the anchor of the map", "input")

    def comp(x, y, name, sub, kind="ill-fill", side="right", to=None, left=None):
        if to:  # expected movement along the evolution road
            d.path([(x + 8, y), (to, y)], dashed=True)
        cls = "dg-ill-fill-accent" if kind == "accent" else "dg-ill-fill"
        r = 8 if kind == "accent" else 6
        d.nodes.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{r}"/>')
        lx = (to or x) + 16 if side == "right" else (left or x) - 12
        anchor = "start" if side == "right" else "end"
        mw = int(max(len(name) * 7.0, len(sub) * 5.6)) // 4 * 4 + 8
        d.extra.append(f'<rect class="dg-mask" x="{lx - 4 if side == "right" else lx - mw + 4}" y="{y - 10}" '
                       f'width="{mw}" height="32" rx="2"/>')
        _t(d, lx, y + 4, name, "dg-name", anchor)
        _t(d, lx, y + 17, sub, "dg-sub", anchor)

    comp(520, 124, "Listing and storefront", "partners run good ones; leave open")
    comp(568, 172, "Checkout, all-in price", "reuse the primary checkout")
    comp(616, 220, "Wallet passes", "Apple and Google supply them")
    comp(424, 268, "Rotating barcodes, revocation", "own it now; watch it evolve", to=512)
    comp(264, 324, "Organizer resale rules", "own it, and expect to learn fast", to=352)
    comp(360, 380, "Reissue, new ticket identity", "Encore's advantage: own it", kind="accent")
    comp(400, 428, "Buyer screening", "custom, on rented signals; reuse as is")
    comp(440, 476, "Fee split in the ledger", "custom on a commodity ledger; extend it")
    # payments span product and commodity
    d.zones.append('<line class="dg-ill-ink" x1="624" y1="524" x2="704" y2="524" stroke-width="3"/>')
    comp(664, 524, "Payments, split payouts", "the PSP's marketplace product", side="left", left=624)
    d.legend([("backend", "Component, placed by the trio's judgment"), ("focal", "Encore's advantage"),
              ("arrow:muted:dashed", "Expected movement")])
    return d
