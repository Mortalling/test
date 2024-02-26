import csv
file=open('game.txt')
data=file.read().split('\n')
datanew=[]
filenew=open('game_counter.csv','w')
writer=csv.writer(filenew)
header=data.pop(0).split('$')
header.append('counter')
writer.writerow(header)
for i in data:
    s=i.split('$')
    datanew.append(s)
datasort=sorted(datanew)
game=''
bugs=[]
bugsum=0
for line in datasort:
    if line[0]!=game:
        bugs.append([game,bugsum])
        bugsum=0
        game=line[0]
    bugsum+=1
bugs.pop(0)
for line in datanew:
    newline=line
    for i in bugs:
        if i[0]==newline[0]:
            newline.append(i[1])
            break
    writer.writerow(newline)
    
