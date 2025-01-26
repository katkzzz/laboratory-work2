class Animal:
    """
    Базовый класс для всех животных.
    """
    def __init__(self, name: str, age: int):
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def __str__(self) -> str:
        return f"Животное: {self.name}, Возраст: {self.age}"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    def make_sound(self) -> str:
        """
        Метод для издания звука. Должен быть переопределен в дочерних классах.
        """
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

class Dog(Animal):
    """
    Дочерний класс для собаки.
    """
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)  # Унаследованный конструктор базового класса
        self.breed = breed  # Порода собаки

    def __str__(self) -> str:
        return f"Собака: {self.name}, Возраст: {self.age}, Порода: {self.breed}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Переопределяем метод, чтобы собака лаяла.
        """
        return "Гав-гав"

    def fetch(self, item: str) -> str:
        """
        Собака приносит указанный предмет.
        """
        return f"{self.name} принес(ла) {item}!"

class Cat(Animal):
    """
    Дочерний класс для кошки.
    """
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)  # Унаследованный конструктор базового класса
        self.color = color  # Окрас кошки

    def __str__(self) -> str:
        return f"Кошка: {self.name}, Возраст: {self.age}, Окрас: {self.color}"

    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """
        Переопределяем метод, чтобы кошка мяукала.
        """
        return "Мяу"

    def climb(self, surface: str) -> str:
        """
        Кошка карабкается по указанной поверхности.
        """
        return f"{self.name} карабкается по {surface}!"

if __name__ == "__main__":
    dog = Dog(name="Бобик", age=3, breed="Лабрадор")
    cat = Cat(name="Мурка", age=2, color="Белый")

    print(dog)
    print(cat)

    print(dog.make_sound())
    print(cat.make_sound())

    print(dog.fetch("мяч"))
    print(cat.climb("дереву"))
