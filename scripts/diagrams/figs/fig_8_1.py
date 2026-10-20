"""Figure 8.1: the road to the App Store, June 2007 to October 2008, and the path a build took afterwards."""
from html import escape

from dg import Diagram
from registry import figure


def _card(d, x, y, w, h, date, name, lines, kind="backend"):
    d.nodes.append(f'<rect class="dg-mask" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>'
                   f'<rect class="dg-n dg-n-{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>')
    tcls = "dg-label dg-l-accent" if kind == "focal" else "dg-label"
    out = [f'<text class="{tcls}" x="{x + 12}" y="{y + 16}" style="text-anchor:start">{escape(date)}</text>',
           f'<text class="dg-name" x="{x + 12}" y="{y + 34}" style="text-anchor:start">{escape(name)}</text>']
    for i, t in enumerate(lines):
        out.append(f'<text class="dg-note" x="{x + 12}" y="{y + 50 + i * 13}">{escape(t)}</text>')
    d.extra.append("\n".join(out))


@figure
def fig_8_1():
    d = Diagram("fig-8-1", 864, 520, "The road to the App Store",
                "Top: a timeline from June 2007 to October 2008. In June 2007 the first iPhone shipped with no "
                "third-party native apps; Apple's answer to developers that summer was web applications running "
                "in Safari, and some developers jailbroke their phones to run native code. In March 2008 Apple "
                "announced a software development kit and a store in which developers set their own prices and "
                "keep 70% of the revenue, while Apple hosts, signs and reviews every app. On 10 July 2008 the App "
                "Store opened as a section of iTunes 7.7 with more than 500 native applications; iPhone OS 2.0 "
                "and the iPhone 3G went on sale the next day; on 14 July Apple announced 10 million downloads in "
                "the first weekend. Google's Android Market opened that October. Bottom: the path a build took "
                "from then on, a schematic. The developer's build goes to Apple, which signs and reviews it, so a "
                "fix is a submission and not a deploy; the store then delivers the approved version to everyone "
                "at once, since staged rollouts came years later; and on the phone the version stays until its "
                "owner replaces it. The rules for the whole path are written and revised by the platform owner.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'JUNE 2007 TO OCTOBER 2008 · ONE PLATFORM OWNER\'S REVIEW IN FRONT OF ALL THIRD-PARTY SOFTWARE</text>')
    # month axis: x = 72 + 44 * months since June 2007
    AX, AY = 72, 168
    mx = lambda m: AX + 44 * m  # noqa: E731
    d.zones.append(f'<line class="dg-axis" x1="{mx(0) - 24}" y1="{AY}" x2="{mx(16) + 32}" y2="{AY}"/>')
    names = ["JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
             "JUL", "AUG", "SEP", "OCT"]
    for m, nm in enumerate(names):
        d.zones.append(f'<line class="dg-axis" x1="{mx(m)}" y1="{AY}" x2="{mx(m)}" y2="{AY + 4}"/>')
        if m != 13:  # the July 2008 leader passes here; its card names the month
            d.zones.append(f'<text class="dg-tick" x="{mx(m)}" y="{AY + 16}" text-anchor="middle">{nm}</text>')
    d.zones.append(f'<text class="dg-axis-label" x="{mx(0)}" y="{AY + 30}" text-anchor="middle">2007</text>'
                   f'<text class="dg-axis-label" x="{mx(7)}" y="{AY + 30}" text-anchor="middle">2008</text>')
    # leaders from the axis to each card
    for m, top in ((0, 128), (9, 128), (16, 128)):
        d.zones.append(f'<line class="dg-ill-soft" x1="{mx(m)}" y1="{top}" x2="{mx(m)}" y2="{AY}"/>')
    d.zones.append(f'<line class="dg-ill-soft" x1="{mx(13)}" y1="{AY}" x2="{mx(13)}" y2="216"/>')
    for m in (0, 9, 16):
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{mx(m)}" cy="{AY}" r="4"/>')
    d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{mx(13)}" cy="{AY}" r="5"/>')
    _card(d, 24, 48, 232, 80, "JUNE 2007", "iPhone ships, no native apps",
          ["Apple's answer: web apps in Safari", "some developers jailbreak for native"])
    _card(d, 344, 48, 248, 80, "MARCH 2008", "SDK and store announced",
          ["developers set prices, keep 70%", "Apple hosts, signs, reviews every app"])
    _card(d, 664, 48, 176, 80, "OCTOBER 2008", "Android Market opens",
          ["store review becomes", "the normal path"])
    _card(d, 456, 216, 384, 88, "10 – 14 JULY 2008", "The App Store opens",
          ["10 JUL  in iTunes 7.7, more than 500 native apps",
           "11 JUL  iPhone OS 2.0 and the iPhone 3G on sale",
           "14 JUL  10 million downloads in the first weekend"], kind="focal")
    # the path a build takes from then on
    ZY = 340
    d.zone(24, ZY, 816, 112, "FROM THEN ON · THE PATH FROM A BUILD TO A PHONE (SCHEMATIC)")
    xs, W, NY, NH = [48, 248, 448, 648], 168, ZY + 24, 52
    for a, b in zip(xs, xs[1:]):
        d.path([(a + W, NY + NH // 2), (b, NY + NH // 2)])
    d.node(xs[0], NY, W, NH, "Developer's build", "a fix is a new build")
    d.node(xs[1], NY, W, NH, "Apple signs, reviews", "every app, every update", kind="focal")
    d.node(xs[2], NY, W, NH, "App Store", "to everyone at once")
    d.node(xs[3], NY, W, NH, "The fan's phone", "version stays installed")
    notes = ["a fix is a submission,", "a reviewer stands between", "no staged rollouts until", "until its owner replaces it"]
    notes2 = ["not a deploy", "the build and the user", "years later", "with a newer one"]
    for x, n1, n2 in zip(xs, notes, notes2):
        d.note(x + 4, NY + NH + 16, n1)
        d.note(x + 4, NY + NH + 29, n2)
    d.legend([("focal", "The opening, and the review that came with it"), ("backend", "Event or step"),
              ("arrow:muted", "Path of a release")])
    return d
