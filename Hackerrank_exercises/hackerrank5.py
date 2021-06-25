# Lists
"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
N = int(input())
cmd_list = []
list1 = []
#recibir los comandos a hacer
for command in range(N):
    cmd = input()
    cmd_list.append(cmd)
#ejecutar los comandos
com = 0
while com < len(cmd_list):
    check_com = cmd_list[com]
    if check_com == "print":
        print(list1)
    elif check_com == "sort":
        list1.sort()
    elif check_com == "pop":
        list1.pop()
    elif check_com == "reverse":
        list1.reverse()
    else:
        args_split = check_com.split()
        check_com = str(args_split[0])
        arg1 = int(args_split[1])
        if check_com == "remove":
            list1.remove(arg1)
        elif check_com == "append":
            list1.append(arg1)
        else:
            arg2 = int(args_split[2])
            list1.insert(arg1, arg2)
    com += 1