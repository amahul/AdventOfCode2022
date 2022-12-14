input = []
directories = []

with open('input.txt') as file:
    input = file.read().splitlines()

class Directory:
    childrens = []
    def __init__(self, name, parent, depth):    
        self.depth = depth
        self.name = name
        self.parent = parent
        self.size = 0

    def add_size(self, new_size):    
        # print("Add " + str(new_size) + " to " + self.name)
        self.size += new_size  

    # Print
    def __str__(self):         
        
        out = "Name: " + self.name + " Size: " + str(self.size) +  " Parent: "
        if self.parent:
            out += self.parent.name
        else:
            out += " none"
    
        return out
  


current_dir = None
depth = 0
for line in input:

    splitted = line.split()    
    
    if splitted[0] == '$':
        # Handle direction actions
        if splitted[1] == 'cd':
            # Move one up in dir
            if splitted[2] == '..':
                depth -= 1
                current_dir = current_dir.parent
            else:
                
                # Create new directory
                if current_dir:
                    new_dir = Directory(splitted[2], current_dir, depth)
                else: 
                    new_dir = Directory(splitted[2], None, depth)
                                
                # Save all directories 
                directories.append(new_dir)      
                current_dir = new_dir        
                depth += 1     

    # Check for file after ls and add size to current dir
    elif splitted[0] != 'dir':
        current_dir.add_size(int(splitted[0]))    


# Sort list with maximum depth first
directories.sort(key=lambda x: x.depth, reverse=True)

# Add size to parent directories
for dir in directories:
    if dir.parent:
        dir.parent.add_size(dir.size)    

sum = 0
for dir in directories:
    if dir.size < 100000:
        sum += dir.size

    
print("Part1: " + str(sum))

# 1495548 too low
# 1581595 Correct

# Part 2
unused_size = 70000000 - directories[len(directories)-1].size
required = 30000000
min_size = 999999999
for dir in directories:
    new_size = unused_size + dir.size

    if new_size > required and dir.size < min_size:
        min_size = dir.size


print("Minimum size: " + str(min_size))
        
# 3847317 - too high
# 1544176 - correct