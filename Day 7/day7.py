with open("day7.txt", 'r') as f:
    rules = f.readlines()


rule_set = {}

for rule in rules:
    
    key, contains = rule.split(" bags contain ")
    ibs = contains.split(", ")

    for i in range(len(ibs)):
        clean_val = ibs[i][:ibs[i].rfind(' ')]

        if clean_val != "no other":
            num = int(clean_val[:ibs[i].find(' ')])
            col = clean_val[ibs[i].find(' ') + 1:]
            ibs[i] = (num, col)
        else:
            ibs[i] = None

    rule_set[key] = ibs

### Part 1

# Bags to find
btf = ["shiny gold"]
bf = []

while btf != []:
    bag = btf.pop()
    for k, v in rule_set.items():
        if v == [None]:
            continue

        found = False
        for b in v:
            if b[1] == bag:
                found = True

        if found and k not in bf:
            btf.append(k)
            bf.append(k)

print(len(bf))

### Part 2

def countBags2(bag):
    if rule_set[bag] == [None]:
        return 1

    sc = 0
    for s in rule_set[bag]:
        sc += s[0] * countBags2(s[1])

    return 1 + sc

print(countBags2("shiny gold") - 1)
