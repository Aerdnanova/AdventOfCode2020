with open("day2.txt", "r") as file1:
    list1 = file1.readlines()
    list2 = []
    for line in list1:
        list2.append(line)
    file1.close()

new_total = 0

for value in list2:
    
    rang, char, string = value.split()

    char = char[0]
    min_val, max_val = map(int, rang.split("-"))

    new_total += sum(string[x - 1] == char for x in (min_val, max_val)) == 1 

print(new_total)
