from datetime import datetime

import pytest

from careslot.cancellations import TooLateToCancel, cancel
from careslot.models import Appointment, Slot


def _appt(starts_at):
    return Appointment(slot=Slot(doctor_id="dr-lee", starts_at=starts_at), patient_id="pat-1", patient_phone="+15550001")


def test_can_cancel_more_than_24_hours_before():
    appt = _appt(datetime(2026, 12, 3, 9, 0))
    cancel(appt, now=datetime(2026, 12, 1, 9, 0))
    assert appt.status == "cancelled"


def test_cannot_cancel_inside_24_hours():
    appt = _appt(datetime(2026, 12, 1, 18, 0))
    with pytest.raises(TooLateToCancel):
        cancel(appt, now=datetime(2026, 12, 1, 9, 0))
