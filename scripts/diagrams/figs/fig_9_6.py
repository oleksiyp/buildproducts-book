"""Figure 9.6: Encore's default webhook retry schedule, and what the partner sees at each step."""
from html import escape

from dg import Diagram, label_width
from registry import figure


@figure
def fig_9_6():
    d = Diagram("fig-9-6", 864, 340, "Encore's webhook retry schedule",
                "Time after the event runs left to right, not to scale. Attempt 1 is immediate, and the delivery "
                "is logged with its status code and latency. Attempts 2 to 4 come at 30 seconds, 2 minutes and "
                "10 minutes, and the event is marked retrying with its next attempt time. Attempts 5 to 7 come at "
                "30 minutes, 1 hour and 3 hours, and the endpoint's health turns amber in the portal. From "
                "attempt 8 onward, delivery is retried every 6 hours; after 24 hours of continuous failure the "
                "partner's technical contacts get an email and a portal banner. At 72 hours the endpoint is "
                "disabled with notice, and its events are kept for replay for 14 days. Partners may shorten the "
                "total window to 24 hours or choose other intervals within bounds.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'ONE EVENT TO A FAILING ENDPOINT · TIME AFTER THE EVENT, NOT TO SCALE</text>')
    TY = 96
    marks = [(72, "0", 1), (152, "30 S", 2), (232, "2 MIN", 3), (312, "10 MIN", 4), (392, "30 MIN", 5),
             (472, "1 H", 6), (552, "3 H", 7), (672, "24 H", None), (808, "72 H", None)]
    # the track: solid through attempt 7, dashed for the every-6-h tail
    d.zones.append(f'<line class="dg-ill-soft" x1="72" y1="{TY}" x2="552" y2="{TY}"/>')
    d.zones.append(f'<line class="dg-ill-soft" x1="552" y1="{TY}" x2="808" y2="{TY}" stroke-dasharray="5 4"/>')
    for x, t, n in marks:
        if n:
            d.nodes.append(f'<circle class="dg-ill-fill" cx="{x}" cy="{TY}" r="5"/>')
            d.extra.append(f'<text class="dg-name" x="{x}" y="{TY - 16}">{n}</text>')
        elif t == "24 H":
            d.zones.append(f'<line class="dg-ill-ink" x1="{x}" y1="{TY - 8}" x2="{x}" y2="{TY + 8}"/>')
        if t == "72 H":
            d.extra.append(f'<rect class="dg-mask" x="{x - 14}" y="{TY + 14}" width="28" height="14" rx="2"/>')
        d.extra.append(f'<text class="dg-tick" x="{x}" y="{TY + 24}" text-anchor="middle">{t}</text>')
    d.label_at("ATTEMPT 8 ONWARD · EVERY 6 H", 680, TY, horizontal=True, side="above")
    # the turn: disabled at 72 h
    d.nodes.append(f'<line class="dg-ill-accent" x1="808" y1="{TY - 24}" x2="808" y2="244"/>')
    d.label_at("DISABLED", 808, TY - 24, horizontal=True, side="above", kind="accent")
    # what the partner sees
    SY, SH = 152, 40
    segs = [(24, 112, "Logged", ["status code", "and latency"]),
            (116, 348, "Retrying", ["event marked \"retrying\",", "next attempt time shown"]),
            (352, 668, "Health amber", ["endpoint health turns amber", "in the portal, and stays so"]),
            (672, 804, "Email + banner", ["after 24 h of failure,", "to technical contacts"])]
    d.extra.append(f'<text class="dg-eyebrow" x="24" y="{SY - 12}" style="text-anchor:start">'
                   f'WHAT THE PARTNER SEES</text>')
    for x0, x1, name, notes in segs:
        d.node(x0, SY, x1 - x0, SH, name, None, "backend")
        for i, n in enumerate(notes):
            d.note(x0 + 4, SY + SH + 20 + i * 14, n)
    d.note(800, 264, "72 h: endpoint disabled with notice; events kept for replay for 14 days", anchor="end")
    d.note(800, 280, "Partners may shorten the window to 24 h, or choose intervals within bounds", anchor="end")
    d.legend([("backend", "What the partner sees in the portal"), ("focal", "Endpoint disabled at 72 h")])
    return d
