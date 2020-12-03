with open("day3.txt", "r") as file1:
    list1 = file1.readlines()

list1.pop(0)

def tree_finder(right, down, list1):
    
    row_length = len(list1[0]) - 1
    column_index = right
    tree_count = 0
    
    
    for line in list1:

        if column_index >= row_length:
            column_index = column_index - row_length

        if line[column_index] == "#":
            tree_count = tree_count + 1

        column_index = column_index + right
    
    return tree_count


def opp_tree_finder(right, down, list1):
    row_length = len(list1[0]) - 1
    length = len(list1)
    column_index = right
    tree_count = 0
   
    if down%2 == 0:
        list1.pop(0)

    for i in range(0, length, down):
        line = list1[i]
        if column_index >= row_length:
            column_index = column_index - row_length

        if line[column_index] == "#":
            tree_count = tree_count + 1

        column_index = column_index + right
    
    return tree_count

print(tree_finder(1,1,list1)*tree_finder(3,1,list1)*tree_finder(5,1,list1)*tree_finder(7,1,list1)*opp_tree_finder(1,2,list1))
