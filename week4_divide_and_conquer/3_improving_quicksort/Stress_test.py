from sorting import randomized_quick_sort, randomized_quick_sort2
import numpy as np

if __name__ == '__main__':
    run = True
    counter = 0
    while run:
        n = int(np.random.randint(2, 5, size=1))
        print('n:', n)
        a = np.random.choice(range(10**2), size=n).tolist()
        b = a[:]
        #np.random.randint(1, 10**1, size=n)
        print('done generating data')
        print('data:', a)

        randomized_quick_sort(a, 0, n-1)
        randomized_quick_sort2(b, 0, n-1)
        if a != b:
            print('error \n')
            print('3 partition', a)
            print('2 partition', b)
            break
