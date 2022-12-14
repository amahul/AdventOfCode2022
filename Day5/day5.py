## TASK 1
directions = False

crates=[]
actions=[]
n = 9
for i in range(n):
	crates.append([])

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        if line.strip():  
            if(directions):
                actions.append(line)       
                
            elif '[' in line:                
                # print(line)
                row = [line[idx:idx + 4] for idx in range(0, len(line), 4)]
                
                index = 0
                for value in row:
                    if value.strip():
                        print(value.strip())
                        # crates[index].append(value.strip())
                        crates[index].insert(0, value.strip())
                    index += 1
                    
                # for character in line:
                #     print(character)
        else:                  
            directions = True

# PART 1
# print(crates)
# crate = ""      
# for action in actions:
#     # print(action)
#     splitted = action.split()
#     for i in range(0, int(splitted[1])):
#         # print(i)
#         crate = crates[int(splitted[3])-1].pop(0)
#         # crates[int(splitted[5])-1].append(crate)
#         crates[int(splitted[5])-1].append(crate)
    
#     print(crates)
  
# for crate in crates:
#     print(crate)


# PART 2      
print(crates)

for action in actions:
    to_move = []
    print(action)
    splitted = action.split()
    for i in range(0, int(splitted[1])):
        print(i)
        to_move.append(crates[int(splitted[3])-1].pop())
        # crates[int(splitted[5])-1].append(crate)
    
    print(to_move)
    # for crate in to_move:
    #     crates[int(splitted[5])-1].append(crate)
    for x in range(len(to_move)):       
        crates[int(splitted[5])-1].append(to_move.pop())
        
    
    print(crates)
  
print("END")
for crate in crates:
    print(crate)

# JNRSCDWPP