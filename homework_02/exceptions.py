"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    """Исключение, возникающее при низком уровне топлива."""

    def __init__(self, message="Low fuel level"):
        super().__init__(message)


class NotEnoughFuel(Exception):
    """Исключение, возникающее когда недостаточно топлива для совершения действия."""

    def __init__(self, message="Not enough fuel"):
        super().__init__(message)


class CargoOverload(Exception):
    """Исключение, возникающее при перегрузке груза."""

    def __init__(self, message="Cargo overload"):
        super().__init__(message)