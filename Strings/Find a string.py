def count_substring(string:str, sub_string:str):
    find = string.find(sub_string)
    total = 0
    while find != -1:
        total += 1
        find = string.find(sub_string,find+1)
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)