from datetime import datetime, timedelta

from .models import Appointment

CANCEL_WINDOW = timedelta(hours=24)


class TooLateToCancel(Exception):
    """Raised when a patient tries to cancel less than 24 hours before the appointment."""


def cancel(appt: Appointment, now: datetime) -> Appointment:
    """Cancel an appointment. Allowed only up to 24 hours before it starts."""
    if appt.status != "booked":
        raise ValueError("Appointment is not active")
    if appt.slot.starts_at - now < CANCEL_WINDOW:
        raise TooLateToCancel("Appointments can only be cancelled up to 24 hours before they start")
    appt.status = "cancelled"
    appt.cancelled_at = now
    # TODO: text the patient a cancellation confirmation
    return appt
