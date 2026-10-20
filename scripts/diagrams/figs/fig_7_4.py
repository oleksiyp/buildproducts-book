"""Figure 7.4: Setlist's contribution path, from a team's local component to a shared one owned by the core."""
from dg import Diagram
from registry import figure


@figure
def fig_7_4():
    d = Diagram("fig-7-4", 864, 476, "From local to shared in Setlist",
                "A flow in two lanes. In the top lane, owned by the team that built it: a team builds a component "
                "in its own code, in Setlist's style; it registers it in the library as a pattern candidate, "
                "visible to every team but owned by its maker and with no promise of support; then the question "
                "is whether a second team needs it. If not, it stays a candidate and the core never absorbs it. "
                "If so, the flow moves to the bottom lane, owned by the Design System team: the two teams and the "
                "core review it against Setlist's criteria (useful, unique, accessible to the component contract "
                "of Section 6.4, documented, and free of business logic), and then the core team takes ownership "
                "and releases it. Below, the Verified Resale example: VerifiedBadge and ReissueStatus began as "
                "candidates in the Resale team's code during the prototype; Mobile App needed both for the app's "
                "resale module and Fan Messaging needed ReissueStatus for the 'your ticket sold' email; the "
                "accessibility review found that the badge conveyed 'verified' by color and an icon alone, and "
                "the promoted version carries a visible label.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="24" style="text-anchor:start">'
                   'SETLIST\'S CONTRIBUTION PATH · READ ALONG THE ARROWS</text>')
    d.zone(24, 48, 816, 120, "OWNED BY THE TEAM THAT BUILT IT")
    d.zone(24, 200, 816, 120, "OWNED BY THE DESIGN SYSTEM TEAM")
    W, H = 176, 64
    xs = [44, 244, 444, 644]
    R1, R2 = 76, 228
    # connectors
    d.path([(xs[0] + W, R1 + 32), (xs[1], R1 + 32)])
    d.path([(xs[1] + W, R1 + 32), (xs[2], R1 + 32)])
    d.path([(xs[2] + W, R1 + 32), (xs[3], R1 + 32)], dashed=True, label="NO")
    d.path([(xs[2] + W // 2, R1 + H), (xs[2] + W // 2, R2)], label="YES", side="right")
    d.path([(xs[2] + W, R2 + 32), (xs[3], R2 + 32)], kind="accent")
    d.node(xs[0], R1, W, H, "Built locally", "own code, Setlist's style", tag="1 · ONE TEAM")
    d.node(xs[1], R1, W, H, "Pattern candidate", "visible to all · no support", tag="2 · REGISTERED")
    d.node(xs[2], R1, W, H, "Second team needs it?", None, tag="3 · DEMAND")
    d.node(xs[3], R1, W, H, "Stays a candidate", "the core never absorbs it", "optional")
    d.node(xs[2], R2, W, H, "Joint review", "both teams and the core", tag="4 · CRITERIA")
    d.node(xs[3], R2, W, H, "Core owns, releases", "a shared Setlist component", "focal", tag="5 · PROMOTED")
    # the criteria, beside the review
    d.extra.append(f'<text class="dg-eyebrow" x="420" y="{R2 + 6}" style="text-anchor:end">SETLIST\'S CRITERIA</text>')
    for i, t in enumerate(["useful · unique", "accessible to the 6.4 contract", "documented",
                           "free of business logic"]):
        d.note(420, R2 + 22 + 13 * i, t, anchor="end")
    # the worked example
    d.zone(24, 344, 816, 80, "VERIFIED RESALE, TWICE THROUGH THE PATH")
    d.note(44, 368, "1–2 · VerifiedBadge and ReissueStatus begin as candidates in the Resale team's code, in the prototype")
    d.note(44, 384, "3 · Mobile App needs both for the app's resale module; Fan Messaging needs ReissueStatus for \"your ticket sold\"")
    d.note(44, 400, "4 · Review: the badge said \"verified\" by color and an icon alone; the promoted version carries a visible label")
    d.legend([("backend", "Step"), ("optional", "Not promoted"), ("focal", "Shared, owned by the core"),
              ("arrow:accent", "Ownership moves to the core")])
    return d
