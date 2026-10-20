"""Figure 1.3: Encore's products, customers and teams on one map."""
from html import escape

from dg import Diagram, NAME_CH, SUB_CH
from registry import figure


def block(d, x, y, w, h, kind, tag, name, lines, watch):
    """A product: team-count tag, name, example teams, and the outcome it watches below a rule."""
    assert all(v % 4 == 0 for v in (x, y, w, h)), (name, x, y, w, h)
    assert len(name) * NAME_CH <= w - 12, f"name too wide: {name!r}"
    for ln in [*lines, *watch]:
        assert len(ln) * SUB_CH <= w - 12, f"line too wide: {ln!r}"
    cx = x + w // 2
    tw = int(len(tag) * 5.2 + 10 + 3) // 4 * 4
    out = [f'<rect class="dg-mask" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>',
           f'<rect class="dg-n dg-n-{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>',
           f'<rect class="dg-tagbox dg-t-{kind}" x="{x + 8}" y="{y + 6}" width="{tw}" height="12" rx="2"/>',
           f'<text class="dg-tag dg-t-{kind}" x="{x + 8 + tw / 2:g}" y="{y + 15}">{escape(tag)}</text>',
           f'<text class="dg-name" x="{cx}" y="{y + 38}">{escape(name)}</text>']
    yy = y + 54
    for ln in lines:
        out.append(f'<text class="dg-sub" x="{cx}" y="{yy}">{escape(ln)}</text>')
        yy += 12
    ry = y + h - 20 - 12 * len(watch)
    out.append(f'<line class="dg-rule" x1="{x + 12}" y1="{ry}" x2="{x + w - 12}" y2="{ry}"/>')
    out.append(f'<text class="dg-eyebrow" x="{cx}" y="{ry + 12}">OUTCOME IT WATCHES</text>')
    for i, ln in enumerate(watch):
        out.append(f'<text class="dg-sub" x="{cx}" y="{ry + 25 + 12 * i}">{escape(ln)}</text>')
    d.nodes.append("\n".join(out))


@figure
def fig_1_3():
    d = Diagram("fig-1-3", 864, 588, "Encore's products, customers and teams",
                "A map of Encore's 40 stream-aligned teams, of about nine engineers each, and its platform group. "
                "Four kinds of customer sit at the top, each served by one product. The fan storefront and app "
                "serves fans with 9 teams, such as Fan Discovery, Seat Map, Checkout, Mobile App and Design System, "
                "and watches the share of admitted fans who complete a purchase. The organizer console serves "
                "organizers with 7 teams, such as Organizer Console, Event Setup, Pricing & Presales, Festivals and "
                "Forecasting, and watches the time from contract to first event on sale. The partner and public APIs "
                "serve partners with 3 teams, Public API, Partner APIs and Embeds & Channels, and watch partner "
                "integrations certified and live. Encore SaaS for venues serves venue tenants with 7 teams, such as "
                "Tenant Onboarding, Tenant Configuration, Box Office and Venue Entry, and watches the days from "
                "signature to a venue's first sale. Beneath all four products, 14 shared-domain teams, such as "
                "On-Sale, Bot Screening, Inventory, Orders & Payments and Fan Messaging, serve all four kinds of "
                "customer through the products; each domain watches its service levels, set with its consumers. "
                "Beneath the stream-aligned teams, the internal platform, 9 platform teams of 40 people such as "
                "Reliability, Runtime, Developer Portal and AI Platform, serves Encore's own teams and watches the "
                "share of services on the golden path.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'ENCORE IN ITS NINTH YEAR · WHO EACH TEAM SERVES</text>')
    XS, W = [40, 240, 440, 640], 184
    CY, CH = 44, 36          # customers
    PY, PH = 132, 156        # products
    SY, SH = 336, 76         # shared domains
    LY, LH = 476, 64         # platform
    customers = ["Fans", "Organizers", "Partners", "Venue tenants"]
    products = [
        ("9 TEAMS", "Fan storefront and app", ["Fan Discovery, Seat Map,", "Checkout, Mobile App,",
                                               "Design System"],
         ["share of admitted fans", "who complete a purchase"]),
        ("7 TEAMS", "Organizer console", ["Organizer Console, Event", "Setup, Pricing & Presales,",
                                          "Festivals, Forecasting"],
         ["time from contract to", "first event on sale"]),
        ("3 TEAMS", "Partner and public APIs", ["Public API, Partner APIs,", "Embeds & Channels"],
         ["partner integrations", "certified and live"]),
        ("7 TEAMS", "Encore SaaS for venues", ["Tenant Onboarding, Tenant", "Configuration, Box Office,",
                                               "Venue Entry"],
         ["days from signature to", "a venue's first sale"]),
    ]
    # connectors first
    for x in XS:
        c = x + W // 2
        d.path([(c, PY), (c, CY + CH)], kind="link")
        d.path([(c, SY), (c, PY + PH)])
    d.path([(432, LY), (432, SY + SH + 16)], label="PAVED ROADS FOR ENCORE'S OWN TEAMS", side="right")
    # connectors under the zone, so its label mask sits over the Fans arrow
    d.zones.extend(d.arrows)
    d.arrows.clear()
    d.zone(24, 116, 816, 312, "40 STREAM-ALIGNED TEAMS · ABOUT NINE ENGINEERS EACH")
    for x, name in zip(XS, customers):
        d.node(x, CY, W, CH, name, None, "external")
    for x, (tag, name, lines, watch) in zip(XS, products):
        block(d, x, PY, W, PH, "backend", tag, name, lines, watch)
    d.node(40, SY, 784, SH, "Shared domains, with customers in every column",
           "On-Sale, Bot Screening, Inventory, Orders & Payments, Fan Messaging · outcome: each domain's "
           "service levels, set with its consumers", "store", tag="14 TEAMS")
    d.node(40, LY, 784, LH, "Internal platform",
           "Reliability, Runtime, Developer Portal, AI Platform · outcome: share of services on the golden path",
           "input", tag="9 PLATFORM TEAMS · 40 PEOPLE")
    d.legend([("external", "Customer"), ("backend", "Product and its teams"),
              ("store", "Shared domains"), ("input", "Platform"),
              ("arrow:link", "Serves a customer"), ("arrow:muted", "Serves teams")])
    return d
