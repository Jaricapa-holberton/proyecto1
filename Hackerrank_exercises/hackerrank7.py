# sWAP cASE
"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""
def swap_case(s):
    new_str = ""
    iter_char = 0
    check_up = False
    check_low = False
    while iter_char < len(s):
        char1 = s[iter_char]
        check_up = char1.isupper()
        check_low = char1.islower()
        if check_up == True:
            char2 = char1.lower()
        if check_low == True:
            char2 = char1.upper()
        if check_low == False and check_up == False:
            char2 = char1
        new_str += char2
        iter_char +=  1
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)