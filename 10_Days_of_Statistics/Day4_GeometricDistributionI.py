def geomtrcD(n,p):
    return ((1-p)**(n-1)) * p

if __name__ == '__main__':
    [nr,dr] = [int(i) for i in raw_input().strip().split()]
    n = int(raw_input())
    p = nr*1.0 / dr
    print "{0:0.3f}".format(geomtrcD(n,p))