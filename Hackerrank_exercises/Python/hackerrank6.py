# Check Strict Superset
# i used this page for declare  varibles in a loop: https://www.codegrepper.com/code-examples/python/dynamically+create+variables+in+loop+python
"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set .
The second line contains integer , the number of other sets.
The next  lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
"""
#Variable A contains a set of items.
#Variable N tells the program how many sets will be created.

A = set(map(int, input().split()))
N = int(input())

#List in which we will store different sets once we create them.

set_list = []

#We loop N times and variable x creates N sets. We append these sets to a list. Previously created variable set_list now contains a number of different sets.

for i in range(N):
    x = set(map(int, input().split()))
    set_list.append(x)

#Default value of the resuls variable is True

result = True

#We iterate over differnet sets in a list.  Result will stay True, unless we find a set to whom A is not a superset.

for i in set_list:
    if not A.issuperset(i):
        result = False

print(result)