with open("day8.txt", "r") as file1:
    list1 = file1.read()


new_information = list1.split("\n")

command_list_length = len(new_information)

def calculate_value(new_information):

    prev_index = []
    index = 0

    incr_val = 0
    
    while(True):

        command = new_information[index].split()
    
        if index not in prev_index:
            prev_index.append(index)
        else:
            return False


        if command[0] == "acc":
            if command[1][0] == "+": 
                incr_val += int(command[1][1:])
            elif command[1][0] == "-":
                incr_val -= int(command[1][1:])
            else:
                continue
            index += 1

        elif command[0] == "jmp":
            if command[1][0] == "+":
                index += int(command[1][1:])
            elif command[1][0] == "-":
                index -= int(command[1][1:])
            else:
                continue
        else:
            index += 1
        
        if index >= command_list_length - 1:
            print("terminated", incr_val)
            return True



for i in range(len(new_information)):
    line_break = new_information[i].split()
    
    temp_list = new_information.copy()

    if line_break[0] == "jmp":
        temp_list[i] = temp_list[i].replace("jmp", "nop")
        if calculate_value(temp_list):
            break
    elif line_break == "nop":
        temp_list[i] = temp_list[i].replace("nop", "jmp")
        if calculate_value(temp_list):
            break
    else:
        continue
