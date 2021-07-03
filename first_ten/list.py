#HackerRank program to perform list operations based on user input
if __name__ == '__main__':
    N = int(input("Enter no.of commands"))
    myList = []
    for i in range(N):
        command = input("Enter command").split()
        for j in range(1, len(command)):
            command[j] = int(command[j])

        if command[0] == 'append':
            myList.append(command[1])
        elif command[0] == 'insert':
            myList.insert(command[1], command[2])
        elif command[0] == 'remove':
            myList.remove(command[1])
        elif command[0] == 'pop':
            myList.pop()
        elif command[0] == 'sort':
            myList.sort()
        elif command[0] == 'reverse':
            myList.reverse()
        elif command[0] == 'print':
            print(myList)