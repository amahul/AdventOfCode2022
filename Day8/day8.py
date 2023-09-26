trees = []


index = -1
with open("input.txt", "r") as file:
    for line in file:  
        trees.append([])
        index += 1
        for ch in line: 
            if ch.strip():
                trees[index].append(ch)
   

# Save data as rows and columns
rows = []
for row in trees:
    rows.append(row)

columns = []
for i in range(0, len(trees)):
    column = []
    for j in range(0, len(trees[i])):        
        # print(trees[i][j])
        column.append(trees[j][i])
    columns.append(column)

visible = 2*len(rows)+2*(len(columns)-2)

# Loop through all tress that are not on the edge
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):          
        value = trees[i][j]        
        # Save all trees before and after in both row and column
        before_row = trees[i][:j]
        after_row = trees[i][j+1:]
        before_column = columns[j][:i]
        after_column =  columns[j][i+1:]
        # Tree height must be larger than existing tree in any direction
        if value > max(before_row) or value > max(after_row) or value > max(before_column) or value > max(after_column):
            visible += 1    

       
print(visible)

# 1719

# Part 2

def scenic_score_dir(current, trees):
    nr_trees = 0
    prev_tree = current

    for next_tree in trees:
        nr_trees += 1
        if next_tree >= prev_tree:                    
            return nr_trees 
                
    return nr_trees


scenic_scores = []
# Loop through all tress that are not on the edge
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):   
        # i is row
        # j is column
        # print(trees[i][j])
        currentHeight = trees[i][j]

        before_row = trees[i][:j]
        before_row.reverse()    
        after_row = trees[i][j+1:]
        before_column = columns[j][:i]
        before_column.reverse()
        after_column =  columns[j][i+1:]

        

        s1 = scenic_score_dir(currentHeight, before_row)
        s2 = scenic_score_dir(currentHeight, before_column)
        s3 = scenic_score_dir(currentHeight, after_row)
        s4 = scenic_score_dir(currentHeight, after_column)
        scenic_score = s1 * s2 * s3 * s4
        
        print("Sum: " + str(scenic_score))
        print("------------")
        scenic_scores.append(scenic_score)

print(max(scenic_scores))

# 590824
