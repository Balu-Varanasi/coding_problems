import sys


def binary_search(seq, e):
    """
    returns the position of a specified element "e"
    within a sorted sequence 'seq'.
    """
    left, right = 0, len(seq) - 1
    while 1:
        if right < left:
            return -1
        mid = (left + right) / 2
        if seq[mid] < e:
            left = mid + 1
        elif seq[mid] > e:
            right = mid - 1
        else:
            return mid


if __name__ == '__main__':
    seq, e = range(3, 100), 4
    print binary_search(seq, e)
