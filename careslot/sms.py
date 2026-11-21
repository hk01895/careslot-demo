"""SMS sender. Stubbed: records messages instead of calling a provider."""

sent: list[tuple[str, str]] = []


def send_sms(phone: str, message: str) -> None:
    sent.append((phone, message))
