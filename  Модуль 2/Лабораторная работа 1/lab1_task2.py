from task_1 import *  # TODO: импортируйте классы, созданные в ходе выполнения прошлого задания if __name__=="__main__":


# TODO: инстанцировать все описанные классы, создав три объекта.C()

def test_closet():
    # Создание экземпляра
    closet = Closet(material='дерево', capacity=100, color='коричневый')
    print(closet.describe())  # Коричневый шкаф вместимостью 100 вещей, материал: дерево.

    # Тест метода recolor
    closet.recolor('серый')

    # Тест валидации аргументов
    try:
        # TODO: вызвать метод с некорректными аргументами (b)
        invalid_closet = Closet('металл', 50, 'синий')
    except (TypeError, ValueError) as er:
        print(f"Ошибка: {er}")


test_closet()


def test_bath():
    # Создание экземпляра
    bath = Bath(capacity=150, water_level=0.0)
    bath.fill_water(100)  # Должно добавить 100 литров воды
    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        # Попытка добавить воды больше, чем вмещает ванна
        bath.fill_water(100)  # Это вызовет исключение ValueError
    except ValueError as er:
        print(f"Ошибка: {er}")

        # Слив воды из ванны
        print(bath.drain_water())  # Должно слить всю воду из ванны

    try:
        # Попытка создать ванну с некорректным параметром
        invalid_bath = Bath('A', -100)  # Вместимость должна быть типа int или float, уровень воды не может быть < 0
    except (TypeError, ValueError) as er:
        print(f"Ошибка: {er}")


test_bath()


# TODO: вызвать метод с некорректными аргументами(a)
def test_anime():
    # Создание экземпляра
    anime = Anime(title='Берсерк', episodes=36, genre='Драма')
    print(anime.get_info())

    # Просмотр 10 серий
    print(anime.watch_episodes(10))  # Должно вывести информацию о просмотренных сериях
    try:
        # Попытка просмотреть больше серий, чем есть
        print(anime.watch_episodes(50))  # Это вызовет исключение ValueError
    except ValueError as er:
        print(f"Ошибка: {er}")

    try:
        # Попытка создать аниме с некорректным параметром
        invalid_anime = Anime(86, -10, 5)  # Некорректное количество серий

        # Просмотр 10 серий
        print(anime.watch_episodes(10))
    except (TypeError, ValueError) as er:
        print(f"Ошибка: неправильные данные {er}")


test_anime()
