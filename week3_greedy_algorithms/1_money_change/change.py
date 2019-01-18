# Uses python3
import sys

def get_change(m):
    #write your code here
    counter = 0
    while m>0:
        if m >= 10:
            counter +=1
            m-=10
        elif m >= 5:
            counter +=1
            m-=5
        elif m >= 1:
            counter +=1
            m-=1
    return counter  

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
