def print_full_name(first, last):
    str="Hello {} {}! You just delved into python."
    print(str.format(first,last))
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)