if __name__ == '__main__':
    students = []
    grades = set()
    for _ in range(int(input())):

        name = input()
        score = float(input())
        students.append([name, score])
        grades.add(score)
    
    grades = sorted(grades)
    students.sort()

    temp = grades[1]
    for i in range(len(students)):
        if students[i][1] == temp:
            print(students[i][0])
            