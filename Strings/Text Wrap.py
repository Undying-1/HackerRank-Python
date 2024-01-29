import textwrap

#Textwrap solution

# def wrap(string, max_width):
#     list = textwrap.wrap(string, max_width)
#     result = ''
#     for l in list:
#         result += l + '\n'
#     return result
               
# Custom solution
def wrap(string, max_width):
    total = len(string) / max_width
    start_index= 0
    end_index = max_width
    result = ''
    for i in range(int(total)):
        result += string[start_index:end_index] + '\n'
        start_index = end_index
        end_index += max_width
    
    if isinstance(total, float):
        result += string[start_index::]
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)