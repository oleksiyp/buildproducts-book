"""Figure 1.5: dual-track development, discovery one iteration ahead of delivery, worked by the same people."""
from dg import Diagram
from registry import figure


@figure
def fig_1_5():
    d = Diagram("fig-1-5", 864, 372, "Discovery and delivery as two tracks",
                "A schematic of dual-track development across four iterations; the ideas are lettered for "
                "illustration only. The discovery track, above, produces validated ideas through research, design "
                "and prototypes; the delivery track, below, produces releasable software. Each idea tested in "
                "discovery in one iteration is built in delivery in the next: idea A is tested in iteration 1 and "
                "built in 2, B in 2 and built in 3, D in 3 and built in 4, while E is tested in 4. Idea C is "
                "tested in iteration 2 and dropped, so it is never built. One frame encloses both tracks: the same "
                "team works in both, every week; they are not two teams and not two phases. A note quotes Jeff "
                "Patton: the most expensive way to test your idea is to build production quality software.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="28" style="text-anchor:start">'
                   'SCHEMATIC · IDEAS LETTERED FOR ILLUSTRATION</text>')
    X0, STEP, W = 176, 168, 152
    DY, VY, H = 96, 208, 52
    xs = [X0 + i * STEP for i in range(4)]
    for i, x in enumerate(xs):
        d.note(x + W // 2, 84, f"ITERATION {i + 1}", anchor="middle")
    # handoffs: tested in iteration k, built in k+1
    for k in (0, 1, 2):
        a, b = xs[k] + W // 2, xs[k + 1] + W // 2
        d.path([(a, DY + H), (a, 164), (b - 40, 164), (b - 40, VY)],
               label="TESTED IDEA" if k == 0 else None, at=1, side="below")
    d.zone(24, 52, 816, 224, "ONE TEAM · THE SAME PEOPLE IN BOTH TRACKS, EVERY WEEK")
    for y, name, sub in ((DY, "Discovery", "validated ideas"), (VY, "Delivery", "releasable software")):
        d.extra.append(f'<text class="dg-name" x="40" y="{y + 24}" style="text-anchor:start">{name}</text>'
                       f'<text class="dg-sub" x="40" y="{y + 39}" style="text-anchor:start">{sub}</text>')
    disc = [("Test idea A", None, "input"), ("Test B and C", "C dropped, never built", "input"),
            ("Test idea D", None, "input"), ("Test idea E", None, "input")]
    for x, (name, sub, kind) in zip(xs, disc):
        d.node(x, DY, W, H, name, sub or "research, design", kind)
    deliv = [("Earlier work", "optional"), ("Build idea A", "backend"), ("Build idea B", "backend"),
             ("Build idea D", "backend")]
    for x, (name, kind) in zip(xs, deliv):
        d.node(x, VY, W, H, name, "production code" if kind == "backend" else None, kind)
    # the dropped idea: one accent mark
    d.nodes.append(f'<rect class="dg-ill-accent" x="{xs[1] + 8}" y="{DY + 32}" width="{W - 16}" '
                   f'height="14" rx="3"/>')
    d.note(24, 304, "“The most expensive way to test your idea is to build production quality software.”"
                    " — Jeff Patton")
    d.legend([("input", "Discovery work"), ("backend", "Delivery work"), ("optional", "Work from earlier iterations"),
              ("arrow:muted", "Tested idea handed to delivery")])
    return d
