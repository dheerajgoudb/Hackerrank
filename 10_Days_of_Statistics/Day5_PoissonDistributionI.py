from math import factorial

def poisson(k,lmda):
    return ((lmda**k) * (2.71828**(-lmda))) / factorial(k)

if __name__ == '__main__':
    lmda = float(raw_input().strip())
    k = int(raw_input())
    print "{0:0.3f}".format(poisson(k,lmda))