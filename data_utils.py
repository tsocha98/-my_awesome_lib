def convert_to_int(value: str) -> int:
    "Konwertuje wartość na int, zwraca None jeśli nie jest możliwe."
    try:
        return int(value)
    except ValueError:
        return None
