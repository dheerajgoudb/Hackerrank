from math import sqrt, erf

def normalCDF(x, mu, std):
    return 0.5 * (1+erf((x-mu)/(std*sqrt(2))))

if __name__ == '__main__':
    max_tkt = input()
    n = input()
    mu = input()
    std = input()
    mu_new = n * mu
    std_new = sqrt(n) * std
    print "{0:0.4f}".format(normalCDF(max_tkt, mu_new, std_new))