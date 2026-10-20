"""Figure 9.1: Twitter and its third-party clients, 2006–2023, in three acts."""
from html import escape

from dg import Diagram, label_width
from registry import figure

COLS = [
    ("COURTSHIP, THEN A WARNING · 2006–2011", [
        ("Jul 2006", False, ["Twitter launches; its API is", "open early"]),
        ("Jan 2007", False, ["Iconfactory's Twitterrific for Mac:", "first bird icon; the app that",
                             "popularized \"tweet\""]),
        ("2010", False, ["Twitter buys Tweetie; it becomes", "the official iPhone app"]),
        ("11 Mar 2011", False, ["Ryan Sarver: do not \"build client", "apps that mimic or reproduce the",
                                "mainstream Twitter consumer", "client experience\""]),
        ("May 2011", False, ["Twitter buys TweetDeck, reportedly", "for about $40 million"]),
    ], None),
    ("THE RULES, WITH NOTICE · 2012–2013", [
        ("16 Aug 2012", True, ["Sippey announces API v1.1 and new", "Rules of the Road: auth everywhere;",
                               "60 calls an hour (720 for a few),", "not a flat 350; Display Requirements;",
                               "certification for pre-installed apps;", "permission above 100,000 user",
                               "tokens; apps past it may grow to 200%"]),
        ("5 Sep 2012", False, ["v1.1 ships, with six months", "promised to migrate"]),
        ("18 Oct 2012", False, ["Tweetbot for Mac ships at $19.99:", "its token allotment is fixed"]),
        ("Mar 2013", False, ["v1.0's retirement moved to 7 May,", "with blackout tests before it"]),
        ("11 Jun 2013", False, ["v1.0 returns 410 Gone"]),
    ], "EVERY ENDPOINT KEPT WORKING"),
    ("THE CUT-OFF, WITHOUT NOTICE · 2022–2023", [
        ("Late Oct 2022", False, ["Elon Musk's ownership of Twitter", "begins"]),
        ("12–13 Jan 2023", True, ["Tweetbot, Twitterrific, Echofon and", "other clients stop working,",
                                  "with no notice"]),
        ("17 Jan 2023", False, ["@TwitterDev: \"Twitter is enforcing", "its long-standing API rules\""]),
        ("19 Jan 2023", False, ["Developer Agreement bars a", "\"substitute or similar service or",
                                "product\"; Iconfactory ends", "Twitterrific after 16 years"]),
    ], "THE WRITTEN RULE CAME A WEEK LATER"),
]

CW, GAP, X0, ZY = 256, 24, 24, 64
DATE_H, LINE, ENTRY_GAP = 16, 14, 16


def _col_height(entries):
    return sum(DATE_H + len(lines) * LINE + ENTRY_GAP for _, _, lines in entries)


@figure
def fig_9_1():
    inner = max(_col_height(e) for _, e, _ in COLS)
    zh = (24 + inner + 28 + 3) // 4 * 4
    h = ZY + zh + 64
    d = Diagram("fig-9-1", 864, h, "Twitter's clients, 2006–2023",
                "A schematic timeline in three columns. Courtship, then a warning, 2006 to 2011: Twitter "
                "launches in July 2006 with an API open early; the Iconfactory's Twitterrific for Mac arrives in "
                "January 2007, giving Twitter its first bird icon and popularizing the word tweet; Twitter buys "
                "Tweetie in 2010, which becomes its official iPhone app; on 11 March 2011 Ryan Sarver tells "
                "developers not to build client apps that mimic or reproduce the mainstream Twitter consumer "
                "client experience; in May 2011 Twitter buys TweetDeck, reportedly for about 40 million dollars. "
                "The rules, with notice, 2012 to 2013, highlighted: on 16 August 2012 Michael Sippey announces "
                "API version 1.1 and new Developer Rules of the Road: authentication on every endpoint, 60 calls "
                "an hour per endpoint (720 for a few) in place of a flat 350, Display Requirements, certification "
                "for pre-installed client apps, and Twitter's permission above 100,000 user tokens, with apps "
                "already past that line allowed to grow to 200 percent of their count; version 1.1 ships on "
                "5 September 2012 with six months promised to migrate; Tweetbot for Mac ships on 18 October 2012 "
                "at 19.99 dollars because its token allotment is fixed; in March 2013 version 1.0's retirement "
                "moves to 7 May with blackout tests; on 11 June 2013 version 1.0 returns 410 Gone. Every endpoint "
                "kept working. The cut-off, without notice, 2022 to 2023, highlighted: Elon Musk's ownership "
                "begins in late October 2022; around 12 and 13 January 2023 Tweetbot, Twitterrific, Echofon and "
                "other clients stop working with no notice; on 17 January @TwitterDev says Twitter is enforcing "
                "its long-standing API rules; on 19 January the Developer Agreement bars building a substitute "
                "or similar service or product, and the Iconfactory ends Twitterrific after 16 years. The written "
                "rule came a week after the act.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="36" style="text-anchor:start">'
                   'TWITTER AND ITS THIRD-PARTY CLIENTS · SCHEMATIC TIMELINE, NOT TO SCALE</text>')
    for c, (label, entries, foot) in enumerate(COLS):
        cx = X0 + c * (CW + GAP)
        d.zone(cx, ZY, CW, zh, label)
        rail = cx + 20
        y = ZY + 28
        first = last = None
        for date, accent, lines in entries:
            dot_y = y - 4
            first = dot_y if first is None else first
            last = dot_y
            cls = "dg-ill-fill-accent" if accent else "dg-ill-fill"
            d.nodes.append(f'<circle class="{cls}" cx="{rail}" cy="{dot_y}" r="{6 if accent else 5}"/>')
            d.extra.append(f'<text class="dg-name" x="{rail + 16}" y="{y}" style="text-anchor:start">'
                           f'{escape(date)}</text>')
            for i, line in enumerate(lines):
                assert len(line) * 5.4 <= CW - 44, line
                d.note(rail + 16, y + DATE_H + i * LINE, line)
            y += DATE_H + len(lines) * LINE + ENTRY_GAP
        d.zones.append(f'<line class="dg-ill-soft" x1="{rail}" y1="{first}" x2="{rail}" y2="{last}"/>')
        if foot:
            fw = label_width(foot)
            fy = ZY + zh - 20
            d.labels.append(f'<rect class="dg-mask" x="{cx + 16}" y="{fy}" width="{fw}" height="12" rx="2"/>'
                            f'<text class="dg-label" x="{cx + 16 + fw / 2:g}" y="{fy + 9}">{escape(foot)}</text>')
    d.legend([("backend", "Dated event"), ("focal", "A turn in the terms partners lived by")])
    return d
