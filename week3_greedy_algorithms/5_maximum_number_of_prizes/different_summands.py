# Uses python3
import sys

def optimal_summands(n):
    summands = []

    if n==2:
        return [2]
    else:
        remain = n-1
        summands.append(1)
        last = 1
        while remain>0:
            last +=1
            test = remain - last
            if test > last-1 and test != last:
                summands.append(last)
                remain -= last
            else:
                summands.append(remain)
                remain = 0
  
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
