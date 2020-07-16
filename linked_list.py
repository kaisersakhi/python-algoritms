"""
Created By : Kaiser Sakhi Bhat : Date 08-07-2020
this code is Released under MIT licence : Youre free to use it in you project
but before you do that let me clarify this , i think this code is only for learning and if u use it in your project then u might be dumb
i thought python sucks but feels good , i was java lover and still am;
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


head_rev = None


def revRecursion(current, previous=None):
    if current is not None:
        revRecursion(previous=current, current=current.next)
        current.next = previous
    else:
        global head_rev
        head_rev = previous


class LinkedList:
    head = None
    size = None
    isSorted = None

    def __init__(self):
        self.size = 0
        self.isSorted = True

    def add(self, n, at=None):
        # add() : will add at the end of the list but with at , will insert in a desired position;
        node = Node(n)
        node.next = None

        self.isSorted = False
        # check:- if at is not null that means instance hasn't specified the position
        # and check if size is greater then 0 otherwise it would same
        # and check if at is less than size otherwise it would be invalid index to insert into and "at" is out of range

        if at is not None and self.size > 0 and at < self.size - 1:
            self.size = self.size + 1
            # Case: when the list is not empty and 'at' position is first node
            if at == 0:
                # store the head node to the newNode of next
                node.next = self.head
                # and then store the newNode into head : that is it
                self.head = node
            else:
                # if the case is not the first element
                # create a temp and make it point to the head
                temp = self.head
                # get to the index : or : index is actually the position where the element should be inserted
                # at= index : [AFTER HOW MANY NODE SHOULD NEW NODE BE INSERTED] = at

                # this for loop will
                # loop will run form 0 to 'at'-1
                for _ in range(at - 1):
                    # essentially this loop counts the element till 'at' and at the end the temp will contain the node
                    # whose next node will be new node
                    temp = temp.next

                # make new node point to temp.next
                node.next = temp.next
                # make temp.next point to node
                temp.next = node
        else:
            # else if 'at' is not mentioned than insert new node to the end of the list
            self.size = self.size + 1
            # At first list will be empty then , head will directly point to the new node
            if self.head is None:
                self.head = node
            else:
                # if list is not empty then , create temp and make it point to the head
                temp = self.head
                # from head get to the last node
                while temp.next is not None:
                    temp = temp.next
                # temp is pointing to last node , now make its next point to the new node
                temp.next = node
                # that is it ;)

    def display(self):
        if self.head is not None:
            temp = self.head

            while temp is not None:
                print(str(temp.data) + "\n")
                temp = temp.next

    def linearSearch(self, key):
        temp = self.head
        counter = 0
        while temp is not None:
            counter = counter + 1
            if temp.data is key:
                return counter
                # print(str(key) + " found at "+ str(counter) +" Position.\n")
                # return
            temp = temp.next
        return -1

    def remove(self, keyElement):
        temp = self.head
        position = self.linearSearch(keyElement)
        if position == -1:
            return False
        if position == 1:
            temp = self.head
            temp_p = temp.next
            self.head = temp_p
            del temp
            self.size = self.size - 1
            return True
        else:

            for _ in range(position):
                temp_p = temp
                temp = temp.next
                if temp.data == keyElement:
                    # store the  ........-->|previousNode or temp_p| -->  |temp or current | --> |next node or temp.next| --> .........
                    # in previous of next store temp.next  ^_____________________________________________________^
                    temp_p.next = temp.next
                    # make temp || current node.next null | actually this is ineffective
                    temp.next = None
                    # and finally delete the instance of temp or current  node
                    del temp
                    self.size = self.size - 1
                    return True

    def addInSorted(self, n):

        """
        this method will add new node in its sorted position only if the list is sorted otherwise , the element
        will be added at the end of the list without considering the sort property
        :param n:
        :return:
        """
        # as usual create a new node
        newNode = Node(n)

        if self.head is None or not (self.isSorted):
            self.add(n)
            self.isSorted = True
            return

        current = self.head
        previous = None

        if n < current.data:
            newNode.next = self.head
            self.head = newNode
            self.size = self.size + 1
            return

        while current.data < n and current is not None:
            previous = current
            if current.next is None:
                current.next = newNode
                self.size = self.size + 1
                return
            current = current.next

        newNode.next = current
        previous.next = newNode
        self.size = self.size + 1
        # print("previous = "+ str(previous.data)+"\n" +"curren = "+str(current.data))

    def reverseLinks(self):
        if self.head is not None and self.size > 1:
            past = None
            present = None
            future = self.head

            while future is not None:
                past = present
                present = future
                future = future.next
                present.next = past

            self.head = present

    def revLinksRecursion(self):
        current = self.head
        revRecursion(current=current)
        if head_rev is not None:
            self.head = head_rev


class DoublyLinkedList:
    head = None
    tail = None
    size = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)

        if self.head is None:
            self.head = self.tail = node
            self.size = self.size + 1
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self.size = self.size + 1

    def display(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(str(current.data) + "\n")
                current = current.next

    def reverseDisplay(self):
        if self.head is not None:
            current = self.tail
            while current is not None:
                print(str(current.data) + "\n")
                current = current.previous

    def insert(self, val, index):
        if self.head is None or index >= self.size or index < 0:
            self.add(val=val)
            return
        node = Node(val)
        if index == 0:
            current = self.head
            node.next = current
            current.previous = node
            self.head = node
            self.size = self.size + 1
        elif index > 0:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            tempNext = current.next
            node.next = tempNext
            node.previous = current
            current.next = node
            tempNext.previous = node
            self.size = self.size + 1
            return

    def remove(self, index):
        if 0 <= index < self.size:
            current = self.head
            val = current.data
            if index == 0:
                # index is 0 delete the head
                tempNext = current.next
                tempNext.previous = None
                self.head = tempNext
                del current
                self.size = self.size - 1
                return val
            else:
                for _ in range(index):
                    current = current.next
                val = current.data
                tempPre = current.previous
                tempNext = current.next
                if tempNext is not None:
                    tempNext.previous = tempPre
                tempPre.next = tempNext
                del current
                self.size = self.size - 1
                return val
