class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedListQueue:

    def __init__(self):
        self.head = None  # Первый элемент
        self.tail = None  # Последний элемент
        self.size = 0     # Количество элементов

    def enqueue(self, x: int) -> None: #Добавить элемент в конец очереди
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self) -> int: #Удалить и вернуть первый элемент. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return val

    def front(self) -> int: #Получить значение первого элемента без удаления. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("front из пустой очереди")
        return self.head.val

    def is_empty(self) -> bool: #Проверить, пуста ли очередь
        return self.size == 0

    def __len__(self) -> int: #Вернуть количество элементов в очереди
        return self.size


class ListQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, x: int) -> None: #Добавить элемент в конец очереди
        self.data.append(x)

    def dequeue(self) -> int: #Удалить и вернуть первый элемент. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        return self.data.pop(0)

    def front(self) -> int: #Получить значение первого элемента без удаления. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("front из пустой очереди")
        return self.data[0]

    def is_empty(self) -> bool: #Проверить, пуста ли очередь
        return len(self.data) == 0

    def __len__(self) -> int: #Вернуть количество элементов в очереди
        return len(self.data)


class StackQueue: #Очередь, реализованная на двух стеках

    def __init__(self):
        self.in_stack = []  # Для добавления
        self.out_stack = []  # Для извлечения

    def enqueue(self, x: int) -> None: #Добавить элемент в конец очереди
        self.in_stack.append(x)

    def dequeue(self) -> int: #Удалить и вернуть первый элемент. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def front(self) -> int: #Получить значение первого элемента без удаления. Выбрасывает IndexError если очередь пуста
        if self.is_empty():
            raise IndexError("front из пустой очереди")
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def is_empty(self) -> bool: #Проверить, пуста ли очередь."""
        return not self.in_stack and not self.out_stack

    def __len__(self) -> int: #Вернуть количество элементов в очереди
        return len(self.in_stack) + len(self.out_stack)