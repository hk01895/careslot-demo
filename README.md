# CareSlot

Appointment booking for small clinics. Patients book, cancel and get reminders by SMS; doctors see their day at a glance.

## Requirements

This is the spec agreed with the clinic (Riverside Family Practice).

1. Patients can book an open appointment slot with a doctor.
2. A slot can never be booked twice (no double booking).
3. Patients can cancel an appointment up to 24 hours before it starts.
4. Patients get an SMS confirmation when they cancel.
5. Patients get an SMS reminder 24 hours before their appointment.
6. Doctors can view their schedule for any day.
7. Every booking or cancellation is written to an audit log with who did it and when.
8. Patients can reschedule an appointment to a different open slot.

## Run the tests

```
python -m pytest
```

## Layout

| Path | What it is |
|---|---|
| `careslot/models.py` | Slot and Appointment |
| `careslot/store.py` | In-memory store |
| `careslot/sms.py` | SMS sender (stubbed) |
| `tests/` | Tests |
