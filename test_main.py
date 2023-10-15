import random
import string

import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def create_book_collector_object(self):
        self.collector = BooksCollector()

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('length', [1,20,40])
    def test_add_new_book_add_books_with_titles_of_different_lengths_successful(self, length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        self.collector.add_new_book(rand_string)
        assert rand_string in self.collector.books_genre.keys()

    def test_set_book_genre_addition_of_genre_successful(self):
        letters = string.ascii_lowercase
        rand_book_name = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
        rand_genre_from_list_of_genres = self.collector.genre[random.randint(0, len(self.collector.genre) - 1)]
        self.collector.add_new_book(rand_book_name)
        self.collector.set_book_genre(rand_book_name, rand_genre_from_list_of_genres)
        assert self.collector.books_genre.get(rand_book_name) == rand_genre_from_list_of_genres

    def test_get_book_genre_search_by_valid_name_successful(self):
        letters = string.ascii_lowercase
        rand_book_name = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
        rand_genre_from_list_of_genres = self.collector.genre[random.randint(0, len(self.collector.genre) - 1)]
        self.collector.add_new_book(rand_book_name)
        self.collector.set_book_genre(rand_book_name, rand_genre_from_list_of_genres)
        assert self.collector.get_book_genre(rand_book_name) == rand_genre_from_list_of_genres

    @pytest.mark.parametrize('length', [1, 5, 10])
    def test_get_books_with_specific_genre_lists_of_different_lengths_successful(self, length):
        genres_of_books = []
        for i in range(length):
            letters = string.ascii_lowercase
            rand_book_name = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
            rand_genre_from_list_of_genres = self.collector.genre[random.randint(0, len(self.collector.genre) - 1)]
            self.collector.add_new_book(rand_book_name)
            self.collector.set_book_genre(rand_book_name, rand_genre_from_list_of_genres)
            genres_of_books.append(rand_genre_from_list_of_genres)
        books_with_specific_genre = []
        desired_genre = genres_of_books[0]
        for name, book_genre in self.collector.books_genre.items():
            if book_genre == desired_genre:
                books_with_specific_genre.append(name)
        assert set(books_with_specific_genre) == set(self.collector.get_books_with_specific_genre(desired_genre))

    def test_get_books_genre(self):
        books_genre = {}
        for i in range(5):
            letters = string.ascii_lowercase
            rand_book_name = ''.join(random.choice(letters) for i in range(random.randint(1, 10)))
            rand_genre_from_list_of_genres = self.collector.genre[random.randint(0, len(self.collector.genre) - 1)]
            self.collector.add_new_book(rand_book_name)
            self.collector.set_book_genre(rand_book_name, rand_genre_from_list_of_genres)
            books_genre[rand_book_name] = rand_genre_from_list_of_genres
        assert set(books_genre) == set(self.collector.get_books_genre())

    def test_get_books_for_children_add_two_books_return_one(self):
        name_book_not_for_children = 'Книга номер 1'
        genre_first_book= 'Ужасы'
        name_book_for_children = 'Книга номер 2'
        genre_second_book = 'Фантастика'
        self.collector.add_new_book(name_book_not_for_children)
        self.collector.set_book_genre(name_book_not_for_children, genre_first_book)
        self.collector.add_new_book(name_book_for_children)
        self.collector.set_book_genre(name_book_for_children, genre_second_book)
        print(self.collector.get_books_for_children())
        assert self.collector.get_books_for_children()[0] == name_book_for_children

    def test_add_book_in_favorites_name_is_not_in_favorites_list_successful(self):
        book_name = 'Книга номер 2'
        book_genre = self.collector.genre[0]
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, book_genre)
        self.collector.add_book_in_favorites(book_name)
        assert self.collector.favorites[0] == book_name

    def test_delete_book_from_favorites_success(self):
        book_name = 'Книга номер 2'
        book_genre = self.collector.genre[0]
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, book_genre)
        self.collector.add_book_in_favorites(book_name)
        self.collector.delete_book_from_favorites(book_name)
        assert len(self.collector.favorites) == 0

    def test_get_list_of_favorites_books_one_book_in_list_successful(self):
        book_name = 'Книга номер 2'
        book_genre = self.collector.genre[0]
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, book_genre)
        self.collector.add_book_in_favorites(book_name)
        assert self.collector.get_list_of_favorites_books() == [book_name]





