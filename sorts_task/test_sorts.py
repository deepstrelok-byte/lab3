import pytest
from sorts import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort


class TestBubbleSort: #Тесты для пузырьковой сортировки

    def test_basic_sort(self):
        assert bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([5]) == [5]

    def test_already_sorted(self):
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_with_key(self):
        # Bubble sort может работать с любыми типами через key
        students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
        result = bubble_sort(students, key=lambda x: x[1])
        assert result == [("Charlie", 78), ("Alice", 85), ("Bob", 92)]

    def test_with_cmp(self):
        def reverse_cmp(a, b):
            if a < b: return 1
            if a > b: return -1
            return 0

        assert bubble_sort([3, 1, 4, 1, 5], cmp=reverse_cmp) == [5, 4, 3, 1, 1]

    def test_none_input(self):
        with pytest.raises(ValueError, match="Список не может быть None"):
            bubble_sort(None)

    def test_invalid_key(self):
        with pytest.raises(ValueError, match="Аргумент key должен быть функцией или None"):
            bubble_sort([1, 2, 3], key="not_callable")

    def test_invalid_cmp(self):
        with pytest.raises(ValueError, match="Аргумент cmp должен быть функцией или None"):
            bubble_sort([1, 2, 3], cmp="not_callable")


class TestQuickSort: #Тесты для быстрой сортировки

    def test_basic_sort(self):
        assert quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_with_key(self):
        # Quick sort может работать с любыми типами через key
        students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
        result = quick_sort(students, key=lambda x: x[1])
        assert [x[1] for x in result] == [78, 85, 92]  # Проверяем только значения

    def test_with_cmp(self):
        def reverse_cmp(a, b):
            if a < b: return 1
            if a > b: return -1
            return 0

        result = quick_sort([3, 1, 4, 1, 5], cmp=reverse_cmp)
        assert result == [5, 4, 3, 1, 1]

    def test_large_list(self):
        import random
        arr = [random.randint(1, 1000) for _ in range(100)]
        sorted_arr = quick_sort(arr)
        assert sorted_arr == sorted(arr)


class TestCountingSort: #Тесты для сортировки подсчетом

    def test_basic_sort(self):
        assert counting_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert counting_sort([]) == []

    def test_with_key_for_numbers(self):
        # Counting sort работает только с числами, даже через key
        numbers = [3, 1, 4, 1]
        result = counting_sort(numbers, key=lambda x: x)  # key возвращает числа
        assert result == [1, 1, 3, 4]

    def test_negative_numbers(self):
        with pytest.raises((ValueError, RuntimeError)):
            counting_sort([1, -2, 3])

    def test_non_numeric_elements(self):
        with pytest.raises((TypeError, RuntimeError)):
            counting_sort([1, "2", 3])

    def test_key_returns_non_number(self):
        # Если key возвращает не-число - должна быть ошибка
        with pytest.raises((TypeError, RuntimeError)):
            counting_sort([1, 2, 3], key=lambda x: str(x))


class TestRadixSort: #Тесты для поразрядной сортировки

    def test_basic_sort(self):
        assert radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_empty_list(self):
        assert radix_sort([]) == []

    def test_with_key_for_integers(self):
        # Radix sort работает только с целыми числами, даже через key
        numbers = [170, 45, 75, 90]
        result = radix_sort(numbers, key=lambda x: x)  # key возвращает целые числа
        assert result == [45, 75, 90, 170]

    def test_different_base(self):
        assert radix_sort([5, 3, 1, 4, 2], base=2) == [1, 2, 3, 4, 5]

    def test_negative_numbers(self):
        with pytest.raises((ValueError, RuntimeError)):
            radix_sort([1, -2, 3])

    def test_non_integer_elements(self):
        with pytest.raises((TypeError, RuntimeError)):
            radix_sort([1, 2.5, 3])

    def test_key_returns_non_integer(self):
        # Если key возвращает не-целое число - должна быть ошибка
        with pytest.raises((TypeError, RuntimeError)):
            radix_sort([1, 2, 3], key=lambda x: x + 0.5)


