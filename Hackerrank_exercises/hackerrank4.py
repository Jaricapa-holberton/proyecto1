#Set .discard(), .remove() & .pop()
""" 
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints



Output Format

Print the sum of the elements of set  on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
"""
n = int(input())
s = set(map(int, input().split()))
cmd_list = []
c = int(input())
#recibir los comandos a hacer
for command in range(c):
    cmd = input()
    cmd_list.append(cmd)
#ejecutar los comandos
com = 0
while com < len(cmd_list):
    check_com = cmd_list[com]
    if check_com == "pop":
        s.pop()
    else:
        if check_com == "remove":
            lan = len(cmd_list[com]) - 1
            lin = int(cmd_list[com][lan])
            s.remove(lin)
        else:
            lan = len(cmd_list[com]) - 1
            lin = int(cmd_list[com][lan])
            s.discard(lin)
    com += 1
#sumar los elementos restantes del set
sum_set = 0
for n in s:
    sum_set += n
#mostrar suma
print(sum_set)