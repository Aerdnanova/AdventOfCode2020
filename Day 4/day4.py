with open("day4.txt", "r") as file1:
    file_text = file1.read()


passport_list = file_text.split("\n\n")
find_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid']
invalid = 0
flag = False

for passport in passport_list:
    for string in find_list:
        if string not in passport:
            invalid += 1
            flag = True
            break
    if flag:
        flag = False
        continue

    passport_information = passport.split()
    for entry in passport_information:
        entry_info = entry.split(":")
        if entry_info[0] == "byr":
            if len(entry_info[1]) != 4 or (int(entry_info[1]) > 2002 or int(entry_info[1]) < 1920):
                invalid += 1
                break
        elif entry_info[0] == "iyr":
            if len(entry_info[1]) != 4 or (int(entry_info[1]) > 2020 or int(entry_info[1]) < 2010):
                invalid += 1
                break
        elif entry_info[0] == "eyr":
            if len(entry_info[1]) != 4 or (int(entry_info[1]) > 2030 or int(entry_info[1]) < 2020):
                invalid += 1
                break
        elif entry_info[0] == "hgt":
            length = len(entry_info[1]) - 2
            if entry_info[1][length:] in ["in", "cm"]:
                if (int(entry_info[1][:length]) < 150 or int(entry_info[1][:length]) > 193) and entry_info[1][length:] == "cm":
                    invalid += 1
                    break
                if (int(entry_info[1][:length]) < 59 or int(entry_info[1][:length]) > 76) and entry_info[1][length:] == "in":
                    invalid += 1
                    break
            else:
                invalid += 1
                break
      
        elif entry_info[0] == "ecl":
            eye_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if entry_info[1] not in eye_colour:
                invalid += 1
                break
        elif entry_info[0] == "pid":
            if len(entry_info[1]) != 9:
                invalid += 1
                break
        elif entry_info[0] == "hcl":
            if entry_info[1][0] != "#" or len(entry_info[1][1:]) != 6:
                invalid += 1
                break
        else:
            # better not be anything else
            print(entry_info[0])

                    

print((len(passport_list) - invalid))
