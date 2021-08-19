def count_substring(string, sub_string):
    len_str = len(string)
    len_sub = len(sub_string)
    i = 0
    j = 0
    compare = ''
    counter = 0
    while (i < len_str):
        compare += string[i]
        idx = i
        while (j < len_sub - 1):
            if ((idx + 1) < len_str):
                compare += string[idx + 1]
            idx += 1
            j += 1
        idx = 0
        j = 0
        if (sub_string == compare):
            counter += 1
            compare = ''
        else:
            compare = ''
        i += 1
    return(counter)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)