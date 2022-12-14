## TASK 1
chars = []


with open("input.txt") as file:
    for line in file:  
       for ch in line: 
           chars.append(ch)


# PART 1
for i in range(3, len(chars)):
    four_chars = []
    for j in range(0,4):
        four_chars.insert(0, chars[i-j])
    
    if len(four_chars) == len(set(four_chars)):
        index = i    
        break

print(index+1)

# PART 2
for i in range(3, len(chars)):
    fourteen_chars = []
    for j in range(0,14):
        fourteen_chars.insert(0, chars[i-j])
    
    if len(fourteen_chars) == len(set(fourteen_chars)):
        index = i    
        break

print(index+1)
