# TODO: описать базовый класс
class Anime:
    """
    Базовый класс Аниме.
    """

    def __init__(self, title: str, genre: str, episodes: int) -> None:
        """
        Инициализация аниме с названием, жанром и количеством серий.

        Параметры:
        title (str): Название аниме.
        genre (str): Жанр аниме.
        episodes (int): Количество серий.
        """
        self.title = title
        self.genre = genre
        self.episodes = episodes

    def __str__(self) -> str:
        """
        Возвращает строковое представление аниме в виде:
        "Название (Жанр) - Количество серий: X"
        """
        return f"{self.title} ({self.genre}) - Количество серий: {self.episodes}"

    def __repr__(self) -> str:
        """
        Возвращает строку, которая воссоздаёт объект Аниме.
        """
        return f"Anime(title='{self.title}', genre='{self.genre}', episodes={self.episodes})"

    def watch(self) -> None:
        """
        Запускает просмотр аниме.
        """
        print(f"Вы начинаете смотреть {self.title}. Приятного просмотра!")


# TODO: описать дочерний класс
class MovieAnime(Anime):
    """
    Дочерний класс для аниме фильмов.

    Атрибуты:
    title (str): Название аниме.
    genre (str): Жанр аниме.
    episodes (int): Количество серий (для фильмов будет равно 1).
    duration (float): Длительность фильма в минутах.
    """

    def __init__(self, title: str, genre: str, duration: float) -> None:
        """
        Инициализация аниме фильма с названием, жанром и длительностью.

        title (str): Название аниме.
        genre (str): Жанр аниме.
        duration (float): Длительность фильма в минутах.
        """
        super().__init__(title, genre, episodes=1)  # Количество серий всегда 1 для фильмов
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля.")
        self.duration = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление аниме фильма в виде:
        "Название (Жанр) - Длительность: X минут"
        """
        return f"{self.title} ({self.genre}) - Длительность: {self.duration} минут"

    def watch(self) -> None:
        """
        Переопределяет метод просмотра аниме фильма с указанием продолжительности.
        """
        print(f"Вы начинаете смотреть аниме фильм {self.title}, который длится {self.duration} минут.")


class SeriesAnime(Anime):
    """ Дочерний класс для аниме сериалов.

    title (str): Название аниме.
    genre (str): Жанр аниме.
    episodes (int): Количество серий.
    seasons: (int): Количество сезонов.
    """

    def __init__(self, title: str, genre: str, episodes: int, seasons: int) -> None:
        super().__init__(title, genre, episodes)
        self.seasons = seasons

    @property
    def seasons(self):
        return self.seasons

    @seasons.setter
    def seasons(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Количество сезонов должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество сезонов должно быть больше нуля.")
        self.seasons = value

    def __str__(self):
        return f"Аниме-сериал '{self.title}'. Жанр: {self.genre}, Серий: {self.episodes}, Сезонов: {self.seasons}"

    def __repr__(self):
        return f"{self.__class__.__name__}(title={self.title!r}, genre={self.genre!r}, episodes={self.episodes!r}, " \
               f"seasons={self.seasons!r})"
