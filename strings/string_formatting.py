def print_numbers(n):
    l=len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=l))


if __name__ == '__main__':
    inp =int(input("Enter value of n"))
    print_numbers(inp)

