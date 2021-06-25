if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listing = list(arr)
    A = 0
    maxim = max(listing)
    #loop 1
    for num1 in listing:
        if (num1 > 0):
            if ((num1 > A) and (num1 < maxim)):
                A = num1
        else:
            if ((num1 < A) and (num1 < maxim)):
                A = num1