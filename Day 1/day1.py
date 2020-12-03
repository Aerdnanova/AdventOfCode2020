with open("day1.txt", "r") as file1:
    list1 = file1.readlines()
    list2 = []
    for line in list1:
        list2.append(int(line))
    file1.close()


for value in list2:
    for value2 in list2:
        for value3 in list2:
            if value + value2 + value3 == 2020:
                print(value * value2 * value3)
                break
