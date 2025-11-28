def bubble_sort(a: list, key=None, cmp=None) -> list:
    if a is None:
        raise ValueError("Список не может быть None")

    if not a:
        return []

    if key is not None and not callable(key):
        raise ValueError("Аргумент key должен быть функцией или None")

    if cmp is not None and not callable(cmp):
        raise ValueError("Аргумент cmp должен быть функцией или None")

    arr = a.copy()
    n = len(arr)

    def compare(x, y):
        if cmp is not None:
            return cmp(x, y)

        x_val = key(x) if key else x
        y_val = key(y) if key else y

        try:
            if x_val < y_val:
                return -1
            elif x_val > y_val:
                return 1
            else:
                return 0
        except TypeError as e:
            raise TypeError(f"Невозможно сравнить {x_val} и {y_val}: {e}")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparison = compare(arr[j], arr[j + 1])
            if comparison > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def quick_sort(a: list, key=None, cmp=None) -> list:
    if a is None:
        raise ValueError("Список не может быть None")
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")

    if len(a) <= 1:
        return a.copy()

    if key is not None and not callable(key):
        raise TypeError("key должен быть callable или None")
    if cmp is not None and not callable(cmp):
        raise TypeError("cmp должен быть callable или None")

    def compare(x, y):
        if cmp:
            return cmp(x, y)
        x_val = key(x) if key else x
        y_val = key(y) if key else y

        try:
            if x_val < y_val: return -1
            if x_val > y_val: return 1
            return 0
        except TypeError as e:
            raise TypeError(f"Невозможно сравнить {x_val} и {y_val}: {e}")

    arr = a.copy()

    def _partition(lst, low, high):
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            try:
                if compare(lst[j], pivot) <= 0:
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
            except Exception as e:
                raise RuntimeError(f"Ошибка при сравнении элементов: {e}")

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    def _quick_sort(lst, low, high):
        if low < high:
            pi = _partition(lst, low, high)
            _quick_sort(lst, low, pi - 1)
            _quick_sort(lst, pi + 1, high)
    try:
        _quick_sort(arr, 0, len(arr) - 1)
        return arr
    except Exception as e:
        raise RuntimeError(f"Ошибка в быстрой сортировке: {e}")


def counting_sort(a: list, key=None, cmp=None) -> list:

    if a is None:
        raise ValueError("Список не может быть None")
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")

    if not a:
        return a.copy()

    if key is not None and not callable(key):
        raise TypeError("key должен быть callable или None")

    try:
        if key:
            arr = [key(x) for x in a]
        else:
            arr = a.copy()

        for i, elem in enumerate(arr):
            if not isinstance(elem, (int, float)):
                raise TypeError(f"Элемент {elem} не является числом")

        if min(arr) < 0:
            raise ValueError("Counting sort работает только для неотрицательных чисел")

        max_val = max(arr)
        min_val = min(arr)
        count = [0] * (max_val - min_val + 1)

        for num in arr:
            count[num - min_val] += 1

        result = []
        for i in range(len(count)):
            result.extend([i + min_val] * count[i])

        if key:
            key_to_elements = {}
            for elem in a:
                k = key(elem)
                if k not in key_to_elements:
                    key_to_elements[k] = []
                key_to_elements[k].append(elem)

            final_result = []
            for k in result:
                if key_to_elements[k]:
                    final_result.append(key_to_elements[k].pop(0))
            return final_result

        return result
    except Exception as e:
        raise RuntimeError(f"Ошибка в сортировке подсчетом: {e}")


def radix_sort(a: list, base: int = 10, key=None, cmp=None) -> list:
    if a is None:
        raise ValueError("Список не может быть None")
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not isinstance(base, int) or base <= 0:
        raise ValueError("base должен быть положительным целым числом")

    if not a:
        return a.copy()

    if key is not None and not callable(key):
        raise TypeError("key должен быть callable или None")

    try:
        if key:
            arr = [key(x) for x in a]
        else:
            arr = a.copy()

        for i, elem in enumerate(arr):
            if not isinstance(elem, int):
                raise TypeError(f"Элемент {elem} не является целым числом")

        if min(arr) < 0:
            raise ValueError("Radix sort работает только для неотрицательных чисел")

        max_num = max(arr)
        exp = 1

        while max_num // exp > 0:
            arr = _counting_sort_for_radix(arr, exp, base)
            exp *= base

        if key:
            key_to_elements = {}
            for elem in a:
                k = key(elem)
                if k not in key_to_elements:
                    key_to_elements[k] = []
                key_to_elements[k].append(elem)

            final_result = []
            for k in arr:
                if key_to_elements[k]:
                    final_result.append(key_to_elements[k].pop(0))
            return final_result

        return arr
    except Exception as e:
        raise RuntimeError(f"Ошибка в поразрядной сортировке: {e}")


