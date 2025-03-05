
def create_rules_and_updates():
    rules = {}
    updates = []
    with open("day5/input.txt", "r") as file:
        for line in file.readlines():
            if "|" in line:
                tmp = line.strip("\n").split("|")
                print(tmp)
                if rules.get(tmp[0]) == None:
                    rules[tmp[0]] = [tmp[1]]
                else:
                    rules[tmp[0]].append(tmp[1])
            elif line != "\n":
                updates.append(line.strip("\n").split(","))
    print(rules, updates)
    return rules, updates

def remove_unnecessary(rules, update):
    new_rules = {}
    for page in update:
        items = rules.get(page)
        new_rules[page] = []
        for page_1 in update:
            if items != None:
                if page_1 in items:
                    new_rules[page].append(page_1)
    return new_rules

def order_an_update(rules, update):
    new_rules = remove_unnecessary(rules, update)
    ordered_update = len(update)*[None]
    for key, item in new_rules.items():
        ordered_update[len(ordered_update) - len(item) -1] = key
    #print(new_rules)
    #for key, item in new_rules.items():
     #   print(key, item)
      #  if len(item) == int(update_len/2):
       #     mid = int(key)
        #    print(mid)
         #   break
    #print(f"LOL: {ordered_update}")
    return ordered_update

def check(update, ordered_update):
    return update == ordered_update

def get_mid(ordered_update):
    return int(ordered_update[int(len(ordered_update)/2)])

def main():
    score = 0
    score1 = 0
    rules, updates = create_rules_and_updates()
    for update in updates:
        tmp =  order_an_update(rules, update)
        if check(update, tmp):
            score += get_mid(tmp)
        else:
            score1 += get_mid(tmp)
    return score1
print(main())