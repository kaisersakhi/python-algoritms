# first i will write n^2 sorts
"""
    for basic understanding im using simple builtin list;
    i would have chosen linked list but concept is more important here not the implementation with different structures .
    OWNER :- KAISER SAKHI -> i donno y i keep writing this :)
    :because of the entrance exam prepration i thought i should write this module after exam but im doing it now;;
"""


def bubbleSort(mList):
    size = len(mList)
    if size > 1:
        for i in range(size - 1):
            for j in range(size - 1 - i):
                if mList[j] > mList[j + 1]:
                    # a , b = b ,a
                    mList[j], mList[j + 1] = mList[j + 1], mList[j]

    """
        Bubble sort is basic sorting algorithm which sorts a list in n square time 
        bubble sort is adaptive and stable
        bubble sort can do k passes:
            k passes means if we want to perform "k" iteration on list and can find largest or smallest not all n iterations
                while k < n -1 
                
        bubble s. is not useful when working with linked list
        
        Note stable means : keeping the order of the list
        adaptive means if the list is already sorted then the algorithm should take minimum time
    """


def insertionSort(mList):
    size = len(mList)
    if size > 1:
        for i in range(1, size):
            x = mList[i]
            j = i - 1
            while j != -1 and mList[j] > x:
                mList[j + 1] = mList[j]
                j -= 1
            mList[j + 1] = x
    """
            time complexity of insertion sort in worst case | average case is O(n^2) 
            best case is O(n) if the list is already sorted , so insertion sort is adaptive
            insertion sort is not useful if we want k passes
    """


def selectionSort(mList):
    size = len(mList)

    def minimum(frm):
        m1 = frm
        for x1 in range(frm, size):
            if mList[m1] > mList[x1]:
                m1 = x1
        return m1

    for x in range(size):
        m = minimum(x)
        mList[x], mList[m] = mList[m], mList[x]

    """
        selection sort is also simple sorting algorithm which sort a list in O (n ^ 2) time 
        this , is not  adaptive and  stable
        
    """


"""    
    till now all above all three sorting algorithms are comparison based sorting algrithm
    and sort a list in O(n^2) time
"""


def quickSort(mList, randomize=False):
    size = len(mList)
    if size > 1:

        def partition(l, h):
            pivot = mList[h]
            j = l

            for i in range(l, h):
                if mList[i] <= pivot:
                    mList[i], mList[j] = mList[j], mList[i]
                    j += 1
            mList[j], mList[h] = mList[h], mList[j]
            return j

        def sort(low, high):
            if low < high:
                partitionPoint = partition(low, high)
                sort(low, partitionPoint-1)
                sort(partitionPoint, high)

        sort(0, size - 1)

        """
            DATE :-  15-AUG-2020
            this it for the time , i have entrace test near 
            after entrance test i will work on this again INSHALLAH
        """
