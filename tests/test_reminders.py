from datetime import datetime

from careslot import sms
from careslot.booking import book
from careslot.cancellations import cancel
from careslot.models import Slot
from careslot.reminders import send_due_reminders
from careslot.store import Store


def test_cancel_sends_sms_confirmation():
    sms.sent.clear()
    store = Store()
    slot = store.add_slot(Slot(doctor_id="dr-lee", starts_at=datetime(2026, 12, 3, 9, 0)))
    appt = book(store, slot, "pat-1", "+15550001")
    cancel(appt, now=datetime(2026, 12, 1, 9, 0))
    assert sms.sent[-1][0] == "+15550001"
    assert "cancelled" in sms.sent[-1][1]


def test_reminder_sent_24_hours_before_once():
    sms.sent.clear()
    store = Store()
    slot = store.add_slot(Slot(doctor_id="dr-lee", starts_at=datetime(2026, 12, 2, 9, 0)))
    appt = book(store, slot, "pat-1", "+15550001")
    done: set[int] = set()
    assert send_due_reminders(store, datetime(2026, 12, 1, 8, 0), done) == []  # 25h before: too early
    assert send_due_reminders(store, datetime(2026, 12, 1, 9, 0), done) == [appt.id]  # 24h before
    assert send_due_reminders(store, datetime(2026, 12, 1, 9, 5), done) == []  # only once
