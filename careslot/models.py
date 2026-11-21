from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import itertools

_ids = itertools.count(1)


@dataclass
class Slot:
    doctor_id: str
    starts_at: datetime
    id: int = field(default_factory=lambda: next(_ids))


@dataclass
class Appointment:
    slot: Slot
    patient_id: str
    patient_phone: str
    status: str = "booked"  # booked | cancelled
    cancelled_at: Optional[datetime] = None
    id: int = field(default_factory=lambda: next(_ids))
