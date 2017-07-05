def Mean(arr,l):
    s = sum(arr)
    mean = s/(l*1.0)
    return "{0:0.1f}".format(mean)

def Median(arr, l):
    arr.sort()
    if l%2 == 0:
        median = (arr[l/2]+arr[(l/2)-1]) / 2.0
    else:
        median = arr[l/2]
    return "{0:0.1f}".format(median)

def Mode(arr):
    d = {}
    mode = 0
    max_count = 0
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d.keys():
        if d[key] >= max_count:
            if d[key] == max_count:
                if key < mode:
                    mode = key
                    max_count = d[key]
            else:
                max_count = d[key]
                mode = key
    return mode

if __name__ == '__main__':
    n = int(raw_input())
    arr = [int(i) for i in raw_input().split()]
    print Mean(arr, n)
    print Median(arr, n)
    print Mode(arr)