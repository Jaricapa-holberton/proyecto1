"""
You are given a string .
Your task is to find out if the string  contains: 
* alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()
    l=list(s)
    a,b,c,d,e=False,False,False,False,False
    for i in l:
        if i.isalnum():
            a=True
        if i.isalpha():
            b=True
        if i.isdigit():
            c=True
        if i.islower():
            d=True
        if i.isupper():
            e=True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)