import doctest


# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Closet:
    def __init__(self, material: str, capacity: int, color: str):
        """
        Инициализация шкафа.

        :param material: Материал, из которого сделан шкаф ('дерево', 'ЛДСП', 'МДФ', 'шпон').
        :param capacity: Вместимость шкафа (в количестве вещей).
        :param color: Цвет шкафа.
        """
        if not isinstance(material, str):
            raise TypeError("Материал шкафа должен быть типа str")
        if material not in ['дерево', 'ЛДСП', 'МДФ', 'шпон']:
            raise ValueError("Материал шкафа должен быть одним из: 'дерево', 'ЛДСП', 'МДФ', 'шпон'")
        self.material = material

        if not isinstance(capacity, int):
            raise TypeError("Вместимость шкафа должна быть типа int")
        if capacity <= 0:
            raise ValueError("Вместимость шкафа должна быть положительным числом")
        self.capacity = capacity

        if not isinstance(color, str):
            raise TypeError("Цвет шкафа должен быть типа str")
        self.color = color

    def describe(self) -> str:
        """
        Возвращает описание шкафа.

        :return: Описание шкафа.
        >>> closet = Closet('дерево', 100, 'коричневый')
        >>> closet.describe()
        'Коричневый шкаф вместимостью 100 вещей, материал: дерево.'
        """
        return f"{self.color.capitalize()} шкаф вместимостью {self.capacity} вещей, материал: {self.material}."

    def recolor(self, new_color: str = 'белый') -> None:
        """
        Перекрашивает шкаф в любой цвет.

        :param new_color: Новый цвет шкафа (по умолчанию: 'коричневый').

        :raise TypeError: Если задаваемый цвет шкафа не типа str.

        >>> closet = Closet('шпон', 200, 'красный')
        >>> closet.recolor('серый')
       """
        if not isinstance(new_color, str):
            raise TypeError("Цвет шкафа должен быть типа str")
        self.color = new_color


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


# TODO: описать ещё класс
class Bath:
    def __init__(self, capacity: float, water_level: float = 0.0):
        """
        Инициализация объекта ванны.

        :param capacity: Вместимость ванны в литрах.
        :param water_level: Уровень воды в ванной (по умолчанию: 0.0 литров).
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость ванны должна быть типа int или float")
        if capacity < 0:
            raise ValueError("Вместимость не может быть отрицательной.")
        self.capacity = capacity

        if not isinstance(capacity, (int, float)):
            raise TypeError("Уровень воды должен быть типа int или float")
        if water_level < 0:
            raise ValueError("Уровень воды не может быть отрицательным")
        self.water_level = water_level

    def fill_water(self, amount: float) -> str:
        """
        Наполняет ванну некоторым количеством воды.

        :param amount: Количество воды для наполнения ванны.
        :return: Сообщение о новом уровне воды.
        :raises ValueError: Если количество воды превышает вместимость ванны.

        >>> bath = Bath(150)
        >>> bath.fill_water(100)
        'В ванну добавлено 100 литров воды. Текущий уровень воды: 100.0 литров.'
        """
        if self.water_level + amount >= self.capacity:
            raise ValueError("Невозможно добавить столько воды, ванна переполнится.")
        self.water_level += amount
        return f"В ванну добавлено {amount} литров воды. Текущий уровень воды: {self.water_level} литров."

    def drain_water(self) -> str:
        """
        Сливает всю воду из ванны.

        :return: Сообщение о сливе воды.

        >>> bath = Bath(200, 100)
        >>> bath.drain_water()
        'Вся вода из ванны слита.'
        """
        self.water_level = 0
        return "Вся вода из ванны слита."


# TODO: и ещё один
class Anime:
    def __init__(self, title: str, episodes: int, genre: str):
        """
        Инициализация объекта аниме.

        :param title: Название аниме.
        :param episodes: Количество серий.
        :param genre: Жанр аниме.
        """
        if not isinstance(title, str):
            raise TypeError("Название аниме должно быть типа str")
        self.title = title

        if episodes < 1:
            raise ValueError("Количество серий меньше 1.")
        self.episodes = episodes

        if not isinstance(title, str):
            raise TypeError("Жанр аниме должен быть типа str")
        self.genre = genre

    def get_info(self) -> str:
        """
        Выдает информацию об аниме.

        :return: Строка с информацией о названии, жанре и количестве серий.

        >>> anime = Anime('Магическая битва', 47, 'Экшен')
        >>> anime.get_info()
        'Аниме "Магическая битва", Жанр: Экшен, Серий: 47.'
        """
        return f'Аниме "{self.title}", Жанр: {self.genre}, Серий: {self.episodes}.'

    def watch_episodes(self, episodes_watched: int = 0) -> str:
        """
        Просмотреть определённое количество серий.

        :param episodes_watched: Количество серий для просмотра.
        :return: Сообщение о количестве просмотренных серий.

        >>> anime = Anime('Берсерк', 36, 'Драма')
        >>> anime.watch_episodes(10)
        'Вы посмотрели 10 серий.'
        """
        if episodes_watched > self.episodes:
            raise ValueError("Невозможно посмотреть больше серий, чем есть в аниме.")
        self.episodes -= episodes_watched
        return f"Вы посмотрели {episodes_watched} серий."