class TestBucketSort: #Тесты для ведерной сортировки

    def test_basic_sort(self):
        arr = [0.5, 0.2, 0.8, 0.1, 0.9]
        result = bucket_sort(arr)
        expected = sorted(arr)
        assert result == expected

    def test_empty_list(self):
        assert bucket_sort([]) == []

    def test_with_key_for_numbers(self):
        # Bucket sort работает только с числами [0,1), даже через key
        arr = [0.5, 0.2, 0.8]
        result = bucket_sort(arr, key=lambda x: x)  # key возвращает числа
        assert result == [0.2, 0.5, 0.8]

    def test_out_of_range_numbers(self):
        with pytest.raises((ValueError, RuntimeError)):
            bucket_sort([1.5, 0.2, 0.8])

    def test_custom_buckets(self):
        arr = [0.1, 0.9, 0.5, 0.2, 0.8]
        result = bucket_sort(arr, buckets=3)
        assert result == sorted(arr)

    def test_key_returns_out_of_range(self):
        # Если key возвращает числа вне [0,1) - должна быть ошибка
        with pytest.raises((ValueError, RuntimeError)):
            bucket_sort([0.1, 0.2, 0.3], key=lambda x: x + 1.0)


class TestHeapSort: #Тесты для пирамидальной сортировки

    def test_basic_sort(self):
        assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_empty_list(self):
        assert heap_sort([]) == []

    def test_with_key(self):
        # Heap sort может работать с любыми типами через key
        students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
        result = heap_sort(students, key=lambda x: x[1])
        assert result == [("Bob", 20), ("Alice", 25), ("Charlie", 30)]

    def test_with_cmp(self):
        def reverse_cmp(a, b):
            if a < b: return 1
            if a > b: return -1
            return 0

        result = heap_sort([3, 1, 4, 1, 5], cmp=reverse_cmp)
        assert result == [5, 4, 3, 1, 1]

    def test_complex_objects(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __repr__(self):
                return f"Person({self.name}, {self.age})"

        people = [Person("Alice", 25), Person("Bob", 20), Person("Charlie", 30)]
        result = heap_sort(people, key=lambda p: p.age)
        assert [p.age for p in result] == [20, 25, 30]


class TestAllSortsComparison: #Тесты для сравнения всех алгоритмов сортировки

    def test_all_sorts_same_result_for_numbers(self):
        test_data = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(test_data)

        assert bubble_sort(test_data) == expected
        assert quick_sort(test_data) == expected
        assert counting_sort(test_data) == expected
        assert radix_sort(test_data) == expected
        assert heap_sort(test_data) == expected

    def test_all_sorts_with_numeric_key(self):
        test_data = [64, 34, 25, 12, 22, 11, 90]
        expected = sorted(test_data)

        # Все сортировки должны работать с numeric key
        assert bubble_sort(test_data, key=lambda x: x) == expected
        assert quick_sort(test_data, key=lambda x: x) == expected
        assert counting_sort(test_data, key=lambda x: x) == expected
        assert radix_sort(test_data, key=lambda x: x) == expected
        assert heap_sort(test_data, key=lambda x: x) == expected


class TestUniversalSorts: #Тесты для сортировок, которые работают с любыми типами

    def test_universal_sorts_with_strings(self):
        test_data = ["banana", "apple", "cherry"]
        expected = sorted(test_data)

        # Эти сортировки могут работать со строками
        assert bubble_sort(test_data) == expected
        assert quick_sort(test_data) == expected
        assert heap_sort(test_data) == expected

    def test_universal_sorts_with_tuples(self):
        test_data = [("b", 2), ("a", 1), ("c", 3)]
        expected = sorted(test_data)

        assert bubble_sort(test_data) == expected
        assert quick_sort(test_data) == expected
        assert heap_sort(test_data) == expected