def _counting_sort_for_radix(arr, exp, base):
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    return output


def bucket_sort(a: list[float], buckets: int | None = None, key=None, cmp=None) -> list[float]:
    if a is None:
        raise ValueError("Список не может быть None")
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if buckets is not None and (not isinstance(buckets, int) or buckets <= 0):
        raise ValueError("buckets должен быть положительным целым числом или None")

    if not a:
        return a.copy()

    if key is not None and not callable(key):
        raise TypeError("key должен быть callable или None")
    if cmp is not None and not callable(cmp):
        raise TypeError("cmp должен быть callable или None")

    try:
        if key:
            arr = [key(x) for x in a]
        else:
            arr = a.copy()

        for i, elem in enumerate(arr):
            if not isinstance(elem, (int, float)):
                raise TypeError(f"Элемент {elem} не является числом")

        n = len(arr)
        if buckets is None:
            buckets = n

        bucket_list = [[] for _ in range(buckets)]

        for num in arr:
            if num < 0 or num >= 1:
                raise ValueError("Bucket sort ожидает числа в диапазоне [0, 1)")
            index = int(num * buckets)
            if index == buckets:
                index = buckets - 1
            bucket_list[index].append(num)

        for bucket in bucket_list:
            if cmp:
                _sort_bucket_with_cmp(bucket, cmp)
            else:
                try:
                    bucket.sort()
                except TypeError as e:
                    raise TypeError(f"Невозможно отсортировать ведро: {e}")

        sorted_keys = []
        for bucket in bucket_list:
            sorted_keys.extend(bucket)

        if key:
            key_to_elements = {}
            for elem in a:
                k = key(elem)
                if k not in key_to_elements:
                    key_to_elements[k] = []
                key_to_elements[k].append(elem)

            final_result = []
            for k in sorted_keys:
                if key_to_elements[k]:
                    final_result.append(key_to_elements[k].pop(0))
            return final_result

        return sorted_keys
    except Exception as e:
        raise RuntimeError(f"Ошибка в ведерной сортировке: {e}")


def _sort_bucket_with_cmp(bucket, cmp):
    n = len(bucket)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            try:
                if cmp(bucket[j], bucket[j + 1]) > 0:
                    bucket[j], bucket[j + 1] = bucket[j + 1], bucket[j]
                    swapped = True
            except Exception as e:
                raise RuntimeError(f"Ошибка при сравнении в ведре: {e}")
        if not swapped:
            break


def heap_sort(a: list, key=None, cmp=None) -> list:

    if a is None:
        raise ValueError("Список не может быть None")
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")

    if not a:
        return a.copy()

    if key is not None and not callable(key):
        raise TypeError("key должен быть callable или None")
    if cmp is not None and not callable(cmp):
        raise TypeError("cmp должен быть callable или None")

    try:
        arr = a.copy()
        n = len(arr)

        def compare(x, y):
            if cmp:
                return cmp(x, y)
            x_val = key(x) if key else x
            y_val = key(y) if key else y

            try:
                if x_val < y_val: return -1
                if x_val > y_val: return 1
                return 0
            except TypeError as e:
                raise TypeError(f"Невозможно сравнить {x_val} и {y_val}: {e}")

        def _heapify(lst, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                try:
                    if compare(lst[left], lst[largest]) > 0:
                        largest = left
                except Exception as e:
                    raise RuntimeError(f"Ошибка сравнения слева: {e}")

            if right < n:
                try:
                    if compare(lst[right], lst[largest]) > 0:
                        largest = right
                except Exception as e:
                    raise RuntimeError(f"Ошибка сравнения справа: {e}")

            if largest != i:
                lst[i], lst[largest] = lst[largest], lst[i]
                _heapify(lst, n, largest)

        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            _heapify(arr, i, 0)

        return arr
    except Exception as e:
        raise RuntimeError(f"Ошибка в пирамидальной сортировке: {e}")