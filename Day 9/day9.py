with open("day9.txt", "r") as file1:
    list1 = file1.read()

input_info = list1.split()

start = 0
end = 25

while(True):
    test_list = input_info[start:end]
    test_val = int(input_info[end])

    for preamble in test_list:
        if str(test_val - int(preamble)) in test_list:
            break
        else:
            if preamble == input_info[end - 1]:
                hold_val = test_val
                print(test_val)


    start += 1
    end += 1

    if end >= len(input_info):
        break


for i in range(0, len(input_info)):
    summ = 0
    start = i
    for n in range(i, len(input_info)):
        
        summ += int(input_info[n])

        if summ == hold_val:
            new_list = input_info[i:n + 1]
            new_list = [int(a) for a in new_list]
            max_val = max(new_list)
            min_val = min(new_list)
            print(max_val, min_val, max_val + min_val)
            break

