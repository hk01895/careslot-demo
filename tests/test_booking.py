from datetime import datetime

import pytest

from careslot.booking import SlotTaken, book
from careslot.models import Slot
from careslot.store import Store


def test_patient_can_book_open_slot():
    store = Store()
    slot = store.add_slot(Slot(doctor_id="dr-lee", starts_at=datetime(2026, 12, 1, 9, 0)))
    appt = book(store, slot, "pat-1", "+15550001")
    assert appt.status == "booked"
    assert appt.slot is slot


def test_slot_cannot_be_double_booked():
    store = Store()
    slot = store.add_slot(Slot(doctor_id="dr-lee", starts_at=datetime(2026, 12, 1, 9, 0)))
    book(store, slot, "pat-1", "+15550001")
    with pytest.raises(SlotTaken):
        book(store, slot, "pat-2", "+15550002")
