from itertools import product
import copy
from tqdm import tqdm

with open("inputs/day22.txt", "r") as file:
    X = file.read().splitlines()


def parse(lines):
    brick_dict = {}
    for idx, line in enumerate(lines):
        # bricks, brick_name = line.split("   <- ")
        bricks_coords = [item.split(",") for item in line.split("~")]

        x_range = [int(bricks_coords[0][0]), int(bricks_coords[1][0])]
        y_range = [int(bricks_coords[0][1]), int(bricks_coords[1][1])]
        z_range = [int(bricks_coords[0][2]), int(bricks_coords[1][2])]
        # brick_dict[brick_name] = {"x": x_range, "y": y_range, "z": z_range}
        brick_dict[idx] = {"x": x_range, "y": y_range, "z": z_range}

        # Sort the bricks on z level
        brick_dict = dict(sorted(brick_dict.items(), key=lambda item: item[1]["z"][0]))
    return brick_dict


brick_dict = parse(X)


def drop_bricks(brick_dict: dict):
    brick_dict_copy = copy.deepcopy(brick_dict)
    min_z = min(value["z"][0] for value in brick_dict_copy.values())
    max_z = max(value["z"][-1] for value in brick_dict_copy.values())
    z_values = list(range(min_z, max_z + 1))
    layer_list = [set() for z in z_values]
    for z_value in z_values:
        for brick, coords in brick_dict_copy.items():
            x_values_brick = list(range(coords["x"][0], coords["x"][1] + 1))
            y_values_brick = list(range(coords["y"][0], coords["y"][1] + 1))
            z_values_brick = list(range(coords["z"][0], coords["z"][1] + 1))
            if z_value in z_values_brick:
                layer_coords = list(product(x_values_brick, y_values_brick))
                layer_list[z_value - min_z].update(layer_coords)

            if z_value in z_values_brick and z_value > 1 and z_value < len(z_values):
                if not set(product(x_values_brick, y_values_brick)).intersection(
                    layer_list[z_value - min_z - 1]
                ):
                    # print(
                    #     f"Brick {brick} has z_values {z_values_brick}. This fits into the lower layer of z: {z_value - 1}"
                    # )
                    brick_dict_copy[brick]["z"] = [
                        coords["z"][0] - 1,
                        coords["z"][1] - 1,
                    ]

    return brick_dict_copy


def recursive_function(brick_dict):
    print("-")
    if brick_dict == drop_bricks(brick_dict):
        return brick_dict

    else:
        return recursive_function(drop_bricks(brick_dict))


print("Dropping bricks")
dropped_bricks_dict = recursive_function(brick_dict)


def disintegrate(brick_dict):
    n_bricks = len(brick_dict.keys())
    for key_ in tqdm(brick_dict.keys()):
        new_dict = {key: value for key, value in brick_dict.items() if key != key_}
        if new_dict != drop_bricks(new_dict):
            n_bricks -= 1

    return n_bricks


print(disintegrate(dropped_bricks_dict))
