from datetime import datetime, timedelta

from .sms import send_sms
from .store import Store

REMINDER_LEAD = timedelta(hours=24)


def send_due_reminders(store: Store, now: datetime, already_sent: set[int]) -> list[int]:
    """Run every few minutes. Texts each patient 24 hours before their appointment, once."""
    reminded = []
    for appt in store.appointments.values():
        if appt.status != "booked" or appt.id in already_sent:
            continue
        if now >= appt.slot.starts_at - REMINDER_LEAD and now < appt.slot.starts_at:
            send_sms(appt.patient_phone, f"Reminder: you have an appointment tomorrow at {appt.slot.starts_at:%H:%M}.")
            already_sent.add(appt.id)
            reminded.append(appt.id)
    return reminded
