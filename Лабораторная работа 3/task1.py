class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def get_name(self):
        return self._name

    def get_author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.get_name()}. Автор {self.get_author()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.set_pages(pages)

    def get_pages(self):
        return self._pages

    def set_pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.get_name()}. Автор {self.get_author()}. Количество страниц: {self.get_pages()}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.set_duration(duration)

    def get_duration(self):
        return self._duration

    def set_duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.get_name()}. Автор {self.get_author()}. Продолжительность: {self.get_duration()} часов"


