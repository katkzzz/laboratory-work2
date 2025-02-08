class MythicalCreature:
    """Базовый класс для всех вымышленных существ."""

    def __init__(self, name: str, habitat: str, magical_power: str):
        """
        Инициализация вымышленного существа.

        :param name: Имя существа.
        :param habitat: Место обитания.
        :param magical_power: Основная магическая способность.
        """
        self._name = name  # Имя не должно изменяться после создания.
        self._habitat = habitat
        self._magical_power = magical_power

    @property
    def name(self) -> str:
        """Геттер для имени существа (изменять нельзя)."""
        return self._name

    @property
    def habitat(self) -> str:
        """Геттер для места обитания."""
        return self._habitat

    @habitat.setter
    def habitat(self, value: str):
        """Сеттер для места обитания."""
        self._habitat = value

    @property
    def magical_power(self) -> str:
        """Геттер для магической способности."""
        return self._magical_power

    @magical_power.setter
    def magical_power(self, value: str):
        """Сеттер для магической способности."""
        self._magical_power = value

    def use_magic(self) -> str:
        """Метод, демонстрирующий магическую способность существа."""
        return f"{self.name} использует свою способность: {self.magical_power}!"

    def __str__(self) -> str:
        return f"{self.name}, обитающий в {self.habitat}, обладает магией: {self.magical_power}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, habitat={self.habitat!r}, magical_power={self.magical_power!r})"


class Dragon(MythicalCreature):
    """Класс для драконов, наследуется от MythicalCreature."""

    def __init__(self, name: str, habitat: str, magical_power: str, fire_temperature: int):
        """
        Инициализация дракона.

        :param name: Имя дракона.
        :param habitat: Место обитания.
        :param magical_power: Основная магическая способность.
        :param fire_temperature: Температура огня, которым дышит дракон.
        """
        super().__init__(name, habitat, magical_power)
        self.fire_temperature = fire_temperature  # Температура огня

    @property
    def fire_temperature(self) -> int:
        """Геттер для температуры огня."""
        return self._fire_temperature

    @fire_temperature.setter
    def fire_temperature(self, value: int):
        """Сеттер для температуры огня (огонь должен быть очень горячим)."""
        if value < 500:
            raise ValueError("Температура огня у дракона должна быть минимум 500 градусов.")
        self._fire_temperature = value

    def breathe_fire(self) -> str:
        """Метод, демонстрирующий дыхание огнем."""
        return f"{self.name} извергает пламя с температурой {self.fire_temperature}°C!"

    def use_magic(self) -> str:
        """
        Переопределенный метод использования магии.
        Драконы могут сочетать свою магию с дыханием огня, поэтому метод изменен.
        """
        return f"{self.name} использует магию {self.magical_power}!"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, habitat={self.habitat!r}, "
                f"magical_power={self.magical_power!r}, fire_temperature={self.fire_temperature})")


class Unicorn(MythicalCreature):
    """Класс для единорогов, наследуется от MythicalCreature."""

    def __init__(self, name: str, habitat: str, magical_power: str, horn_length: float):
        """
        Инициализация единорога.

        :param name: Имя единорога.
        :param habitat: Место обитания.
        :param magical_power: Основная магическая способность.
        :param horn_length: Длина рога единорога.
        """
        super().__init__(name, habitat, magical_power)
        self.horn_length = horn_length  # Длина рога

    @property
    def horn_length(self) -> float:
        """Геттер для длины рога."""
        return self._horn_length

    @horn_length.setter
    def horn_length(self, value: float):
        """Сеттер для длины рога (рог не может быть меньше 10 см)."""
        if value < 10:
            raise ValueError("Длина рога единорога должна быть не менее 10 см.")
        self._horn_length = value

    def heal(self) -> str:
        """Метод, демонстрирующий способность единорога исцелять."""
        return f"{self.name} использует свой рог длиной {self.horn_length} см, чтобы исцелять раны!"

    def use_magic(self) -> str:
        """
        Переопределенный метод использования магии.
        Единороги известны своей светлой магией, поэтому метод изменен.
        """
        return f"{self.name} использует светлую магию: {self.magical_power}!"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name={self.name!r}, habitat={self.habitat!r}, "
                f"magical_power={self.magical_power!r}, horn_length={self.horn_length})")


dragon = Dragon(name="Спайк", habitat="Горах", magical_power="Огненное дыхание", fire_temperature=1200)
unicorn = Unicorn(name="Сахарок", habitat="Волшебном лесу", magical_power="Исцеление", horn_length=50.5)


print(dragon)  # __str__
print(repr(dragon))  # __repr__
print(dragon.use_magic())
print(dragon.breathe_fire())

print("=================================================================================")

print(unicorn)  # __str__
print(repr(unicorn))  # __repr__
print(unicorn.use_magic())
print(unicorn.heal())
