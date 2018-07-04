if __name__ == '__main__':
    N = int(input())
    listNew = []
    for _ in range(N):
        command, *line = input().split()
        inputParam = list(line)
        
        if (command == 'insert'):
            listNew.insert(int(inputParam[0]),int(inputParam[1]))
        if (command == 'print'):
            #for item in listNew:
                print(listNew)
        if (command == 'remove'):
            listNew.remove(int(inputParam[0]))
        if (command == 'append'):
            listNew.append(int(inputParam[0]))
        if (command == 'sort'):
            listNew.sort()
        if (command == 'pop'):
            listNew.pop()
        if (command == 'reverse'):
            listNew.reverse()