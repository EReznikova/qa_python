from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_book(self):
         # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector() 

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_long_named_book(self):
        collector = BooksCollector() 
        long_name = '123456789012345678901234567890123456789012' #42 символа
        collector.add_new_book(long_name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_empty_named_book(self):
        collector = BooksCollector() 
        book_name = '' 
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_genre_in_set(self):
        collector = BooksCollector() 
        book_name = 'Назад в будущее'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.books_genre[book_name] == book_genre

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector() 
        book_name = 'Назад в будущее'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre        

    def test_get_books_with_specific_genre_genre_in_set(self):
        collector = BooksCollector() 
        book_name = 'Назад в будущее'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_books_with_specific_genre(book_genre) == [book_name]

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Назад в будущее')
        collector.set_book_genre('Назад в будущее', 'Фантастика')
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')        

        assert collector.get_books_genre() == {
            'Назад в будущее': 'Фантастика',
            'Звонок': 'Ужасы'
        }


    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Назад в будущее')
        collector.set_book_genre('Назад в будущее', 'Фантастика')
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы') 

        assert collector.get_books_for_children() == ['Назад в будущее']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Назад в будущее')
        collector.add_book_in_favorites('Назад в будущее')

        assert collector.favorites[0] == 'Назад в будущее'

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Назад в будущее')
        collector.add_book_in_favorites('Назад в будущее')
        collector.delete_book_from_favorites('Назад в будущее')

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Назад в будущее')
        collector.add_new_book('Звонок')
        collector.add_book_in_favorites('Назад в будущее')
        collector.add_book_in_favorites('Звонок')

        assert collector.get_list_of_favorites_books() == ['Назад в будущее', 'Звонок']
