"""Figure 10.6: the month-18 review's two headline numbers against the lines the memo drew for them."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_10_6():
    d = Diagram("fig-10-6", 864, 264, "The review's two numbers",
                "Left: completed verified resales per eligible event in France at month 18. The average was 34, "
                "above the memo's month-18 target of 30, but the median was 11, because a handful of arena nights "
                "produced most of the resales; kill criterion K2 fires below 10. Right: the synthetic control's "
                "estimate of the change in primary sell-through on resale-enabled events, a fall of 0.4 points, "
                "with an interval from a fall of 1.3 points to a rise of 0.5. The whole interval lies above the "
                "guardrail of no worse than minus 2.0 points, so the guardrail held, but the interval does not "
                "rule out a small harm.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'NORTH STAR · COMPLETED RESALES PER ELIGIBLE EVENT</text>')
    d.extra.append('<text class="dg-eyebrow" x="472" y="28" style="text-anchor:start">'
                   'GUARDRAIL · CHANGE IN PRIMARY SELL-THROUGH (PTS)</text>')

    # left panel: average and median against the target and the kill line
    a = Plot(d, x=96, y=56, w=320, h=120, xr=(0, 40), yr=(0, 3))
    a.axes(xticks=[0, 10, 20, 30, 40], grid=False)
    for name, v, row in (("Average", 34, 2), ("Median", 11, 1)):
        y = a.py(row) - 10
        d.nodes.append(f'<rect class="dg-ill-fill" x="{a.px(0):.1f}" y="{y:.1f}" width="{a.px(v) - a.px(0):.1f}" height="20"/>')
        d.note(88, round(y) + 14, name, anchor="end")
        d.note(round(a.px(v)) + 6, round(y) + 14, str(v))
    a.vline(30, kind="ink", dashed=True)
    a.annotate(30, 3, "MONTH-18 TARGET 30", dx=-4, dy=-2, anchor="end")
    a.vline(10, kind="soft", dashed=True)
    a.annotate(10, 3, "K2 FIRES BELOW 10", dx=-4, dy=-2, anchor="end")

    # right panel: the synthetic control estimate and its interval against the guardrail
    b = Plot(d, x=488, y=56, w=344, h=120, xr=(-2.5, 1.0), yr=(0, 3))
    b.axes(xticks=[-2, -1, 0, 1], grid=False, xfmt=lambda t: f"{t:+d}" if t else "0")
    b.vline(0, kind="soft", dashed=False)
    b.vline(-2.0, kind="accent", dashed=True)
    b.annotate(-2.0, 3, "GUARDRAIL −2.0", dx=4, dy=-2)
    yy = b.py(1.5)
    d.nodes.append(f'<line class="dg-series dg-s-ink" x1="{b.px(-1.3):.1f}" y1="{yy:.1f}" x2="{b.px(0.5):.1f}" y2="{yy:.1f}"/>')
    for v in (-1.3, 0.5):
        d.nodes.append(f'<line class="dg-series dg-s-ink" x1="{b.px(v):.1f}" y1="{yy - 6:.1f}" x2="{b.px(v):.1f}" y2="{yy + 6:.1f}"/>')
    b.dot(-0.4, 1.5, kind="accent", r=5)
    b.annotate(-0.4, 1.5, "−0.4 PTS", dx=-20, dy=-12)
    b.annotate(-1.3, 1.5, "−1.3", dx=-16, dy=22)
    b.annotate(0.5, 1.5, "+0.5", dx=-16, dy=22)
    d.note(472, 216, "Guardrail held; the interval cannot rule out a small harm.")
    d.note(24, 216, "Average above target; the median shows how narrow the reach was.")
    d.legend([("backend", "Measured at month 18"), ("arrow:accent", "The memo's guardrail and the estimate")])
    return d
