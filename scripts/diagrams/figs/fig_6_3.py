"""Figure 6.3: Norman's seven stages of action and the two gulfs, with the ballot's two errors."""
from dg import Diagram
from registry import figure


@figure
def fig_6_3():
    d = Diagram("fig-6-3", 864, 528, "The seven stages and two gulfs",
                "Norman's seven stages of action drawn as a loop. From the goal at the top, the side of execution "
                "runs down the left: plan the action, specify it, perform it, acting on the world. The side of "
                "evaluation runs up the right: perceive the state of the world, interpret it, compare it with the "
                "goal. The gulf of execution, the distance between what a person wants to do and what the system "
                "lets them see they can do, is bridged by discoverability and mapping; on the butterfly ballot it "
                "produced more than 2,000 votes for Buchanan meant for Gore. The gulf of evaluation, the distance "
                "between the system's state and what the person can perceive and understand of it, is bridged by "
                "feedback; on the ballot it produced about 6,600 net votes lost to Gore through overvotes, and in "
                "Verified Resale's first seller flow a 'Sold' badge beside a ticket that still looked valid.")
    CX = 432
    NW, NH = 176, 44
    LX, RX = 112, 576
    ys = [124, 192, 260]
    GY, WY = 40, 344

    d.zone(88, 100, 224, 220, "GULF OF EXECUTION")
    d.zone(552, 100, 224, 220, "GULF OF EVALUATION")

    # loop: goal -> execution side -> world -> evaluation side -> goal
    d.path([(CX - 80, GY + 22), (LX + NW // 2, GY + 22), (LX + NW // 2, ys[0])])
    d.path([(LX + NW // 2, ys[0] + NH), (LX + NW // 2, ys[1])])
    d.path([(LX + NW // 2, ys[1] + NH), (LX + NW // 2, ys[2])])
    d.path([(LX + NW // 2, ys[2] + NH), (LX + NW // 2, WY + 24), (CX - 120, WY + 24)], label="ACT", at=1)
    d.path([(CX + 120, WY + 24), (RX + NW // 2, WY + 24), (RX + NW // 2, ys[2] + NH)], label="OBSERVE", at=0)
    d.path([(RX + NW // 2, ys[2]), (RX + NW // 2, ys[1] + NH)])
    d.path([(RX + NW // 2, ys[1]), (RX + NW // 2, ys[0] + NH)])
    d.path([(RX + NW // 2, ys[0]), (RX + NW // 2, GY + 22), (CX + 80, GY + 22)])

    d.node(CX - 80, GY, 160, NH, "Goal", "WHAT THE PERSON WANTS", "focal")
    for y, n, s in zip(ys, ("Plan", "Specify", "Perform"),
                       ("THE ACTION", "THE ACTION SEQUENCE", "ACT ON THE WORLD")):
        d.node(LX, y, NW, NH, n, s)
    for y, n, s in zip(ys, ("Compare", "Interpret", "Perceive"),
                       ("THE STATE WITH THE GOAL", "WHAT WAS PERCEIVED", "THE STATE OF THE WORLD")):
        d.node(RX, y, NW, NH, n, s)
    d.node(CX - 120, WY, 240, 48, "The world", "THE SYSTEM AND ITS STATE", "store")

    d.note(88, 420, "BRIDGED BY DISCOVERABILITY AND MAPPING")
    d.note(88, 436, "BALLOT: MORE THAN 2,000 VOTES FOR BUCHANAN")
    d.note(88, 452, "MEANT FOR GORE (WAND ET AL.)")
    d.note(776, 420, "BRIDGED BY FEEDBACK", anchor="end")
    d.note(776, 436, "BALLOT: ABOUT 6,600 NET GORE VOTES LOST", anchor="end")
    d.note(776, 452, "TO OVERVOTES (PALM BEACH POST)", anchor="end")
    d.note(776, 468, "RESALE: 'SOLD' BADGE, OLD TICKET LOOKS VALID", anchor="end")
    d.legend([("focal", "The person's goal"), ("backend", "Stage of action"), ("store", "The system"),
              ("arrow:muted", "The cycle of one action")])
    return d
