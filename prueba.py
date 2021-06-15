def is_leap(year):
    leap = False
    
    # Write your logic here
    check1, check2, check3 = False, False, False
    if (year % 4 == 0):
        check1 = True
    if (year % 100 != 0):
        check2 = True
    if (year % 400 == 0):
        check3 = True
    if ((check1 == True) and (check2 == True) and (check3 == True)):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))