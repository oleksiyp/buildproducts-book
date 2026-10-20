"""Figure 4.3: fans needed per arm against the smallest change worth detecting."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_4_3():
    d = Diagram("fig-4-3", 864, 364, "Sample size for the sold-out page",
                "Fans needed in each arm, from 16 sigma squared over delta squared with sigma squared 0.16 "
                "(about 80% of fans leave the sold-out page with no next step), against the smallest change "
                "worth detecting, at about 70,000 triggered fans a week in France. A 2-point change (80% to 78%) "
                "needs 6,400 fans per arm, 12,800 in total, under one week, run for two. 1 point, the "
                "pre-registered minimum, needs 25,600 per arm, 51,200 in total, also under one week, run for two. "
                "0.5 points needs 102,400 per arm, 204,800 in total, about three weeks. 0.25 points needs 409,600 "
                "per arm, 819,200 in total, about twelve weeks. Halving the effect quadruples the fans needed.")
    p = Plot(d, x=88, y=44, w=728, h=240, xr=(0, 2.25), yr=(0, 450000))
    p.axes(xticks=[0.25, 0.5, 1, 1.5, 2], yticks=[0, 100000, 200000, 300000, 400000],
           xlabel="SMALLEST CHANGE WORTH DETECTING (PERCENTAGE POINTS)", ylabel="FANS NEEDED PER ARM",
           xfmt=lambda v: f"{v:g}", yfmt=lambda t: "0" if t == 0 else f"{t // 1000:,}k")
    xs = [0.235 + i * 0.005 for i in range(int((2.2 - 0.235) / 0.005) + 1)]
    p.line([(x, 25600 / x ** 2) for x in xs if 25600 / x ** 2 <= 450000], kind="ink")
    pts = [(2, "2 PTS · 6,400 PER ARM · 12,800 TOTAL · UNDER 1 WEEK, RUN 2", 4, -24, "end"),
           (0.5, "0.5 PTS · 102,400 PER ARM · 204,800 TOTAL · ABOUT 3 WEEKS", -4, -32, "start"),
           (0.25, "0.25 PTS · 409,600 PER ARM · 819,200 TOTAL · ABOUT 12 WEEKS", 12, 3, "start")]
    for x, txt, dx, dy, anc in pts:
        if dy < -8:
            xx, yy = p.pt(x, 25600 / x ** 2)
            d.zones.append(f'<line class="dg-ill-soft" x1="{xx:.1f}" y1="{yy - 4:.1f}" x2="{xx:.1f}" y2="{yy + dy + 4:.1f}"/>')
        p.dot(x, 25600 / x ** 2, kind="ink", r=3.5)
        p.annotate(x, 25600 / x ** 2, txt, dx=dx, dy=dy, anchor=anc)
    xx, yy = p.pt(1, 25600)
    d.zones.append(f'<line class="dg-ill-soft" x1="{xx:.1f}" y1="{yy - 4:.1f}" x2="{xx:.1f}" y2="{yy - 52:.1f}"/>')
    p.dot(1, 25600)
    p.annotate(1, 25600, "1 PT, PRE-REGISTERED · 25,600 PER ARM · 51,200 TOTAL · UNDER 1 WEEK, RUN 2",
               dx=-4, dy=-56, kind="accent")
    p.annotate(1.1, 250000, "HALVE THE CHANGE, QUADRUPLE THE FANS", dx=0, dy=0, anchor="start")
    return d
