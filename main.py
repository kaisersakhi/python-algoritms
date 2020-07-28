from linked_list import LinkedList
from linked_list import Node
from linked_list import DoublyLinkedList
from stack import StackArray
from stack import Stack
# from test import Test
from stack_apps import ParenthesisMatching, Postfix
from queues import QueueArray, Queue


def main():
    # queues()
    trees()


def trees():
    pass


def queues():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(40)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(7)
    print(queue)


def linkedList():
    mList = LinkedList()
    mList.add(34)
    mList.add(4)
    mList.add(93)
    mList.add(7)
    mList.display()


def stacks():
    stack = Stack()
    stack.push(23)
    stack.push(2)
    stack.push(13)
    stack.push(33)
    stack.display()


if __name__ == '__main__':
    main()
