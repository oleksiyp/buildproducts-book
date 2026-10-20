"""Figure 5.5: from a resale's lifecycle to the documents derived from it — facts in the event, prices in the book."""
from dg import Diagram
from registry import figure


@figure
def fig_5_5():
    d = Diagram("fig-5-5", 864, 468, "From reissue to invoice",
                "Top left, a listing's lifecycle: listed, reserved, sold, reissued. The partner's commission is "
                "accrued at the sale, but billing starts only at the reissue, when the seller's old barcode has "
                "been revoked and the buyer's issued. Only then does the Resale service emit ResaleCompleted, a "
                "usage event written once with an idempotency key, which carries the facts of the sale and none "
                "of the money. Rating applies to it the entry of the bitemporal price book, recorded with a "
                "valid-from date and a recorded-at date, that was in force on the event's date. From the rated "
                "event three documents are derived: the organizer's payout line for its three points, the "
                "partner's monthly statement line for its four points, and the finance ledger, reconciled daily. "
                "The seller is paid, and the partner's commission released, five days after the event. Four "
                "checks run every night: one rated line per event and one event per line; the parts sum to the "
                "buyer's total, €66 being €60 to the seller plus three shares of the fee; the day's billing "
                "splits equal the day's ledger entries; and each line was rated by the price-book entry valid on "
                "its date.")
    d.extra.append('<text class="dg-eyebrow" x="24" y="32" style="text-anchor:start">'
                   'ONE RESALE · FACTS IN THE EVENT, PRICES IN THE BOOK, DOCUMENTS DERIVED FROM BOTH</text>')
    # the lifecycle
    d.zone(12, 56, 612, 92, "RESALE LIFECYCLE · SOFTWARE BOOK 8.2")
    SY, SH, SW = 76, 56, 128
    sx = [24, 176, 328, 480]
    for a, b in zip(sx, sx[1:]):
        d.path([(a + SW, SY + SH // 2), (b, SY + SH // 2)])
    d.state(sx[0], SY, SW, SH, "Listed")
    d.state(sx[1], SY, SW, SH, "Reserved")
    d.state(sx[2], SY, SW, SH, "Sold", "commission accrued")
    d.state(sx[3], SY, SW, SH, "Reissued", "old barcode revoked", kind="focal")
    # the billable fact, rated against the price book
    EX, EY, EW, EH = 448, 192, 192, 64
    d.path([(544, SY + SH), (544, EY)], kind="accent", label="BILL AT REISSUE", side="right")
    d.node(664, 76, 176, 56, "Price book", "valid_from · recorded_at", "store", tag="BITEMPORAL")
    d.path([(752, 132), (752, EY)])
    d.node(EX, EY, EW, EH, "ResaleCompleted", "idempotency key · no money", "backend", tag="USAGE EVENT")
    d.path([(EX + EW, EY + 32), (664, EY + 32)])
    d.node(664, EY, 176, EH, "Rating", "price in force that day", "backend")
    # derived documents
    OY, OW = 336, 128
    outs = [(432, "Payout line", "organizer · 3 pts", "backend"),
            (572, "Statement line", "partner · 4 pts", "backend"),
            (712, "Finance ledger", "reconciled daily", "store")]
    for x, *_ in outs:
        d.path([(752, EY + EH), (752, 296), (x + OW // 2, 296), (x + OW // 2, OY)])
    for x, name, sub, kind in outs:
        d.node(x, OY, OW, 56, name, sub, kind)
    d.note(432, OY + 76, "seller paid, and partner commission released, five days after the event")
    # nightly checks
    d.zone(12, 192, 396, 184, "NIGHTLY CHECKS")
    checks = ["1 · one rated line per event, one event per line",
              "2 · the parts sum to the buyer's total:",
              "    €66 = €60 to the seller + three shares",
              "3 · the day's billing splits = the day's ledger",
              "4 · each line rated by the entry valid on its date"]
    for i, t in enumerate(checks):
        d.extra.append(f'<text class="dg-note" x="28" y="{224 + i * 20}" xml:space="preserve">{t}</text>')
    d.note(28, 336, "every number paid out can be recomputed")
    d.note(28, 352, "from the events and the price book as they stood")
    d.legend([("focal", "Where billing starts"), ("backend", "Event, step or document"),
              ("store", "Price book and ledger"), ("arrow:accent", "The billable fact is emitted")])
    return d
