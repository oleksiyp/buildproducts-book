"""Figure 6.5: the share of usability problems found as users are added (Nielsen and Landauer; Faulkner)."""
from chartkit import Plot
from dg import Diagram
from registry import figure

L = 0.31


@figure
def fig_6_5():
    d = Diagram("fig-6-5", 864, 328, "Problems found per users tested",
                "Nielsen and Landauer's model: if each user reveals a given problem with probability L, n users "
                "find a share 1 minus (1 minus L) to the power n of the problems. With Nielsen's average L of 31%, "
                "the curve rises steeply and flattens: five users find about 84%. Faulkner's 2003 test of 60 users "
                "shows the spread behind the average: random sets of five found anywhere from 55% to 99% of the "
                "problems, ten users raised the minimum to 80%, and twenty to 95%.")
    p = Plot(d, x=72, y=44, w=744, h=228, xr=(0, 20), yr=(0, 100))
    p.axes(xticks=[0, 1, 2, 3, 4, 5, 10, 15, 20], yticks=[0, 25, 50, 75, 100],
           xlabel="USERS TESTED (n)", ylabel="SHARE OF PROBLEMS FOUND",
           yfmt=lambda t: f"{t}%")
    p.line([(n / 10, 100 * (1 - (1 - L) ** (n / 10))) for n in range(0, 201)], kind="ink")
    # Faulkner's spread at five users, and the minimums at ten and twenty
    x5 = p.px(5)
    d.nodes.append(f'<line class="dg-ill-accent" x1="{x5:.1f}" y1="{p.py(55):.1f}" x2="{x5:.1f}" y2="{p.py(99):.1f}"/>')
    for v in (55, 99):
        d.nodes.append(f'<line class="dg-ill-soft" x1="{x5 - 6:.1f}" y1="{p.py(v):.1f}" x2="{x5 + 6:.1f}" y2="{p.py(v):.1f}"/>')
    p.annotate(5, 55, "FAULKNER: SETS OF 5 FOUND 55–99%", dx=12, dy=3, kind="accent")
    p.dot(5, 100 * (1 - (1 - L) ** 5), kind="ink", r=4)
    p.annotate(5, 84, "MODEL, L = 31%: 5 USERS ≈ 84%", dx=-12, dy=3, anchor="end")
    for n, v in ((10, 80), (20, 95)):
        p.dot(n, v, kind="link", r=3.5)
    p.annotate(10, 80, "10 USERS: MINIMUM 80%", dx=8, dy=16)
    p.annotate(20, 95, "20 USERS: MINIMUM 95%", dx=-8, dy=16, anchor="end")
    return d
