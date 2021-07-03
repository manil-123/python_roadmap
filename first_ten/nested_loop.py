#Program to print the name of student with second lowest score,if multiple students have same second
#lowest marks then print them in ascending order
#Problem from HackerRank

if __name__ == '__main__':
    result=[]
    gradeList=[]
    for i in range(int(input("Enter n"))):
        name = input("Enter name")
        score = float(input("Enter score"))
        result.append([name,score])
        gradeList.append(score)

    gradeList=sorted(set(gradeList))
    lowest_score=gradeList[1]
    namesList=[]
    for val in result:
        if lowest_score==val[1]:
            namesList.append(val[0])
    namesList.sort()
    for name in namesList:
        print(name)