from inversions import get_number_of_inversions, get_number_naive
import numpy as np

if __name__ == '__main__':
    run = True
    counter = 0
    while run:
        n = int(np.random.randint(2, 10**3, size=1))
        print('n:', n)
        a = np.random.choice(range(10**6), size=n).tolist()
        c = a[:]
        b = n * [0]
        #np.random.randint(1, 10**1, size=n)
        print('done generating data')
        print('data:', a)

        res1 = get_number_naive(a, 0, n)
        res2 = get_number_of_inversions(c, b, 0, n)
        if res1 != res2:
            print('error \n')
            print('navie:', res1)
            print('fast:', res2)
            break
