#Uses python3

import sys

def IsGreaterOrEqual(d1, d2):
    if d2==-float('inf'):
        return True

    first = int(d1 + d2)
    second = int(d2 + d1)
    if first < second:
        return False
    else:
        return True


def largest_number(a):
    
    res = ""
    digits =a
    
    while digits !=[]:
        maxDigit = -float("inf")
        for d in digits:
   
            if IsGreaterOrEqual(d, maxDigit):
                maxDigit = d
        res += str(maxDigit)
        digits.remove(maxDigit)

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
