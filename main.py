from linked_list import LinkedList
from linked_list import Node
from linked_list import DoublyLinkedList
from stack import StackArray
from stack import Stack
# from test import Test
from stack_apps import ParenthesisMatching, Postfix
from queues import QueueArray , Queue


def main():
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(40)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(7)


    for _ in range(3):
        print("dequeue: ")
        print(queue.dequeue())

    print("*******************************\n" + "len = " + str(queue.length()))
    queue.display()
    # mQueue = QueueArray()
    # mQueue.enqueue(4)
    # mQueue.enqueue(2)
    # # mQueue.enqueue(9)
    # # mQueue.enqueue(6)
    # mQueue.dequeue()
    # mQueue.dequeue()
    # mQueue.enqueue(2)
    # mQueue.display()
    # expression = Postfix("2-3*6+8/9-3")
    # print(expression.eval())

    # exp = "{()(a+b)*[2(a*b)]}"
    # expMatching = ParenthesisMatching(exp)
    # print(expMatching.match())
    # stack = Stack()
    # stack.push(5)
    # stack.push(4)
    # stack.push(3)
    # stack.push(2)
    # stack.push(1)
    # print("Popped :-> "+str(stack.pop())+"Peek(3) "+str(stack.peek(4)))
    # stack.display()

    # dList = DoublyLinkedList()
    # dList.add(5)
    # dList.add(4)
    # dList.add(3)
    # dList.add(2)
    # dList.add(1)
    # # dList.insert(val=89, index=2)
    # val = dList.remove(index=0)
    # dList.display()
    #
    # print("--->"+str(val)+" has been deleted;")
    # dList.reverseDisplay()


if __name__ == '__main__':
    main()
