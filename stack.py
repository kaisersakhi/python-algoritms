from linked_list import Node


class StackArray:
    top = 0
    arr = None
    size = None

    def __init__(self, n=None):
        self.size = 0
        self.arr = []
        self.top = -1

    def push(self, data):
        # self.arr = []
        top = type(self.top)
        self.arr.append(data)
        self.top = self.top + 1
        self.size = self.size + 1

    def pop(self):
        if not self.top < 0:
            val = self.arr[self.top]
            self.top = self.top - 1
            self.size = self.size - 1

    def display(self):
        if not self.top < 0:
            for x in reversed(range(self.top + 1)):
                print("|____" + str(self.arr[x]) + "____|")


class Stack:
    top = None
    size = None

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
            self.size = self.size + 1
        else:
            node.next = self.top
            self.top = node
            self.size = self.size + 1

    def pop(self):
        popped_val = -1
        if self.top is not None and not self.size < 0:
            current = self.top
            self.top = current.next
            popped_val = current.data
            self.size = self.size - 1
            del current
        return popped_val

    def peek(self, position):
        if 0 <= position < self.size:
            current = self.top
            for _ in range(position):
                current = current.next

            return current.data

    def display(self):
        current = self.top

        for _ in range(self.size):
            print("[____" + str(current.data) + "____]\n")
            current = current.next

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def topMost(self):
        if self.top is not None:
            return self.top.data
