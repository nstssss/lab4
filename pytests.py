import pytest

from tasks.task1 import Task1, STEP
from tasks.task2 import Task2
from tasks.task3 import Task3

""" Проверка класса Task1"""
class Test_task1:
    # проверка возращения нужного количества значений
    def test_get_values_count(self):
        task = Task1(start=0, end=100, n=10)
        values = task.get_values()

        assert len(values) == 10
    # проверка корректности значений генератора
    def test_get_values_correct_math(self):
        task = Task1(start=0, end=1, n=3)
        values = task.get_values()
        for i, val in enumerate(values):
            x = i * STEP
            expected = 0.5 * x - 2
            assert val == pytest.approx(expected)

    # проверка корректности первого значения генератора
    def test_generator_first_value(self):
        task = Task1(start=0, end=1, n=5)
        g = task.generator()

        first_value = next(g)
        expected = 0.5 * 0 - 2  # f(0)

        assert first_value == pytest.approx(expected)

    def test_generator_end_limit(self):
        task = Task1(start=0, end=0.03, n=10)
        g = list(task.generator())

        assert len(g) == 4
""" Проверка класса Task2"""
class Test_task2:
    # проврека количества комбинаций генератора
    def test_generator_count(self):
        task = Task2(start=1, end=4, n=5)
        gen = task.generator()
        assert len(gen) == 27

    # проверка количесьва возвращаемых значений
    def test_get_values_length(self):
        task = Task2(start=1, end=5, n=7)
        results = task.get_values()
        assert len(results) == 7

    # проверка корректности первой тройки значений генератора
    def test_generator_first_value(self):
        task = Task2(start=2, end=5, n=5)
        gen = task.generator()
        assert gen[0] == (2, 2, 2)

    # проверка корректности образования треугольника из длин сторон
    def test_triangle_false(self):
        """Отрицательный тест: 1, 2, 10 — не треугольник."""
        task = Task2(1, 10, 1)
        task2 = Task2(1, 10, 3)
        assert task.triangle((1, 2, 10)) is False
        assert task2.triangle((2, 3, 4)) is True

""" Проверка класcf Task3"""
class Test_task3:
    # проверка корректности нахождения n максимальных чисел
    def test_write_max(self):
        t1 = Task3("1 2 3 4 5 6 7 8 9", 4)
        t2 = Task3("11 22 33 44 55 66", 4)
        t3 = Task3("678 323 9876 238 421", 4)

        res1 = t1.write_max()
        res2 = t2.write_max()
        res3 = t3.write_max()

        assert res1 == [9, 8, 7, 6]
        assert res2 == [66, 55, 44, 33]
        assert res3 == [9876, 678, 421, 323]

    # проверка корректности нахождения максимальных значений с дубликатами
    def test_write_max_duplicates(self):
        task = Task3("5 5 5 3 3 10", 3)
        result = task.write_max()
        assert result == [10, 5, 3]

    # проверка нахождения, если чисел меньше чем n
    def test_write_max_less_than_four(self):
        task = Task3("8 2", 4)
        result = task.write_max()
        assert result == [8, 2]