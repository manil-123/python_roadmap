def merge_the_tools(st,n):
    c = 0;
    s = ''
    for i in st:
        if i not in s:
            s=s+i
        c+=1
        if (c==n):
            print(s)
            c=0
            s=''

if __name__ == '__main__':
    s = input("Enter a sentence")
    n=int(input("enter value of n"))
    merge_the_tools(s,n)

