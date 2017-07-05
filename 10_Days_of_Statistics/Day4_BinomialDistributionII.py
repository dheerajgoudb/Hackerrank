from math import factorial as f

def binom(x,n,p):
    return (f(n) / (f(x) * f(n-x))) * (p**x) * ((1-p) ** (n-x))

if __name__ == '__main__':
    [p, n] = [int(i) for i in raw_input().strip().split()]
    q = 1 - (p/100.0)
    count1 = 0
    count2 = 0
    for i in xrange(0,3):
        count1 += binom(i, n, p/100.0)
    for j in xrange(2,n+1):
        count2 += binom(j, n, p/100.0)
    print "{0:0.3f}".format(count1)
    print "{0:0.3f}".format(count2)