def split_and_join(line):
    list=line.split(" ")
    return "-".join(list)
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)