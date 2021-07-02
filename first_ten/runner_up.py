#Program to find runner up score
if __name__ == '__main__':
    n = int(input("Enter number of array"))
    arr = map(int, input("Enter values").split())
    x = set(arr)
    x = list(x)
    x.sort(reverse=True)
    print(x[1])