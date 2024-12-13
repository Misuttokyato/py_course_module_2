BOOKS_DATABASE = [
    {"id": 1, "name": "test_name_1", "pages": 200},
    {"id": 2, "name": "test_name_2", "pages": 400}
]


# TODO: написать класс Book
class Book:
    def init(self, id_, name, pages):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def str(self):
        """
        Возвращает строковое представление книги в виде:
        Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def repr(self):
        """
        Возвращает строку, которая может быть использована для инициализации такого же экземпляра:
        Book(id_=1, name='test_name_1', pages=200)
        """
        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


# TODO: написать класс Library
class Library:
    def init(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список).
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        """
        Возвращает следующий id для добавления новой книги.

        :return: Следующий id книги (если книг нет - 1, иначе id последней книги + 1).
        """
        if not self.books:
            return 1
        # Возвращаем id последней книги + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_):
        """
        Возвращает индекс книги по ее id.

        :param id_: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с запрашиваемым id не существует.
        """
        for i, book in enumerate(self.books):
            if book.id == id_:
                return i
        raise ValueError('Книги с запрашиваемым id не существует')


if name == 'main':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
