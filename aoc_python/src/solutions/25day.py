import random
from copy import deepcopy

with open("inputs/day25.txt", "r") as file:
    X = file.read().splitlines()

network_dict = {}
for line in X:
    key_component, components = line.split(": ")
    network_dict[key_component] = components.split(" ")


def make_networks(network_dict):
    init_set_list = []
    for key, value in network_dict.items():
        setje = set()
        setje.add(key)
        setje.update(value)
        last_set = None
        intersect_bool = False
        for idx, init_set in enumerate(init_set_list):
            if init_set.intersection(setje):
                intersect_bool = True
                init_set.update(setje)
                if last_set is not None:
                    init_set_list[last_set].update(init_set)
                    init_set_list.pop(idx)
                last_set = idx

        if not intersect_bool:
            init_set_list.append(setje)

    return init_set_list


def get_groups(network_dict):
    set_list = make_networks(network_dict)
    tmp_set_list = []
    while len(tmp_set_list) != 2:
        tmp_dict = deepcopy(network_dict)
        tmp_set_list = deepcopy(set_list)
        for _ in range(3):
            random_key = random.choice(list(tmp_dict.keys()))
            random_value = random.randint(0, len(tmp_dict[random_key]) - 1)
            tmp_dict[random_key].pop(random_value)
            if tmp_dict[random_key] == []:
                del tmp_dict[random_key]

        tmp_set_list = make_networks(tmp_dict)
        print(len(tmp_set_list))

    return tmp_set_list


network = make_networks(network_dict)
def dict_to_dot(graph_dict):
    dot_code = "graph G {\n"

    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            dot_code += f'  {node} -- {neighbor};'

    dot_code += "}"

    return dot_code

dot_rep = dict_to_dot(network_dict)
## Analyzed the dot language and was able to visually point out the 

# network_dict["pzl"].pop(1)
# network_dict["cmg"].pop(3)
# network_dict["jqt"].pop(2)

network_dict["tpn"].pop(0)
network_dict["zcj"].pop(0)
del network_dict["hxq"]

network = make_networks(network_dict)
print(len(network[0]) * len(network[1]))
breakpoint()
