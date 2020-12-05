with open("day5.txt", "r") as file1:
    input_list = file1.read().split()

max_seat_id = 0
id_list = []

for line in input_list:
    start_seat = 0
    end_seat = 127

    start_col = 0
    end_col = 7

   
    for char in line:
        if char == "F":
            end_seat = end_seat - (end_seat - start_seat) // 2 - 1

        elif char == "B":
            start_seat = start_seat + (end_seat - start_seat) // 2 + 1 

        elif char == "R":
            start_col = start_col + (end_col - start_col) // 2 + 1

        elif char == "L":
            end_col = end_col - (end_col - start_col) // 2 - 1

        else:
            print("error")
    
    test_id = end_seat * 8 + end_col
    
    id_list.append(test_id)
    
    if max_seat_id < test_id:
        max_seat_id = test_id

id_list = sorted(id_list)

for val in range(0, len(id_list) - 1):
    if id_list[val] + 2 == id_list[val + 1]:
        print(id_list[val], id_list[val+1])

