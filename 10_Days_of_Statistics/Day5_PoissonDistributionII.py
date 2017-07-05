if __name__ == '__main__':
    [mA, mB] = [float(i) for i in raw_input().strip().split()]
    print "{0:0.3f}".format(160 + 40*(mA + mA**2))
    print "{0:0.3f}".format(128 + 40*(mB + mB**2))