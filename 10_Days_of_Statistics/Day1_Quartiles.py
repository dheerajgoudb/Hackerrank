def quartile(arr):
    l = len(arr)
    if l%2 == 0:
        q = (arr[(l/2)-1]+arr[l/2]) / 2
    else:
        q = arr[l/2]
    return q

if __name__ == '__main__':
    n = int(raw_input())
    X = [int(i) for i in raw_input().strip().split()]
    X.sort()
    if n%2 == 0:
        low = (n/2) - 1
        high = n/2
    else:
        low = (n/2) - 1
        high = (n/2) + 1
    print quartile(X[0:low+1])
    print quartile(X)
    print quartile(X[high:n])