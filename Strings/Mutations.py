
# This solution if you want to write the solution yourself

# def mutate_string(string:str, position, character):
#     result = ''
#     for s,i in zip(string, range(len(string))):
#         result += s if i != position else character
#     return result

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)