## TASK 1
turns = []
index = 0

with open('input.txt') as file:
    turns = file.read().splitlines()

translate = {'A':'r', 'B':'p', 'C':'s', 'X':'r', 'Y':'p', 'Z':'s'}
win_over = {'r':'s', 'p':'r', 's':'p'}
lose_to =  {'s':'r', 'r':'p', 'p':'s'}

def calculate_score(opponent, me):
    sum = 0
    # Players actions
    if(me == 'r'):
        sum += 1
    elif(me == 'p'):
        sum += 2
    elif(me == 's'):
        sum += 3
    
    # Draw
    if(opponent == me):
        return sum + 3
    
    # Win or loose
    if(win_over[me] == opponent):
        return sum + 6
    else:
        return sum
    

sum = 0
for turn in turns:
    actions = turn.split()
   
    # From A,X ... to r,p,s
    opponent = translate[actions[0]]
    me = translate[actions[1]]
    sum += calculate_score(opponent, me)  

print(sum)



## TASK 2

sum2 = 0
for turn in turns:
    actions = turn.split()
    me = ''
    opponent = translate[actions[0]]
    # 
    if(actions[1] == 'X'):
        me = win_over[opponent]
    elif(actions[1] == 'Y'):
        me = opponent
    elif(actions[1] == 'Z'):
        me = lose_to[opponent]

    sum2 += calculate_score(opponent, me)
    

print(sum2)
