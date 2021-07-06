def minion_game(string):
    score_kevin = 0
    score_stuart = 0

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            score_kevin += len(string) - i
        else:
            score_stuart += len(string) - i

    if score_kevin > score_stuart:
        print("Kevin {}".format(score_kevin))
    elif score_kevin < score_stuart:
        print("Stuart {}".format(score_stuart))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input("Enter a string")
    minion_game(s.upper())