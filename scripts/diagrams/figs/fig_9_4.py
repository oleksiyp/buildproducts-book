"""Figure 9.4: the reissue operation, its three stages and the moment it stops being cancellable."""
from html import escape

from dg import Diagram, label_width
from registry import figure


@figure
def fig_9_4():
    d = Diagram("fig-9-4", 864, 532, "The reissue operation",
                "When a listing sells, the order's response names a reissue operation, which passes through "
                "three stages: revoke, in which the seller's barcode is revoked and joins the revocation lists "
                "venue scanners hold for offline validation; issue, in which a new ticket identity and barcode "
                "are issued to the buyer; and deliver, in which the new ticket reaches the buyer's app and any "
                "wallet pass is updated. A failed stage is retried by Encore and reported as such. Most reissues "
                "finish in under 30 seconds and 99 percent within four minutes; listings close two hours before "
                "doors. The operation is cancellable only until the first stage completes; after that, reversing "
                "a reissue needs two people's approval at Encore. Below, what a partner reads from the operation: "
                "its current stage, the cancellable flag, a done flag, and a result or an error once finished; "
                "and the events reissue.completed or reissue.failed. Operations are kept for 30 days.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'ONE RESALE · THE OPERATION THE ORDER NAMES</text>')
    Y, H, W = 128, 72, 168
    xs = [184, 384, 584]
    # timing bracket over the three stages
    bx0, bx1, by = xs[0], xs[2] + W, 64
    d.zones.append(f'<path class="dg-ill-soft" d="M {bx0},{by + 8} V {by} H {bx1} V {by + 8}"/>')
    d.label_at("MOST UNDER 30 S · 99% WITHIN 4 MIN", (bx0 + bx1) / 2, by, horizontal=True, side="above")
    # connectors
    d.path([(152, Y + 36), (xs[0], Y + 36)])
    d.path([(xs[0] + W, Y + 36), (xs[1], Y + 36)])
    d.path([(xs[1] + W, Y + 36), (xs[2], Y + 36)])
    d.path([(xs[2] + W, Y + 36), (792, Y + 36)])
    d.end(808, Y + 36)
    d.note(808, Y + 20, "DONE", anchor="middle")
    # retry loop on a failed stage (shown on deliver)
    d.path([(xs[2] + 128, Y), (xs[2] + 128, 104), (xs[2] + 40, 104), (xs[2] + 40, Y)], dashed=True,
           label="FAILED STAGE · RETRY", at=1, side="above", arrow=True)
    d.node(24, Y + 8, 128, 56, "Order created", "names the operation", "input")
    stages = [("STAGE 1", "Revoke", "seller's barcode", ["joins the revocation lists", "gates hold offline"]),
              ("STAGE 2", "Issue", "new ticket identity", ["new barcode, to the buyer"]),
              ("STAGE 3", "Deliver", "to the buyer's app", ["wallet pass updated, if any"])]
    for x, (tag, name, sub, notes) in zip(xs, stages):
        d.node(x, Y, W, H, name, sub, "backend", tag=tag)
        for i, n in enumerate(notes):
            d.note(x + 4, Y + H + 20 + i * 14, n)
    # cancellable strip
    sy = 248
    d.zones.append(f'<rect class="dg-n dg-n-input" x="{xs[0]}" y="{sy}" width="{376 - xs[0]}" height="24" rx="4"/>')
    d.zones.append(f'<rect class="dg-n dg-n-optional" x="384" y="{sy}" width="{xs[2] + W - 384}" height="24" '
                   f'rx="4" stroke-dasharray="4,3"/>')
    d.extra.append(f'<text class="dg-sub" x="{(xs[0] + 376) // 2}" y="{sy + 15}">cancellable: true</text>')
    d.extra.append(f'<text class="dg-sub" x="{(384 + xs[2] + W) // 2}" y="{sy + 15}">'
                   f'cancellable: false · reversal needs two approvals at Encore</text>')
    # the turn: first stage done
    d.nodes.append(f'<line class="dg-ill-accent" x1="376" y1="{Y - 8}" x2="376" y2="{sy + 36}" '
                   f'stroke-dasharray="5 4"/>')
    d.label_at("FIRST STAGE DONE", 376, sy + 36, horizontal=True, side="below", kind="accent")
    # what the partner reads
    cy = 320
    d.zone(24, cy, 320, 100, "WHAT THE PARTNER READS")
    card = ["operations/rei_51Vd", "  stage:        revoke | issue | deliver",
            "  cancellable:  true, until stage 1 is done", "  done:         false while in progress",
            "  result | error, once done"]
    for i, line in enumerate(card):
        d.extra.append(f'<text class="dg-note" x="40" y="{cy + 24 + i * 15}" xml:space="preserve">'
                       f'{escape(line)}</text>')
    # events to the partner
    d.path([(808, Y + 44), (808, 372), (712, 372)], kind="link",
           label="EVENTS", at=0, side="right")
    d.node(552, 344, 160, 56, "Partner", "e.g. Rowmate", "external")
    d.path([(552, 372), (344, 372)], kind="link", label="READS THE OPERATION", side="above")
    notes = ["The partner tells its buyer \"your ticket is being issued\" honestly;",
             "a failed stage with its retry reads \"delayed\", not \"lost\""]
    for i, n in enumerate(notes):
        d.note(24, 444 + i * 14, n)
    d.note(552, 420, "reissue.completed | reissue.failed")
    d.note(24, 476, "Listings close 2 h before doors, so the slowest reissue ends long before the turnstile. "
                    "Operations are kept 30 days.")
    d.legend([("input", "Order"), ("backend", "Stage of the operation"), ("external", "Partner"),
              ("arrow:link", "What reaches the partner"), ("arrow:muted:dashed", "Retry")])
    return d
