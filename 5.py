import csv
def hash(game,name):
    '''
    Создаёт хэш персонажа на основе его имени и названия игры
    game - название игры
    name - имя персонажа
    '''
    p=65
    s=game.replace(' ','')+name
    m = 10**9+9
    res=0
    alp='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        res+=(alp.find(s[i])*p**i)%m
    return res
file=open('game.txt')
data=file.read().split('\n')
datanew=[]
filenew=open('game_with_hash.csv','w')
writer=csv.writer(filenew)
t=data.pop(0).split('$')
header=['hash',t[0],t[1],t[2],t[3]]
writer.writerow(header)
for i in data:
    s=i.split('$')
    datanew.append(s)
    newline=[hash(s[0],s[1]),s[0],s[1],s[2],s[3]]
    writer.writerow(newline)
