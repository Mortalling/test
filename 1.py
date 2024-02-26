import csv
file=open('game.txt')
data=file.read().split('\n')
header=data.pop(0).split('$')
gamenew=open('game_new.csv','w')
writer=csv.writer(gamenew)
writer.writerow(header)
for i in data:
    s=i.split('$')
    if '55' in s[2]:
        print(f'У персонажа\t{s[1]}\tв игре\t{s[0]}\tнашлась ошибка с кодом:\t {s[2]}.\tДата фиксации:\t {s[3]}')
        s[2]='Done'
        s[3]='0000-00-00'
    writer.writerow(s)
