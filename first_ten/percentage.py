#HackerRank program to find the average mark of desired student
if __name__ == '__main__':
    n = int(input("Enter no.of students"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter name and marks").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for i in student_marks[query_name]:
        sum = sum + i
    print("{0:.2f}".format(sum / 3))