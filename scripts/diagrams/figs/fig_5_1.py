"""Figure 5.1: Amazon's DVD price test, September 2000 — one title, two prices, and the month that followed."""
from html import escape

from dg import Diagram
from registry import figure


def _window(d, x, y, w, h, browser, price, accent=False):
    """A schematic browser window showing one DVD and its price."""
    out = [f'<rect class="dg-ill-fill" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>',
           f'<line class="dg-ill-soft" x1="{x}" y1="{y + 24}" x2="{x + w}" y2="{y + 24}"/>',
           f'<text class="dg-eyebrow" x="{x + 12}" y="{y + 16}" style="text-anchor:start">{escape(browser)}</text>',
           f'<rect class="dg-ill-soft" x="{x + 12}" y="{y + 36}" width="{w - 24}" height="16" rx="3"/>',
           f'<text class="dg-sub" x="{x + 20}" y="{y + 47}" style="text-anchor:start">amazon.com</text>',
           # the DVD case and its disc
           f'<rect class="dg-ill-ink" x="{x + 24}" y="{y + 68}" width="72" height="96" rx="3"/>',
           f'<circle class="dg-ill-soft" cx="{x + 60}" cy="{y + 116}" r="24"/>',
           f'<circle class="dg-ill-soft" cx="{x + 60}" cy="{y + 116}" r="5"/>',
           f'<text class="dg-name" x="{x + 120}" y="{y + 88}" style="text-anchor:start">Men in Black</text>',
           f'<text class="dg-sub" x="{x + 120}" y="{y + 104}" style="text-anchor:start">DVD · one of 68 test titles</text>']
    fill = ' fill:var(--dg-accent);' if accent else ''
    out.append(f'<text class="dg-name" x="{x + 120}" y="{y + 144}" '
               f'style="text-anchor:start; font-size:26px;{fill}">{escape(price)}</text>')
    d.extra.append("\n".join(out))


@figure
def fig_5_1():
    d = Diagram("fig-5-1", 864, 444, "Amazon's DVD price test, 2000",
                "Schematic. Top: two browser windows open on amazon.com at the same moment, each showing the DVD "
                "of Men in Black, one of the 68 titles in the test. Computerworld reported the title at $25.97 in "
                "Netscape and $23.97 in Internet Explorer, two dollars apart. Bottom, the episode in five steps: "
                "in September 2000 a five-day test set the discount on each title at random between 20% and 40%; "
                "customers on an online fan forum compared notes and found the same disc at different prices, and "
                "suspected that loyal customers paid more than new ones; Amazon's first explanation, routine tests "
                "of the navigation, site design and product pricing, satisfied nobody; by 14 September it had "
                "refunded 6,896 customers an average of $3.10, a little over $21,000 in all; and its statement of "
                "27 September called the test a mistake and promised that in any future test every buyer would "
                "automatically receive the lowest test price.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'SCHEMATIC · ONE TITLE, ONE MOMENT, TWO BROWSERS · AS COMPUTERWORLD REPORTED IT</text>')
    _window(d, 24, 52, 392, 176, "NETSCAPE", "$25.97", accent=True)
    _window(d, 448, 52, 392, 176, "INTERNET EXPLORER", "$23.97")
    d.note(432, 252, "the same disc, at the same moment, two dollars apart; the discount on each title was "
                     "set at random between 20% and 40%", anchor="middle")
    xs, W, Y, H = [24, 192, 360, 528, 696], 144, 288, 64
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, Y + 36), (b, Y + 36)])
    steps = [
        ("SEPTEMBER 2000", "Five-day test", "68 DVD titles", "backend",
         "discount random,", "20% to 40%"),
        ("ONLINE FAN FORUM", "Notes compared", "same disc, two prices", "backend",
         "suspicion: loyal", "customers pay more"),
        ("FIRST EXPLANATION", "“Routine tests”", "of the whole site", "backend",
         "navigation, design and", "pricing: satisfied nobody"),
        ("BY 14 SEPTEMBER", "Refunds", "6,896 customers", "backend",
         "an average of $3.10,", "a little over $21,000"),
        ("27 SEPTEMBER", "Statement", "“a mistake”", "focal",
         "every test buyer gets", "the lowest test price"),
    ]
    for x, (tag, name, sub, kind, n1, n2) in zip(xs, steps):
        d.node(x, Y, W, H, name, sub, kind, tag=tag)
        d.note(x + 4, Y + H + 20, n1)
        if n2:
            d.note(x + 4, Y + H + 33, n2)
    d.legend([("backend", "Step in the episode"), ("focal", "The remedy worth copying"),
              ("arrow:muted", "Order of events")])
    return d
