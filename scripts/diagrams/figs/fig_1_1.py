"""Figure 1.1: HealthCare.gov from launch to the US Digital Service, outputs above the line, outcomes below."""
from html import escape

from dg import Diagram, NAME_CH, SUB_CH
from registry import figure


def card(d, x, y, w, h, kind, name, lines):
    assert all(v % 4 == 0 for v in (x, y, w, h)), (name, x, y, w, h)
    assert len(name) * NAME_CH <= w - 12, f"name too wide: {name!r}"
    for ln in lines:
        assert len(ln) * SUB_CH <= w - 12, f"line too wide: {ln!r}"
    dash = ' stroke-dasharray="4,3"' if kind == "optional" else ""
    out = [f'<rect class="dg-mask" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>',
           f'<rect class="dg-n dg-n-{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="6"{dash}/>']
    top = y + (h - (16 + 13 * len(lines))) // 2 + 12
    cx = x + w // 2
    out.append(f'<text class="dg-name" x="{cx}" y="{top}">{escape(name)}</text>')
    for i, ln in enumerate(lines):
        out.append(f'<text class="dg-sub" x="{cx}" y="{top + 18 + 13 * i}">{escape(ln)}</text>')
    d.nodes.append("\n".join(out))


@figure
def fig_1_1():
    d = Diagram("fig-1-1", 864, 440, "HealthCare.gov, October 2013 to August 2014",
                "A timeline of HealthCare.gov's first ten months, with events in order but not to scale. Above the "
                "line is what the organization did; below it is what users experienced. 1 October 2013: the site "
                "opens on the date the White House had promised, built under about 60 contracts with no declared "
                "business owner; about 250,000 people try to use it at once, it is failing within two hours, and "
                "only six people manage to submit an application and select a plan that day. Third week of "
                "October to early December 2013: the repair, in which outside engineers under Jeff Zients and Todd "
                "Park first build a dashboard of the site's health, and CMS staff and contractors work as one "
                "badgeless team with ruthless prioritization; until then nobody could see what users were "
                "experiencing. Early December 2013: the site serves at least 50,000 people at once and uptime has "
                "risen from 43% to 95%. 1 January 2014: coverage begins, the only date the law required. End of "
                "the first open enrollment, 2014: 5.4 million people have selected a plan through the federal "
                "marketplace. August 2014: the US Digital Service is founded, and its Digital Services Playbook's "
                "sixth play says to assign one leader and hold that person accountable.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'HEALTHCARE.GOV · EVENTS IN ORDER, NOT TO SCALE</text>')
    X0, STEP, CW = 36, 132, 124
    cx = [X0 + i * STEP + CW // 2 for i in range(6)]
    AX = 216
    TY, TH = 68, 104
    BY, BH = 268, 104
    # the time axis
    d.zones.append(f'<line class="dg-ill-ink" x1="28" y1="{AX}" x2="836" y2="{AX}"/>')
    tops = {0, 1, 2, 3, 5}
    bottoms = {0, 1, 2, 4}
    for i, c in enumerate(cx):
        if i in tops:
            d.zones.append(f'<line class="dg-ill-soft" x1="{c}" y1="{TY + TH}" x2="{c}" y2="{AX}"/>')
        if i in bottoms:
            d.zones.append(f'<line class="dg-ill-soft" x1="{c}" y1="{AX}" x2="{c}" y2="{BY}"/>')
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{c}" cy="{AX}" r="4"/>')
    # zones after the connectors, so their label masks sit over the lines
    d.zone(24, 52, 816, 132, "ABOVE THE LINE · WHAT THE ORGANIZATION DID")
    d.zone(24, 252, 816, 132, "BELOW THE LINE · WHAT USERS EXPERIENCED")
    dates = ["1 OCT 2013", "3RD WEEK OCT 2013", "EARLY DEC 2013", "1 JAN 2014", "FIRST ENROLLMENT ENDS",
             "AUG 2014"]
    for c, t in zip(cx, dates):
        d.label_at(t, c, AX + 2, horizontal=True, side="below")
    # above the line
    card(d, X0, TY, CW, TH, "backend", "Site opens",
         ["on the date the", "White House set;", "~60 contracts,", "no business owner"])
    card(d, X0 + STEP, TY, CW + STEP, TH, "backend", "The repair",
         ["outside engineers under", "Zients and Park build a", "health dashboard; CMS and",
          "contractors work as one", "badgeless team"])
    card(d, X0 + 3 * STEP, TY, CW, TH, "backend", "Coverage begins",
         ["the only date", "the law required"])
    card(d, X0 + 5 * STEP, TY, CW, TH, "focal", "USDS founded",
         ["Playbook play 6:", "assign one leader,", "hold that person", "accountable"])
    # below the line
    card(d, X0, BY, CW, BH, "focal", "6 people",
         ["apply and select a", "plan on day one;", "~250,000 at once,", "failing in 2 hours"])
    card(d, X0 + STEP, BY, CW, BH, "optional", "Unmeasured",
         ["until then, nobody", "could see what", "users experienced"])
    card(d, X0 + 2 * STEP, BY, CW, BH, "input", "Site recovers",
         ["≥ 50,000 at once;", "uptime from", "43% to 95%"])
    card(d, X0 + 4 * STEP, BY, CW, BH, "input", "5.4 million",
         ["selected a plan", "through the federal", "marketplace"])
    d.legend([("backend", "What was done"), ("input", "What users met"),
              ("optional", "What nobody saw"), ("focal", "The day-one outcome and the lesson")])
    return d
