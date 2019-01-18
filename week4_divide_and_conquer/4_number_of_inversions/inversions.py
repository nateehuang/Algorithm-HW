# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    b = a[:]
    i = left
    j = ave
    k = left
    while i < ave:
        if b[i]>b[j]:
            number_of_inversions += ave - i
            a[k] = b[j]
            j += 1
        else:
            a[k] = b[i]
            i +=1
        k += 1
        if j == right:
            a[k:right] = b[i:ave]
            break
    #print('b:', b[left:right])
    #print('a', a[left:right])
    #print('end number_of_inversions:', number_of_inversions)
    return number_of_inversions

def get_number_naive(a, left, right):
    number_of_inversions = 0
    for i in range(left, right):
        for j in range(i+1, right):
            if a[i] > a[j]:
                number_of_inversions+=1
                #a[i], a[j] = a[j], a[i]
    #print('naive a after:', a)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
