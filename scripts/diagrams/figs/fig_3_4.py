"""Figure 3.4: Encore's Wizard of Oz, what fans saw and what four Support agents did behind it."""
from dg import Diagram, label_width
from registry import figure


@figure
def fig_3_4():
    d = Diagram("fig-3-4", 864, 448, "Encore's Wizard of Oz",
                "Two lanes. In front of the curtain everything a fan touched was real, at four shows in Lyon and "
                "Antwerp: the seller lists through 'Resell this ticket' in My Tickets; the buyer, screened by Bot "
                "Screening and the per-buyer limits as in a primary sale, pays face value plus a 10% fee, shown in "
                "the all-in price, and the payment is only authorized; it is captured only after the reissue; the "
                "buyer then enters with the new barcode. Behind the curtain a rota of four Support agents did the "
                "work for each sale: check that the seller bought through the Sale Gate within the per-fan limit; "
                "check the promoter's rules, resale closing 24 hours before doors and two tickets per fan; cancel "
                "the seller's ticket and issue a new one with Support's old lost-ticket replacement screen; and "
                "confirm the old ticket is on the show's revocation list. If no reissue is done within 12 hours, the "
                "authorization lapses and the listing returns. Sellers were paid by hand after the show.")
    W, H = 180, 60
    xs = [24, 236, 448, 660]
    TY, BY = 112, 276
    d.zone(16, 56, 832, 136, "IN FRONT · REAL SCREENS, REAL MONEY, REAL GATES · FOUR SHOWS")
    # the lower zone's label sits between the two arrows that cross its top edge
    lab = "BEHIND THE CURTAIN · A ROTA OF FOUR SUPPORT AGENTS, BY HAND"
    lw = label_width(lab)
    d.zones.append(f'<rect class="dg-zone" x="16" y="252" width="832" height="92" rx="8"/>'
                   f'<rect class="dg-mask" x="240" y="246" width="{lw}" height="12" rx="2"/>'
                   f'<text class="dg-eyebrow" x="{240 + lw / 2:g}" y="255">{lab}</text>')
    # connectors first
    d.path([(xs[0] + W, TY + 32), (xs[1], TY + 32)])
    d.path([(xs[2] + W, TY + 32), (xs[3], TY + 32)])
    d.path([(xs[1] + W // 2, TY), (xs[1] + W // 2, 80), (xs[0] + W // 2, 80), (xs[0] + W // 2, TY)],
           dashed=True, label="NO REISSUE IN 12 H: LISTING RETURNS", side="below")
    d.path([(xs[1] + W // 2, TY + H), (xs[1] + W // 2, 224), (xs[0] + W // 2, 224), (xs[0] + W // 2, BY)],
           label="SALE AUTHORIZED", at=1)
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, BY + 32), (b, BY + 32)])
    d.path([(xs[3] + W // 2, BY), (xs[3] + W // 2, 224), (xs[2] + W // 2, 224), (xs[2] + W // 2, TY + H)],
           label="REISSUE CONFIRMED", at=1)
    top = [
        ("Seller lists", "My Tickets: Resell this ticket", "backend", None),
        ("Buyer screened, pays", "face value + 10%, authorized", "backend", None),
        ("Payment captured", "only after the reissue", "focal", None),
        ("Buyer enters", "new barcode at the gate", "backend", None),
    ]
    for x, (name, sub, kind, tag) in zip(xs, top):
        d.node(x, TY, W, H, name, sub, kind)
    bottom = [
        ("Check the seller", "bought via Sale Gate, in limit", "backend"),
        ("Check promoter rules", "24 h before doors · 2 per fan", "backend"),
        ("Cancel and reissue", "old lost-ticket screen", "focal"),
        ("Confirm revocation", "old ticket on the show's list", "backend"),
    ]
    for x, (name, sub, kind) in zip(xs, bottom):
        d.node(x, BY, W, H, name, sub, kind)
    d.note(24, 368, "The barcode core had no notion of transfer, so a careful person with an old admin screen did "
                    "the reissue.")
    d.note(24, 382, "Sellers were paid by hand after the show.")
    d.legend([("backend", "Step"), ("focal", "The two safeguards: capture after reissue, reissue by hand"),
              ("arrow:muted", "Flow of one resale"), ("arrow:muted:dashed", "Timeout")])
    return d
