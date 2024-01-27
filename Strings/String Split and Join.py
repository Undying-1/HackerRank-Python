
# This solution if you want to write the solution yourself

# def split_and_join(line):
#     result = ''
#     for s in line:
#         result += '-' if s == ' ' else s
#     return result


def split_and_join(line: str):
    line=  line.split(' ')
    return '-'.join(line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)