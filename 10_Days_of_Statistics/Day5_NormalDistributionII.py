from math import erf, sqrt

def CDF(x, mu, std):
    return (0.5 * (1+erf((x-mu)/(std*sqrt(2))))) * 100

if __name__ == '__main__':
    [mu, std] = [int(i) for i in raw_input().strip().split()]
    x1 = int(raw_input().strip())
    x2 = int(raw_input().strip())
    print "{0:0.2f}".format(100 - CDF(x1, mu, std))
    print "{0:0.2f}".format(100 - CDF(x2, mu, std))
    print "{0:0.2f}".format(CDF(60, mu, std))