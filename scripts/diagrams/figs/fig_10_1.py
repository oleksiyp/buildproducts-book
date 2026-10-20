"""Figure 10.1: the Gmail launch as a timeline, August 2001 to 2012, with the storage offer to scale."""
from html import escape

from dg import Diagram
from registry import figure

X0, PER_YEAR = 72, 60  # x of 1 January 2001; pixels per year


def yx(year):
    return X0 + (year - 2001) * PER_YEAR


@figure
def fig_10_1():
    d = Diagram("fig-10-1", 864, 528, "Gmail's launch, 2001 to 2012",
                "A schematic timeline from 2001 to 2012. Paul Buchheit began Gmail, code-named Caribou, in "
                "August 2001 and built a first searchable prototype in about a day; about a dozen people "
                "worked on it by launch, on about 300 old Pentium III machines nobody else at Google wanted. "
                "Google launched it on 1 April 2004, giving accounts to about 1,000 people outside the company, "
                "each able to invite a couple of friends; invitations later sold on eBay for $150 and more. "
                "On 6 April 2004, five days after launch, 31 organizations and advocates asked Google to "
                "suspend Gmail because it scanned mail to place ads, and California State Senator Liz Figueroa "
                "drafted a consent bill. The invitation gate lasted until sign-up opened to all on 14 February "
                "2007. The beta label stayed on the logo until 7 July 2009, when Google removed it from Gmail, "
                "Calendar, Docs and Talk together, because business customers did not want something that "
                "sounded unfinished. By 2012 Gmail had 425 million active users. Below the timeline, the free "
                "storage offered in April 2004 is drawn to scale: Hotmail 2 MB and Yahoo Mail 4 MB are "
                "hairlines beside Gmail's 1,000 MB, about 500 times Hotmail's.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'GMAIL, 2001–2012 · SCHEMATIC TIMELINE, YEARS TO SCALE</text>')

    caribou, launch, open_, unbeta, y2012 = yx(2001.58), yx(2004.25), yx(2007.12), yx(2009.51), yx(2012.0)
    # spans: what was in force, and for how long
    spans = [
        (56, caribou, launch, "CARIBOU, IN THE MAKING", "dg-ill-fill", "about a dozen people; ~300 old Pentium IIIs"),
        (92, launch, open_, "INVITATION GATE", "dg-ill-fill-accent", "invitations sell on eBay for $150 and more"),
        (128, launch, unbeta, "BETA LABEL ON THE LOGO", "dg-ill-fill", "kept after sign-up opened"),
    ]
    for y, a, b, name, cls, note in spans:
        d.nodes.append(f'<rect class="{cls}" x="{a:.1f}" y="{y}" width="{b - a:.1f}" height="24" rx="3"/>')
        d.extra.append(f'<text class="dg-label" x="{(a + b) / 2:.1f}" y="{y + 15}">{escape(name)}</text>')
        d.note(round(b) + 8, y + 16, note)

    # the axis, in years
    AY = 184
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AY}" x2="{yx(2013)}" y2="{AY}"/>')
    for yr in range(2001, 2014):
        x = yx(yr)
        d.zones.append(f'<line class="dg-axis" x1="{x}" y1="{AY}" x2="{x}" y2="{AY + 4}"/>')
        d.zones.append(f'<text class="dg-tick" x="{x}" y="{AY + 16}" text-anchor="middle">{yr}</text>')

    # events: (x, top of the text block, header, lines, kind)
    T1, T2 = 232, 316
    events = [
        (caribou, T1, "AUG 2001", ["Buchheit starts Caribou;", "prototype in about a day"], "muted"),
        (launch, T1, "1 APR 2004 · LAUNCH", ["1 GB free; ~1,000 outsiders,", "each invites a couple", "of friends"], "muted"),
        (open_, T1, "14 FEB 2007", ["sign-up open to all;", "the gate comes down"], "muted"),
        (y2012, T1, "2012", ["425 million", "active users"], "muted"),
        (launch, T2, "6 APR 2004 · FIVE DAYS IN", ["31 organizations ask Google", "to suspend Gmail over ads", "beside scanned mail;",
                                                  "Figueroa drafts a consent bill"], "link"),
        (unbeta, T2, "7 JUL 2009", ["beta label removed, with", "Calendar, Docs and Talk;", "business customers had",
                                    "balked at \"unfinished\""], "muted"),
    ]
    for x, top, head, lines, kind in events:
        line_cls = "dg-ill-link" if kind == "link" else "dg-ill-soft"
        d.zones.append(f'<line class="{line_cls}" x1="{x:.1f}" y1="{AY + 24}" x2="{x:.1f}" y2="{top + 4 + 14 * len(lines)}"/>')
        hcls = "dg-label dg-l-link" if kind == "link" else "dg-label"
        d.extra.append(f'<text class="{hcls}" x="{x + 8:.1f}" y="{top}" style="text-anchor:start">{escape(head)}</text>')
        for i, t in enumerate(lines):
            d.note(round(x) + 8, top + 16 + 14 * i, t)
    for x in (caribou, launch, open_, unbeta, y2012):
        d.nodes.append(f'<circle class="dg-ill-fill" cx="{x:.1f}" cy="{AY}" r="4"/>')

    # the offer, to scale
    SY, SX, SW = 412, 152, 520  # SW pixels = 1,000 MB
    d.extra.append(f'<text class="dg-eyebrow" x="24" y="{SY - 12}" style="text-anchor:start">'
                   'FREE STORAGE OFFERED, APRIL 2004 · BARS TO SCALE</text>')
    rows = [("Hotmail", 2, "2 MB", "dg-ill-fill"), ("Yahoo Mail", 4, "4 MB", "dg-ill-fill"),
            ("Gmail", 1000, "1,000 MB · about 500 × Hotmail", "dg-ill-fill-accent")]
    for i, (name, mb, label, cls) in enumerate(rows):
        y = SY + 4 + i * 24
        w = SW * mb / 1000
        d.note(SX - 12, y + 10, name, anchor="end")
        d.nodes.append(f'<rect class="{cls}" x="{SX}" y="{y}" width="{w:.2f}" height="14"/>')
        d.note(round(SX + w) + 10, y + 11, label)
    d.legend([("backend", "Span or event"), ("focal", "The gate, and the offer behind it"),
              ("arrow:link", "The outside objection")])
    return d
