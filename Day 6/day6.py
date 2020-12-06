with open("day6.txt", "r") as file1:
    new_list = file1.read()

new_list = new_list.split("\n\n")
char_list = []
yes_count = 0

for group in new_list:
    person_list = group.split()

    group_yes = list(person_list[0])

    for person in person_list:
        to_remove = []
        for yes in group_yes:
            if yes not in person:
                to_remove.append(yes)
        for rev in to_remove:
            group_yes.remove(rev)

    yes_count += len(group_yes) 

    char_list = []

print(yes_count)
