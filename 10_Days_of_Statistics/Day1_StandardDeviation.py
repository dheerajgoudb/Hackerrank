def SD(X,N):
    s = sum(X)
    mean = s / (N * 1.0)
    count = 0
    for i in xrange(0,N):
        count += (X[i] - mean) ** 2
    sd = (count / N) ** (1/2.0)
    return "{:0.1f}".format(sd)

if __name__ == '__main__':
    N = int(raw_input())
    X = [int(i) for i in raw_input().split()]
    print SD(X,N)