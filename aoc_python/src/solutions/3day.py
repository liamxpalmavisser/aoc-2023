with open("inputs/day03.txt", "r") as file:
    X = file.read().splitlines()

digit_list = []
location_list = []
last_char = ""
for idy, line in enumerate(X):
    for idx, char in enumerate(line):
        if char.isdigit():
            if last_char.isdigit():
                digit_list[-1] = digit_list[-1] + char
            else:
                location_list.append((idy, idx))
                digit_list.append(char)
        last_char = char


loc_dict = {}
for idx, (location, digit) in enumerate(zip(location_list, digit_list)):
    for i in range(len(digit)):
        loc_dict[(location[0], location[1] + i)] = str(idx * "0") + digit

adjacent_set = set({})
gear_ratio_list = []

for idy, line in enumerate(X):
    for idx, char in enumerate(line):
        new_set = adjacent_set.copy()
        if not char.isdigit() and char != ".":
            if (idy, idx + 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy, idx + 1)])
            if (idy, idx - 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy, idx - 1)])
            if (idy + 1, idx - 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy + 1, idx - 1)])
            if (idy - 1, idx - 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy - 1, idx - 1)])
            if (idy + 1, idx) in loc_dict:
                adjacent_set.add(loc_dict[(idy + 1, idx)])
            if (idy - 1, idx) in loc_dict:
                adjacent_set.add(loc_dict[(idy - 1, idx)])
            if (idy - 1, idx + 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy - 1, idx + 1)])
            if (idy + 1, idx + 1) in loc_dict:
                adjacent_set.add(loc_dict[(idy + 1, idx + 1)])

            # Following is for part 2
            if not len(adjacent_set) - len(new_set) == 2:
                adjacent_set = new_set
            else:
                gear_ratios = [int(x) for x in (adjacent_set - new_set)]
                gear_ratio = gear_ratios[0] * gear_ratios[1]
                gear_ratio_list.append(gear_ratio)


# Below is for part 1
# adjacent_sum = sum([int(i) for i in adjacent_set])
# print(adjacent_sum)
print(sum(gear_ratio_list))
