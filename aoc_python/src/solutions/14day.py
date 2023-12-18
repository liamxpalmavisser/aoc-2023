from tqdm import tqdm

with open("inputs/day14.txt", "r") as file:
    X = file.readlines()
    X = list(map(lambda x: x.strip(), X))


def get_columns(lines: list[str]):
    col_list = []
    for j in range(len(lines)):
        col = "".join([lines[i][j] for i in range(len(lines))])
        col_list.append(col)

    return col_list


def tilt_row(row: str):
    rock_splits = row.split("#")
    tilted_split_list = []
    for rock_split in rock_splits:
        tilted_split_list.append(
            "O" * rock_split.count("O") + "." * rock_split.count(".")
        )
        tilted_row = "#".join(tilted_split_list)

    return tilted_row


def tilt_grid(grid: list[str]):
    new_grid = get_columns(grid)
    new_grid = list(map(tilt_row, new_grid))
    new_grid = get_columns(new_grid)
    return new_grid


def rotate_grid_90(grid: list[str]):
    rotated_grid = ["".join(row) for row in zip(*grid[::-1])]
    return rotated_grid


def full_rotation(grid: list[str]):
    new_grid = grid
    for _ in range(4):
        new_grid = tilt_grid(new_grid)
        new_grid = rotate_grid_90(new_grid)

    return new_grid


def convert_grid_to_string(grid: list[str]):
    grid_string = "0".join(grid)
    return grid_string


def convert_string_to_grid(grid_string: str):
    grid = grid_string.split("0")
    return grid


def get_points(grid):
    total_load = 0
    # grid = tilt_grid(grid)
    for idx, line in enumerate(grid):
        total_load += line.count("O") * (len(grid) - idx)
    return total_load


def part_two(grid_string):
    grid = convert_string_to_grid(grid_string)
    new_grid = full_rotation(grid)
    return new_grid


memory = {}
grid = X
for i in range(1, 1000000000):
    grid_string = convert_grid_to_string(grid)
    # if grid_string in memory:
    # print(f"After {i - memory[grid_string]} steps there is a loop")
    memory[grid_string] = i
    grid = part_two(grid_string)
    if i == 160:
        print(get_points(grid))
    # if get_points(grid) == 99291:
    #     print(i)

# grid = X
# for _ in range(7):
#     grid = full_rotation(grid)
#
# breakpoint()
