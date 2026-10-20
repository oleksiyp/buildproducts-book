"""Figure 7.5: the organizer console as a shell with federated remotes, a discovery manifest and shared singletons."""
from dg import Diagram
from registry import figure


@figure
def fig_7_5():
    d = Diagram("fig-7-5", 864, 480, "The organizer console's shell and remotes",
                "In the organizer's browser, the console shell, owned by the Organizer Console team with a 110 KB "
                "JavaScript budget, owns routing, the organizer's session, the tenant and its theme, error "
                "boundaries and the navigation frame; its objective is that 99.9% of console page loads render "
                "the shell and the requested remote without an error boundary firing, over 28 days. At runtime it "
                "loads the remotes, each shipping on its owner's schedule within 80 KB of JavaScript beyond the "
                "shared singletons: Onboarding, Event Setup, Pricing & Presales, Festivals (Setlist adoption 44%), "
                "Insights and Forecasting, with the resale rules console planned as the seventh. Beneath them, "
                "four shared singletons are loaded once for the page: react, react-dom, @encore/setlist and "
                "@encore/session. Served beside the browser: a discovery manifest, fetched by the shell at "
                "startup, names the current version of each remote, so a remote's owner releases or rolls back by "
                "changing one entry; and the organizer backend for frontend, owned by the Organizer Console team.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="24" style="text-anchor:start">'
                   'ENCORE\'S ORGANIZER CONSOLE · RUNTIME MODULE FEDERATION</text>')
    d.zone(24, 48, 632, 380, "ORGANIZER'S BROWSER")
    d.zone(672, 48, 168, 380, "SERVED")
    d.zone(36, 188, 612, 156, "REMOTES · EACH SHIPS ON ITS OWNER'S SCHEDULE")
    # connectors
    d.path([(636, 96), (684, 96)], kind="accent")
    d.path([(636, 132), (664, 132), (664, 240), (684, 240)])
    d.path([(340, 148), (340, 188)], label="LOADS AT RUNTIME", side="right")
    d.node(44, 76, 592, 72, "Console shell",
           "routing · session · tenant theme · error boundaries · navigation frame", "focal",
           tag="ORGANIZER CONSOLE TEAM · 110 KB JS")
    d.note(44, 172, "SLO: 99.9% of loads, no error boundary, 28 days")
    xs = [44, 196, 348, 500]
    remotes = [("Onboarding", None, "backend"), ("Event Setup", None, "backend"),
               ("Pricing & Presales", None, "backend"), ("Festivals", "Setlist adoption 44%", "backend"),
               ("Insights", None, "backend"), ("Forecasting", None, "backend"),
               ("Resale rules", "7th · planned", "optional")]
    for i, (name, sub, kind) in enumerate(remotes):
        d.node(xs[i % 4], 208 + (i // 4) * 68, 144, 52, name, sub, kind)
    d.note(508, 296, "each: its own team,")
    d.note(508, 309, "its own release,")
    d.note(508, 322, "≤ 80 KB JS beyond")
    d.note(508, 335, "the singletons")
    d.node(36, 360, 612, 52, "Shared singletons, loaded once for the page",
           "react · react-dom · @encore/setlist · @encore/session", "store")
    d.node(684, 72, 144, 52, "Discovery manifest", "a version per remote", "store")
    d.note(684, 144, "fetched at startup;")
    d.note(684, 157, "one entry releases")
    d.note(684, 170, "or rolls back a remote")
    d.node(684, 212, 144, 56, "Organizer BFF", "Organizer Console team")
    d.legend([("focal", "Shell, run as a product"), ("backend", "Remote or service"),
              ("optional", "Planned remote"), ("store", "Shared or served data"),
              ("arrow:accent", "Versions from the manifest")])
    return d
