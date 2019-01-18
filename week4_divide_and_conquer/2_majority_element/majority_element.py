# Uses python3
import sys

def get_majority_naive(a):
    length = len(a)
    for i in range(length):
        current = a[i]
        count = 0
        for j in range(length):
            if a[j] == current:
                count +=1
        if count>length/2:
            return a[i]
    return -1

def get_majority_element(a, left, right):
    #print('a:',a)
    #print('left:',left)
    #print('right:', right)
    #import pdb; pdb.set_trace()
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = right//2
    b = a[:mid]
    c = a[mid:]
    lenb = mid
    lenc = right - mid
    B = get_majority_element(b, 0, lenb)
    C = get_majority_element(c, 0, lenc)
    if B != -1:
        count = 0
        for aa in a:
            if aa == B:
                count +=1
        if count > right/2:
            return B
    if C != -1:
        count = 0
        for aa in a:
            if aa == C:
                count +=1
        if count > right/2:
            return C

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
