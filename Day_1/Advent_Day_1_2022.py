# Opening the file as an object (strings)
with open("input_d1.txt") as file_object:
    # define object as a string variable
    calorie_string = file_object.read()
    # split by empty line \n\n and store as a list of strings
    cal_list = calorie_string.split("\n\n")
    # check separation by printing
    # print(cal_list)
    # empty list
    elf_list = []
    # loop through list "elf" is a new variable
    for elf in cal_list:
        # separate by line \n create list of foods
        foods = elf.split("\n")
        # convert str list to int list    ration as new variable.
        int_foods = [int(ration) for ration in foods]
        # sum the rations
        sum_rations = sum(int_foods)
        # add sum to new list elf_list
        elf_list.append(sum_rations)
    print("\n\n\n")
    # highest amount of calories
    best_elf = max(elf_list)
    print(best_elf)


# part two: pop highest count from list and store as variable.
# pop int from elf_list, the index of the int in list is the index of highest int in the elf_list.
first_elf = elf_list.pop(elf_list.index(max(elf_list)))
sec_elf = elf_list.pop(elf_list.index(max(elf_list)))
third_elf = elf_list.pop(elf_list.index(max(elf_list)))

print(first_elf)
print("\n")
print(sec_elf)
print("\n")
print(third_elf)
print("\n The sum of the highest calories is:")
print(first_elf + sec_elf + third_elf)








