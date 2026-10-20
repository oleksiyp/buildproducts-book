"""Figure 8.3: the lifetime of a defect on the web and in a native app, a schematic."""
from html import escape

from dg import Diagram
from registry import figure


def _bracket(d, x0, x1, y, text):
    d.zones.append(f'<path class="dg-ill-soft" d="M {x0},{y - 4} V {y} H {x1} V {y - 4}"/>')
    d.label_at(text, (x0 + x1) / 2, y, horizontal=True, side="below")


@figure
def fig_8_3():
    d = Diagram("fig-8-3", 864, 404, "How long a defect lives",
                "A schematic, not to scale. On the web a defect lives from the deploy that introduced it to the "
                "deploy that removed it, minutes with a good pipeline, and the next visitor never sees the old "
                "version. In a native app the fix has three parts, and only the first is under our control: "
                "build and test the fix; pass store review, where Apple states that on average 90% of "
                "submissions are reviewed in less than 24 hours, with an expedited review for critical fixes; "
                "and wait for fans to update, some the same day, many within a week, while a stubborn minority "
                "never do. Taken together: a day or more to ship the fix, days to weeks before most users have "
                "it, and months before nearly all of them do.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'THE LIFE OF A DEFECT, FROM FIX TO FAN · SCHEMATIC, NOT TO SCALE</text>')
    X0 = 184
    # the web
    d.extra.append('<text class="dg-name" x="24" y="88" style="text-anchor:start">On the web</text>'
                   '<text class="dg-sub" x="24" y="102" style="text-anchor:start">one version in production</text>')
    d.node(X0, 68, 144, 44, "Deploy the fix", "minutes")
    d.note(X0 + 160, 94, "and the next visitor never sees the old version")
    # the native app
    d.extra.append('<text class="dg-name" x="24" y="176" style="text-anchor:start">In a native app</text>'
                   '<text class="dg-sub" x="24" y="190" style="text-anchor:start">only the first part is ours</text>')
    Y, H = 152, 60
    d.node(X0, Y, 176, H, "Build and test fix", "under our control", "backend", tag="1 · OURS")
    d.node(X0 + 176, Y, 200, H, "Store review", "90% in under 24 h", "external", tag="2 · THE STORE'S")
    d.node(X0 + 376, Y, 200, H, "Fans update", "same day to weeks", "focal", tag="3 · THE FANS'")
    d.node(X0 + 576, Y, 80, H, "Never", "a minority", "optional")
    d.note(X0 + 180, Y + H + 16, "expedited review for critical fixes")
    _bracket(d, X0, X0 + 376, 264, "A DAY OR MORE TO SHIP THE FIX")
    _bracket(d, X0, X0 + 496, 296, "DAYS TO WEEKS BEFORE MOST USERS HAVE IT")
    _bracket(d, X0, X0 + 572, 328, "MONTHS BEFORE NEARLY ALL OF THEM DO")
    d.legend([("backend", "Our work"), ("external", "The store's review"),
              ("focal", "Waiting for fans to update"), ("optional", "Fans who never update")])
    return d
