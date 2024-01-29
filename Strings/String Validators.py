if __name__ == '__main__':
    string = input()
    alnum = False
    alpha = False
    digits = False
    lowercase = False
    uppercase = False
    for s in string:
        if s.isalnum():
            alnum = True
        if s.isalpha():
            alpha = True
        if s.isdigit():
            digits = True
        if s.islower():
            lowercase = True
        if s.isupper():
            uppercase = True
    
    print(alnum,alpha,digits,lowercase,uppercase, sep='\n')