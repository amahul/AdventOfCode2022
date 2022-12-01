## TASK 1
calories = [0] * 1000
index = 0

with open('input.txt') as file:    
    lines = file.readlines()
    for line in lines:
        if line.strip():        
            calories[index] = calories[index] + int(line)
        else:
            index = index+1

print(max(calories))

## TASK 2
sum = 0
for x in range(3):
    top = max(calories)
    sum += top
    calories.remove(top)

print(sum)