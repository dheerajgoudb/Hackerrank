def quartile(arr):
    l = len(arr)
    if l%2 == 0:
        q = (arr[(l/2)-1]+arr[l/2]) / 2
    else:
        q = arr[l/2]
    return q

def newData(X,F):
    arr = []
    for i in xrange(0,len(X)):
        for j in xrange(0,len(F)):
            if i == j:
                tmp = [X[i] for item in xrange(0,F[j])]
        arr.append(tmp)
    lst = [item for sublist in arr for item in sublist]
    return lst

if __name__ == '__main__':
    n = int(raw_input())
    X = [int(i) for i in raw_input().strip().split()]
    F = [int(i) for i in raw_input().strip().split()]
    lst = newData(X, F)
    lst.sort()
    n = len(lst)
    if n%2 == 0:
        low = (n/2) - 1
        high = n/2
    else:
        low = (n/2) - 1
        high = (n/2) + 1
    print "{0:0.1f}".format(quartile(lst[high:n]) - quartile(lst[0:low+1]))