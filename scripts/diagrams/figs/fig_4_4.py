"""Figure 4.4: randomizing by fan lets the arms trade seats; randomizing by event contains it."""
from dg import Diagram
from registry import figure


@figure
def fig_4_4():
    d = Diagram("fig-4-4", 864, 400, "Randomizing fans or events",
                "Left, randomized by fan: treatment and control fans of one event buy from the same pool of "
                "resale listings. If treated fans buy more, they take seats control fans would otherwise have "
                "bought, so control finds fewer left and the difference is mostly a transfer between arms. "
                "Right, randomized by event, the cluster design: all fans of event A see one fee presentation "
                "and buy from A's listings, all fans of event B see the other and buy from B's, so the "
                "interference stays inside each event. Fans who browse several events still leak across "
                "clusters at the edges. In Encore's experiment 38 organizers let about 520 of their events be "
                "randomized, so its precision is that of about 520 units, not of the millions of fans inside them.")
    d.zone(24, 40, 384, 268, "RANDOMIZED BY FAN")
    d.zone(456, 40, 384, 268, "RANDOMIZED BY EVENT · CLUSTERS")
    # left: one shared pool
    d.path([(120, 124), (120, 196)], kind="accent", label="BUYS MORE", side="right")
    d.path([(312, 124), (312, 196)], kind="muted", dashed=True, label="FINDS FEWER LEFT", side="left")
    d.node(48, 72, 144, 52, "Treatment fans", "one event", "input")
    d.node(240, 72, 144, 52, "Control fans", "same event", "input")
    d.node(96, 196, 240, 52, "One event's listings", "a seat goes to one fan", "store")
    d.note(48, 276, "The arms trade seats: the difference is mostly")
    d.note(48, 290, "a transfer between arms, not an effect.")
    # right: one pool per event
    d.path([(556, 124), (556, 196)])
    d.path([(740, 124), (740, 196)])
    d.path([(632, 108), (648, 108), (648, 220), (664, 220)], kind="muted", dashed=True, arrow=True)
    d.node(480, 72, 152, 52, "Event A's fans", "fee as one figure", "input")
    d.node(664, 72, 152, 52, "Event B's fans", "fee itemized", "input")
    d.node(480, 196, 152, 52, "Event A's listings", None, "store")
    d.node(664, 196, 152, 52, "Event B's listings", None, "store")
    d.note(480, 276, "38 organizers · about 520 events · leaks at the")
    d.note(480, 290, "edges · precision of ~520 units, not millions of fans.")
    d.legend([("input", "Fans in one arm"), ("store", "Resale listings"),
              ("arrow:accent", "Seats taken from the other arm"),
              ("arrow:muted:dashed", "Lost purchase or leak across clusters")])
    return d
