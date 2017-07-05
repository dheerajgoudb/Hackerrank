def WeightedMean(X,W,N):
    nr_sum = 0
    dr_sum = sum(W)
    for i in xrange(0,N):
        nr_sum += (X[i] * W[i])
    wm = nr_sum / (dr_sum * 1.0)
    return "{:0.1f}".format(wm)

if __name__ == '__main__':
    N = int(raw_input())
    X = [int(i) for i in raw_input().split()]
    W = [int(i) for i in raw_input().split()]
    print WeightedMean(X,W,N)