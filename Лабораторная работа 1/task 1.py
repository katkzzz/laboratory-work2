import doctest


class Phone:
    """
    Абстрактный класс, описывающий телефон.
    """

    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создание объекта "Телефон".

        :param brand: Бренд телефона (например, "Apple", "Samsung").
        :param model: Модель телефона.
        :param battery_capacity: Емкость батареи телефона в мАч.
        :raise ValueError: Если емкость батареи отрицательная.

        Примеры:
        >>> phone = Phone("Apple", "iPhone 14", 3200)
        """
        if battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом.")
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def make_call(self, number: str) -> None:
        """
        Совершает звонок на указанный номер.

        :param number: Номер телефона для звонка.
        :raise ValueError: Если номер пустой.

        Примеры:
        >>> phone = Phone("Apple", "iPhone 14", 3200)
        >>> phone.make_call("+123456789")
        """
        ...

    def charge(self, amount: int) -> None:
        """
        Заряжает телефон.

        :param amount: Количество заряда в мАч.
        :raise ValueError: Если количество заряда отрицательное.

        Примеры:
        >>> phone = Phone("Samsung", "Galaxy S22", 4000)
        >>> phone.charge(500)
        """
        ...


class Book:
    """
    Абстрактный класс, описывающий книгу.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.
        :raise ValueError: Если количество страниц отрицательное или равно 0.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int) -> None:
        """
        Читает указанное количество страниц.

        :param pages_to_read: Количество страниц для чтения.
        :raise ValueError: Если количество страниц отрицательное.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read(50)
        """
        ...

    def bookmark(self, page: int) -> None:
        """
        Устанавливает закладку на указанной странице.

        :param page: Номер страницы для закладки.
        :raise ValueError: Если номер страницы выходит за пределы книги.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.bookmark(150)
        """
        ...


class CloudStorage:
    """
    Абстрактный класс, описывающий облачное хранилище.
    """

    def __init__(self, name: str, capacity: int, used_space: int):
        """
        Создание объекта "Облачное хранилище".

        :param name: Название хранилища (например, "Google Drive").
        :param capacity: Общий объем хранилища в гигабайтах.
        :param used_space: Используемый объем хранилища в гигабайтах.
        :raise ValueError: Если используемое место превышает общий объем или отрицательное.

        Примеры:
        >>> cloud = CloudStorage("Google Drive", 100, 20)
        """
        if used_space < 0 or used_space > capacity:
            raise ValueError("Используемое место должно быть в пределах общего объема.")
        self.name = name
        self.capacity = capacity
        self.used_space = used_space

    def upload_file(self, file_size: int) -> None:
        """
        Загружает файл в облачное хранилище.

        :param file_size: Размер файла в гигабайтах.
        :raise ValueError: Если размер файла отрицательный или превышает доступное место.

        Примеры:
        >>> cloud = CloudStorage("Google Drive", 100, 20)
        >>> cloud.upload_file(5)
        """
        ...

    def delete_file(self, file_size: int) -> None:
        """
        Удаляет файл из облачного хранилища.

        :param file_size: Размер файла в гигабайтах.
        :raise ValueError: Если размер файла отрицательный или превышает используемое место.

        Примеры:
        >>> cloud = CloudStorage("Dropbox", 50, 30)
        >>> cloud.delete_file(10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
