# Complete the solve function below.
def solve(s):
    local_string = ''
    string_list = s.split(' ')
    for i in range(len(string_list)):
        local_string = local_string + string_list[i].capitalize()+" "

    print(local_string)

if __name__ == '__main__':
    s = input()
    solve(s)
