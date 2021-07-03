#HackerRank tuple program
if __name__ == '__main__':
    n = int(input("Enter no.of elements"))
    integer_list = map(int, input("Enter element").split())
    t1=tuple()
    for i in integer_list:
        y = list(t1)
        y.append(i)
        t1 = tuple(y)
    print(hash(t1))

'''
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

'''