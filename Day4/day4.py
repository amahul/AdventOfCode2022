## TASK 1
pairs = []

with open('input.txt') as file:
    pairs = file.read().splitlines()

index1 = 0
# Part 1
for pair in pairs:
    elf1_seq = []
    elf2_seq = []
    elf1, elf2 = pair.split(',')
    # Loop though all numbers in elf1 and create sequence of numbers
    for i in range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1):
        elf1_seq.append(i)
    for j in range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1):
        elf2_seq.append(j)
    
    # Check if all items from one seq exists in the other
    check1 =  all(item in elf1_seq for item in elf2_seq)
    check2 =  all(item in elf2_seq for item in elf1_seq)
    if check1 or check2:
        index1 += 1
            
print(index1)

# Part 2
index2 = 0
for pair in pairs:
    elf1_seq = []
    elf2_seq = []
    elf1, elf2 = pair.split(',')
    # Loop though all numbers in elf1 and create sequence of numbers
    for i in range(int(elf1.split('-')[0]), int(elf1.split('-')[1])+1):
        elf1_seq.append(i)
    for j in range(int(elf2.split('-')[0]), int(elf2.split('-')[1])+1):
        elf2_seq.append(j)

    # Check if any items from one set exists in the other
    set1 = set(elf1_seq) 
    set2 = set(elf2_seq) 
    if set1.intersection(set2) or set2.intersection(set1): 
        index2 += 1
    
        
print(index2)