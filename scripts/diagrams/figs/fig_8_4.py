"""Figure 8.4: Encore's weekly app train, Monday to the following Monday."""
from dg import Diagram
from registry import figure


@figure
def fig_8_4():
    d = Diagram("fig-8-4", 864, 336, "Encore's weekly app train",
                "Six day columns, Monday to the following Monday. Monday 12:00: the Mobile App team cuts the "
                "release branch, after which only fixes for blocking bugs go in. Monday and Tuesday: a staff beta "
                "of about 600 Encore staff and a public beta of about 20,000 fans, triaged by module owners. "
                "Wednesday: the release captain, a rotating role, runs a regression pass on the critical "
                "journeys, makes the go or no-go call and submits to both stores. Thursday: the release captain "
                "begins the rollout if review has cleared. Friday: no rollout step widens while a major on-sale "
                "is running, a rule set by the calendar, as for server canaries. The following Monday: the "
                "release captain widens the rollout if the halt criteria of Figure 8.5 are clear. A feature "
                "that misses the train waits one week; the train never waits for it.")
    C0, CW = 24, 136
    col = lambda i: C0 + i * CW  # noqa: E731
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "FOLLOWING MONDAY"]
    for i, name in enumerate(days):
        d.extra.append(f'<text class="dg-eyebrow" x="{col(i) + CW // 2}" y="44">{name}</text>')
        if i:
            d.zones.append(f'<line class="dg-ill-soft" x1="{col(i)}" y1="32" x2="{col(i)}" y2="276" '
                           f'stroke-dasharray="2 4"/>')
    R1, R2, H, W = 64, 160, 60, 112
    cx = lambda i: col(i) + 12  # noqa: E731
    # connectors
    d.path([(cx(0) + 56, R1 + H), (cx(0) + 56, R2)])
    d.path([(col(2) - 16, R2 + H // 2), (col(2), R2 + H // 2), (col(2), R1 + H // 2), (cx(2), R1 + H // 2)])
    d.path([(cx(2) + 56, R1 + H), (cx(2) + 56, R2)])
    for i in (2, 3, 4):
        d.path([(cx(i) + W, R2 + H // 2), (cx(i + 1), R2 + H // 2)])
    # steps
    d.node(cx(0), R1, W, H, "Branch cut", "12:00", tag="MOBILE APP")
    d.note(col(1) + 12, R1 + 26, "after the cut:")
    d.note(col(1) + 12, R1 + 39, "blocking fixes only")
    d.node(cx(0), R2, 244, H, "Staff and public beta", "~600 staff · ~20,000 fans",
           tag="MODULE OWNERS TRIAGE")
    d.node(cx(2), R1, W, H, "Go or no-go", "regression pass", tag="RELEASE CAPTAIN")
    d.node(cx(2), R2, W, H, "Submit", "to both stores", tag="RELEASE CAPTAIN")
    d.node(cx(3), R2, W, H, "Begin rollout", "if review cleared", tag="RELEASE CAPTAIN")
    d.node(cx(4), R2, W, H, "Hold", "no step widens", "focal", tag="CALENDAR")
    d.node(cx(5), R2, W, H, "Widen", "if halts clear", tag="RELEASE CAPTAIN")
    d.note(cx(4), R2 + H + 16, "while a major on-sale")
    d.note(cx(4), R2 + H + 29, "is running")
    d.note(cx(5), R2 + H + 16, "halt criteria:")
    d.note(cx(5), R2 + H + 29, "Figure 8.5")
    d.labels.append(f'<rect class="dg-mask" x="{col(3) + 8}" y="{R1 + 14}" width="256" height="32" rx="2"/>')
    d.note(col(3) + 12, R1 + 26, "A feature that misses the cut waits one week;")
    d.note(col(3) + 12, R1 + 39, "the train never waits for a feature.")
    d.legend([("backend", "Step, tagged with who runs it"),
              ("focal", "The on-sale rule the week is built around"), ("arrow:muted", "The train moves on")])
    return d
