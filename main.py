from linked_list import LinkedList
from linked_list import Node
from linked_list import DoublyLinkedList
from stack import StackArray
from stack import Stack
# from test import Test
from stack_apps import ParenthesisMatching, Postfix
from queues import QueueArray, Queue
from trees import BinaryTree
from sorts import bubbleSort, insertionSort, selectionSort, quickSort

"""
/*
    Note : This code is not written by a CS professional but a CS Grad. i hosted this code on github because i wannted to get
            taste of git , the code is totally written in simple way possible . if you're learning data structures and algorithms ,
            this might be useful for you.
            :this code is highly infulanced by { Abdul Bari (Great Teacher) }
                    link of his youtube channel : https://www.youtube.com/channel/UCZCFT11CWBi3MHNlGf019nw

             if you find this code helpful in anyway than probally you should star it.
             
             if u like statically typed then checkout my java version right here on github ;)
             
             im working on java and python side by side;
             
 */
"""


def main():
    # queues()
    # trees()
    mList = [10, 5, 8, 3, 15, 6, 12, 4]
    # bubbleSort/(mList)
    # insertionSort(mList)
    # selectionSort(mList)

    print(quickSort(mList))
    print(mList)


def trees():
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(45)
    tree.add(5)
    tree.levelOrder()
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
