from .models import Appointment, Slot


class Store:
    """In-memory storage. Swap for a database later."""

    def __init__(self):
        self.slots: dict[int, Slot] = {}
        self.appointments: dict[int, Appointment] = {}

    def add_slot(self, slot: Slot) -> Slot:
        self.slots[slot.id] = slot
        return slot

    def active_appointment_for_slot(self, slot_id: int):
        for a in self.appointments.values():
            if a.slot.id == slot_id and a.status == "booked":
                return a
        return None
