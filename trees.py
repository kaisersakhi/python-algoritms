from queues import Queue


class Node:
    data = None
    lchild = None
    rchild = None

    def __init__(self, data):
        self.data = data


class BinaryTree:
    root = None
    # size : keeps track of no. of nodes and nothing else
    size = None
    queue = None

    def __init__(self):
        self.size = 0
        self.queue = Queue()

    def add(self, data):
        node = Node(data)
        # self.queue.enqueue(node)
        if self.root is None:
            self.root = node
            self.size += 1
            self.queue.enqueue(self.root)
        elif not self.queue.isEmpty():
            front = self.queue.front()
            if front.lchild is None:
                front.lchild = node
            else:
                front.rchild = node
                self.queue.dequeue()
            self.queue.enqueue(node)
            self.size += 1

    def preOrder(self):

        def r(node):
            if node is None:
                return
            print(node.data)
            r(node.lchild)
            r(node.rchild)
            pass
        r(self.root)

    def levelOrder(self):
        if self.size > 0:
            queue = Queue()
            queue.enqueue(self.root)

            while not queue.isEmpty():
                print(queue.front().data)
                queue.dequeue()
            pass
        pass
