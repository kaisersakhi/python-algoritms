from linked_list import Node


class QueueArray:
    front = None
    rear = None
    size = None
    queue = None

    def __init__(self):
        self.size = 0
        self.queue = []

    def enqueue(self, data):
        if self.size == 0:
            self.front = self.rear = 0
            self.queue.append(data)
            self.size = self.size + 1
        else:
            self.rear = self.rear + 1
            self.queue.insert(self.rear, data)
            self.size = self.size + 1

    def dequeue(self):
        val = None
        if not self.isEmpty():
            val = self.queue[self.front]
            self.front = self.front + 1
        return val

    def isEmpty(self):
        if self.front > self.rear:
            self.front = self.rear = None
            return True

    def display(self):
        if not self.isEmpty():
            for x in range(self.front, self.size):
                print(str(self.queue[x]) + "\n")
        pass


class Queue:
    # _queue = None
    _size = None
    _front = None
    _rear = None

    def __init__(self):
        self._size = 0

    def enqueue(self, data):
        node = Node(data)

        if self._front is None:
            self._front = self._rear = node
            self._size = self._size + 1
        else:
            self._rear.next = node
            self._rear = node
            self._size = self._size + 1

    def dequeue(self):
        val = None
        if self._size > 0:
            current = self._front
            val = current.data
            self._front = current.next
            del current
            self._size = self._size - 1
        return val

    def display(self):
        if self._size > 0:
            current = self._front
            for _ in range(self._size):
                print(current.data)
                current = current.next

    def length(self):
        return self._size

    def isEmpty(self):
        if self._size <= 0:
            return True
        return False

    def __str__(self):
        data = []
        current = self._front
        for _ in range(self._size):
            data.append(current.data)
            current = current.next
        return str(data)

