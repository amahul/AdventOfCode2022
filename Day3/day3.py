## TASK 1
chars = []


with open('input.txt') as file:
    backpacks = file.read().splitlines()

with open("input.txt") as file:
    for line in file:  
       for ch in line: 
           chars.append(ch)

def char_to_number(character):
    print(character)
    if character.islower():        
        return ord(character) - 96
    else:        
        return ord(character) - 38

# Part 1
sum1 = 0
for backpack in backpacks:
    compartment1, compartment2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]

    for char in compartment1:
        if char in compartment2:           
            sum1 += char_to_number(char)
            break

print(sum1)


# Part 2
sum2 = 0
for i in range(0, len(backpacks), 3):
    for char in backpacks[i]:
        if char in backpacks[i+1] and char in backpacks[i+2]:           
            sum2 += char_to_number(char)
            break
print(sum2)