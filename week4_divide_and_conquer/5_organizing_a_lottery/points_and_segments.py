# Uses python3
import sys

def search(ary, pt, way):
    left = 0; right = len(ary)-1
    if way == 'left':
        if ary[right]<=pt:
            return right + 1
        while True:
            if right < left:
                return 0
            mid = (left + right)//2
            if ary[mid] > pt :
                if ary[mid-1] <= pt:
                    return mid
                right = mid - 1
            else:
                if ary[mid+1]>pt:
                    return mid + 1
                left = mid + 1
    else:
        if ary[left] >= pt:
            return right + 1
        while True:
            if right < left:
                return 0
            mid = (left + right)//2
            if ary[mid] >= pt :
                if ary[mid-1] < pt:
                    return len(ary) - mid
                right = mid - 1
            else:
                if mid == len(ary)-1:
                    return 0
                if ary[mid+1] >= pt:
                    return len(ary) - mid - 1
                left = mid + 1



def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    length = len(points)
    for i in range(length):
        p = points[i]
        l = search(starts, p, 'left')
        #print('l:', l)
        r = search(ends, p, 'right')
        #print('r:', r)
        cnt[i] = l + r - len(starts)

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
