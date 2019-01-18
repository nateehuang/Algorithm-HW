from binary_search import binary_search, linear_search
import numpy as np

if __name__ == '__main__':
    run = True
    counter = 0
    while run:
        n = np.random.randint(2, 10**2, size=1)
        print(n)
        a = np.sort(np.random.choice(range(10**3), size=n, replace=False)).tolist()
        #np.random.randint(1, 10**1, size=n)
        print('a done')
        k = np.random.randint(1, n, size=1)
        b = np.random.randint(1, 10**3, size=k)
        print('b done')
        for c in b:
            print(c)
            linear = linear_search(a, c)
            binary = binary_search(a, c)
            counter +=1
            print('already run for:', counter)
            if linear != binary:
                print('error')
                print(a, end='\n')
                print(b, end='\n')
                print(c, end='\n')
                print(linear)
                print(binary)
                run = False
                break
