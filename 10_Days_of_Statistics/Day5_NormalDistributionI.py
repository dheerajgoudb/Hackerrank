from math import erf, sqrt

def CDF(x, mu, sigma):
    return 0.5 * (1+erf((x-mu)/(sigma*sqrt(2))))

if __name__ == '__main__':
    [mean, std] = [int(i) for i in raw_input().strip().split()]
    x1 = float(raw_input().strip())
    [r1, r2] = [int(i) for i in raw_input().strip().split()]
    print "{0:0.3f}".format(CDF(x1, mean, std))
    print "{0:0.3f}".format(CDF(r2, mean, std) - CDF(r1, mean, std))