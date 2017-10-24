from week8 import *
import operator

print randList(10, 100)


def search(myList, term):

    def bSearch(myList, term, low, high):
        if high == low:
            return myList[low] == term
        mid = (low + high) // 2
        if myList[mid] == term:
            return True
        elif myList[mid] > term:
            if low == mid:
                return False
            else:
                return bSearch(myList, e, low, mid - 1)
        else:
            return bSearch(myList, e, mid + 1, high)

    if len(myList) == 0:
        return False
    else:
        return bSearch(myList, term, 0, len(myList) - 1)


def selectionSort(myList):
    suffix = 0
    while suffix != len(myList):
        for i in range(suffix, len(myList)):
            if myList[i] < myList[suffix]:
                myList[suffix], myList[i] = myList[i], myList[suffix]
        suffix += 1


def merge(left, right, compare):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j+=1

    return result

def mergeSort(myList, compare = operator.lt):

    if len(mylist) < 2:
        return myList[:]
    else:
        middle = len(myList)//2
        left = mergeSort(myList[:middle], compare)
        right = mergeSort(myList[middle:], compare)
        return merge(left, right, compare)
