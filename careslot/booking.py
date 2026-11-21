from .models import Appointment, Slot
from .store import Store


class SlotTaken(Exception):
    """Raised when someone tries to book a slot that already has an active appointment."""


def book(store: Store, slot: Slot, patient_id: str, patient_phone: str) -> Appointment:
    """Book an open slot with a doctor for a patient."""
    if slot.id not in store.slots:
        raise ValueError("Unknown slot")
    # No double booking: a slot with an active appointment can't be booked again.
    if store.active_appointment_for_slot(slot.id) is not None:
        raise SlotTaken(f"Slot {slot.id} is already booked")
    appt = Appointment(slot=slot, patient_id=patient_id, patient_phone=patient_phone)
    store.appointments[appt.id] = appt
    return appt
