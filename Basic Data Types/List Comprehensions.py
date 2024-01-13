if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    for i in range(0,x+1):
        for j in range(0, y+1):
            for k in range(0,z+1):
                temp = []
                if i+j+k != n:
                    temp.append(i)
                    temp.append(j)
                    temp.append(k)
                    result.append(temp)
                    
    print(result)