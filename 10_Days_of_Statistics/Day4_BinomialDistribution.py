from math import factorial as f

def binom(x,n,p):
    return (f(n) / (f(x) * f(n-x))) * (p**x) * ((1-p) ** (n-x))

if __name__ == '__main__':
    [a,b] = [float(i) for i in raw_input().strip().split()]
    n = 6
    count = 0
    p, q = a/(a+b), b/(a+b)
    for i in range(3,7):
        count += binom(i,n,p)
    print "{0:0.3f}".format(count)
