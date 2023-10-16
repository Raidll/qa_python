import random
import string

import pytest

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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('length', [1, 20, 40])
    def test_add_new_book_add_books_with_titles_of_different_lengths_successful(self, length, collector):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        collector.add_new_book(rand_string)
        assert rand_string in collector.get_books_genre()

    def test_set_book_genre_addition_of_genre_successful(self, collector):
        book_name = 'Книга 1'
        rand_genre_from_list_of_genres = collector.genre[random.randint(0, len(collector.genre) - 1)]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, rand_genre_from_list_of_genres)
        assert collector.get_book_genre(book_name) == rand_genre_from_list_of_genres

    def test_get_book_genre_search_by_valid_name_successful(self, collector):
        book_name = 'Книга 1'
        rand_genre_from_list_of_genres = collector.genre[random.randint(0, len(collector.genre) - 1)]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, rand_genre_from_list_of_genres)
        assert collector.get_book_genre(book_name) == rand_genre_from_list_of_genres

    def test_get_books_with_specific_genre_two_equals_genres_in_list_get_successful(self, collector):
        name_first_book = 'Книга номер 1'
        name_second_book = 'Книга номер 2'
        genre_for_two_books = 'Фантастика'
        expected_result = ['Книга номер 1', 'Книга номер 2']
        collector.add_new_book(name_first_book)
        collector.set_book_genre(name_first_book, genre_for_two_books)
        collector.add_new_book(name_second_book)
        collector.set_book_genre(name_second_book, genre_for_two_books)
        assert expected_result == collector.get_books_with_specific_genre(genre_for_two_books)

    def test_get_books_with_specific_genre_two_different_genres_in_list_get_successful(self, collector):
        name_first_book = 'Книга номер 1'
        name_second_book = 'Книга номер 2'
        genre_first_book = 'Фантастика'
        genre_second_book = 'Ужасы'
        expected_result = ['Книга номер 1']
        collector.add_new_book(name_first_book)
        collector.set_book_genre(name_first_book, genre_first_book)
        collector.add_new_book(name_second_book)
        collector.set_book_genre(name_second_book, genre_second_book)
        assert expected_result == collector.get_books_with_specific_genre(genre_first_book)

    def test_get_books_genre(self, collector):
        name_first_book = 'Книга номер 1'
        name_second_book = 'Книга номер 2'
        genre_first_book = 'Фантастика'
        genre_second_book = 'Ужасы'
        expected_result = {'Книга номер 1': 'Фантастика', 'Книга номер 2': 'Ужасы'}
        collector.add_new_book(name_first_book)
        collector.set_book_genre(name_first_book, genre_first_book)
        collector.add_new_book(name_second_book)
        collector.set_book_genre(name_second_book, genre_second_book)
        assert expected_result == collector.get_books_genre()

    def test_get_books_for_children_add_two_books_return_one(self, collector):
        name_book_not_for_children = 'Книга номер 1'
        genre_first_book = 'Ужасы'
        name_book_for_children = 'Книга номер 2'
        genre_second_book = 'Фантастика'
        collector.add_new_book(name_book_not_for_children)
        collector.set_book_genre(name_book_not_for_children, genre_first_book)
        collector.add_new_book(name_book_for_children)
        collector.set_book_genre(name_book_for_children, genre_second_book)
        print(collector.get_books_for_children())
        assert collector.get_books_for_children()[0] == name_book_for_children

    def test_add_book_in_favorites_name_is_not_in_favorites_list_successful(self, collector):
        book_name = 'Книга номер 2'
        book_genre = collector.genre[0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        collector.add_book_in_favorites(book_name)
        assert collector.favorites[0] == book_name

    def test_delete_book_from_favorites_success(self, collector):
        book_name = 'Книга номер 2'
        book_genre = collector.genre[0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_one_book_in_list_successful(self, collector):
        book_name = 'Книга номер 2'
        book_genre = collector.genre[0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]
