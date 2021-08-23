if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    #find the key for the query name
    if query_name in student_marks:
        scores_to_avg = student_marks[query_name]
    #get the avg
    sum = 0
    score = 0
    while score < len(scores_to_avg):
        sum += scores_to_avg[score]
        score += 1
    avg = sum / len(scores_to_avg)
    #display the average
    print("{:.2f}".format(avg))

    