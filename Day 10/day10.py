with open("day10.txt", "r") as file1:
    list1 = file1.read()

joltage = list1.split()
joltage = [int(n) for n in joltage]
joltage.append(0)
joltage.append(max(joltage) + 3)

sorted_list = sorted(joltage)

diff_of_one = 0
diff_of_three = 0

for i in range(0, len(sorted_list) - 1):
    if sorted_list[i] + 1 == sorted_list[i+1]:
        diff_of_one += 1
    elif sorted_list[i] + 3 == sorted_list[i+1]:
        diff_of_three += 1
    else:
        continue

print(diff_of_one, diff_of_three, diff_of_one*diff_of_three)

new_sorted_list = set(sorted_list)
tree = [0] * (max(sorted_list) + 4)
tree[0] = 1

for i in range(len(tree)):

    tree[i] += tree[i-1] if i-1 in new_sorted_list else 0
    tree[i] += tree[i-2] if i-2 in new_sorted_list else 0
    tree[i] += tree[i-3] if i-3 in new_sorted_list else 0

print(tree[-1])


