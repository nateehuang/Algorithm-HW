from points_and_segments import fast_count_segments, naive_count_segments
import numpy as np

if __name__ == '__main__':
    run = True
    counter = 0
    while run:
        s = int(np.random.randint(1, 10**4, size=1))
        p = int(np.random.randint(1, 10**4, size=1))
        print('s:', s, ' p:', p)
        ran = 10**3
        a = np.random.choice(range(-ran, ran), size=s).tolist()
        b = (a + np.random.choice(range(0, ran), size=s)).tolist()
        x = np.random.choice(range(-ran, ran), size=p).tolist()
        print('starts:', a)
        print('ends:', b)
        print('test', x)
        #np.random.randint(1, 10**1, size=n)
        print('done generating data')
        #print('data:', a)

        #res1 = naive_count_segments(a, b, x)
        res2 = fast_count_segments(a, b, x)
        print('done fast count')
        #if res1 != res2:
        #    print('error \n')
        #    print('navie:', res1)
        #    print('fast:', res2)
        #    break
