
# This solution if you want to write the solution yourself

# def swap_case(s: str):
#     result = ''
#     for i in s:
#         result += i.lower() if i.isupper() else i.upper()
#     return result

def swap_case(s: str):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)