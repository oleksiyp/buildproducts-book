"""Figure 8.6: reissue of a resold ticket, and where the guarantee against double entry lives."""
from html import escape

from dg import Diagram
from registry import figure


def _box(d, x, y, w, h, name, sub, lines):
    d.nodes.append(f'<rect class="dg-mask" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>'
                   f'<rect class="dg-n dg-n-backend" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    out = [f'<text class="dg-name" x="{x + 12}" y="{y + 22}" style="text-anchor:start">{escape(name)}</text>',
           f'<text class="dg-sub" x="{x + 12}" y="{y + 36}" style="text-anchor:start">{escape(sub)}</text>',
           f'<line class="dg-rule" x1="{x + 12}" y1="{y + 46}" x2="{x + w - 12}" y2="{y + 46}"/>']
    for i, t in enumerate(lines):
        out.append(f'<text class="dg-note" x="{x + 12}" y="{y + 62 + i * 14}">{escape(t)}</text>')
    d.extra.append("\n".join(out))


@figure
def fig_8_6():
    d = Diagram("fig-8-6", 864, 548, "Reissue, and where the guarantee lives",
                "When a ticket is resold, Encore's Inventory team reissues it. The old ticket identity joins the "
                "revocation list held by every gate scanner, which Venue Entry's software syncs every 30 seconds "
                "while it has a connection and which may run offline for up to four hours; each scanner holds the "
                "per-ticket secrets it needs and accepts one time step either side. The buyer's app receives a new "
                "identity and a new secret, and computes rotating codes from the secret and a clock corrected at "
                "each sync; the gate admits them. The seller's app can still generate well-formed codes from the "
                "old secret, and every gate refuses them. Wallet passes are updated through Fan Messaging on a "
                "best-effort basis, the seller's marked Transferred and the buyer's newly delivered; they are a "
                "courtesy, and a static or rotating wallet barcode is checked against the same list. Bottom, a "
                "schematic of the event day: the default resale window runs from purchase until two hours before "
                "doors open, so every revocation exists before the first fan reaches a gate; a scanner that has "
                "synced once after the window closed holds the complete list, and one that has not shows an "
                "amber status to the gate supervisor. Nothing the fan's phone does is part of the guarantee.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'A RESOLD TICKET IS REISSUED · THE GUARANTEE LIVES AT THE GATE, NOT ON THE PHONE</text>')
    # connectors (drawn before boxes)
    d.path([(112, 160), (112, 64), (740, 64), (740, 88)], kind="accent",
           label="OLD IDENTITY JOINS THE REVOCATION LIST", at=1)
    d.path([(200, 228), (312, 228)], label="NEW ID + SECRET")
    d.path([(112, 272), (112, 340), (312, 340)], kind="link", dashed=True,
           label="FAN MESSAGING · BEST EFFORT", at=1, side="below")
    d.path([(528, 116), (640, 116)], kind="accent", label="REFUSED")
    d.path([(528, 228), (640, 228)], label="ADMITTED")
    d.path([(528, 340), (740, 340), (740, 256)], label="STATIC OR ROTATING BARCODE", at=0,
           side="below")
    # boxes
    _box(d, 24, 160, 176, 112, "Encore reissues", "INVENTORY", ["old identity revoked", "new identity issued"])
    d.node(312, 88, 216, 56, "Seller's app", "old identity, old secret")
    d.node(312, 200, 216, 56, "Buyer's app", "new identity, new secret")
    d.node(312, 312, 216, 56, "Wallet passes", "Apple and Google", "external")
    d.note(316, 160, "codes still well-formed")
    d.note(316, 272, "clock corrected at each sync")
    d.note(316, 384, "\"Transferred\", new pass: a courtesy")
    _box(d, 640, 88, 200, 168, "Gate scanner", "VENUE ENTRY",
         ["per-ticket secrets", "revocation list", "syncs every 30 s", "offline up to 4 h",
          "± one time step"])
    # the event day
    ZY = 424
    d.zone(24, ZY, 816, 72, "EVENT DAY (SCHEMATIC)")
    LY = ZY + 28
    d.zones.append(f'<line class="dg-axis" x1="48" y1="{LY}" x2="816" y2="{LY}"/>')
    for x in (64, 440, 760):
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{x}" cy="{LY}" r="4"/>')
    d.zones.append(f'<rect class="dg-ar-soft" x="64" y="{LY - 6}" width="376" height="12"/>')
    d.label_at("RESALE WINDOW", 252, LY, side="above")
    d.note(64, LY + 20, "from purchase")
    d.note(440, LY + 20, "closes: doors − 2 h", anchor="middle")
    d.note(440, LY + 33, "every revocation now exists", anchor="middle")
    d.note(760, LY + 20, "doors open", anchor="middle")
    d.note(824, LY + 33, "synced since the close: complete list; not: amber", anchor="end")
    d.legend([("backend", "Encore software"), ("external", "Wallets owned by Apple and Google"),
              ("arrow:accent", "The guarantee"), ("arrow:link:dashed", "Best effort"),
              ("arrow:muted", "Code shown at the gate")])
    return d
