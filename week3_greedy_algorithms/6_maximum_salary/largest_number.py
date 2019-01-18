#Uses python3

import sys

def IsGreaterOrEqual(d1, d2):
    if d2==-float('inf'):
        return True
    #print(type(d1))
    #print(type(d2))
    first = int(d1 + d2)
    second = int(d2 + d1)
    if first < second:
        return False
    else:
        return True


def largest_number(a):
    #write your code here
    res = ""
    digits =a
    #print(digits)
    while digits !=[]:
        maxDigit = -float("inf")
        for d in digits:
            #print(d)
            if IsGreaterOrEqual(d, maxDigit):
                maxDigit = d
        res += str(maxDigit)
        digits.remove(maxDigit)
    #for x in a:
        #res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
