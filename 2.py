file=open('game.txt')
data=file.read().split('\n')
data.pop(0)
datanew=[]
for i in data:
    s=i.split('$')
    datanew.append(s)
datanew=sorted(datanew)
game=''
bugs=[]
bugsum=0
for line in datanew:
    if line[0]!=game:
        bugs.append([game,bugsum])
        bugsum=0
        game=line[0]
    bugsum+=1
bugs.pop(0)
for i in bugs:
    print(f'{i[0]} - количество багов: {i[1]}')
