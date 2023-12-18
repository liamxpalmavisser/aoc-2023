from tqdm import tqdm

with open("inputs/day16.txt", "r") as file:
    grid = file.read().splitlines()


def reflect(char, dir):
    match char, dir:
        case "\\", "south":
            return "east"
        case "\\", "north":
            return "west"
        case "\\", "east":
            return "south"
        case "\\", "west":
            return "north"
        case "/", "south":
            return "west"
        case "/", "north":
            return "east"
        case "/", "east":
            return "north"
        case "/", "west":
            return "south"
        case "|", ("east" | "west"):
            return "north", "south"
        case "-", ("south" | "north"):
            return "east", "west"
        case _:
            return dir


contrap_dict: dict[tuple, str] = {}
for idy, line in enumerate(grid):
    for idx, symbol in enumerate(line):
        if symbol != ".":
            contrap_dict[(idy, idx)] = symbol


def move_dir(loc: tuple[int, int], dir: str):
    match dir:
        case "south":
            loc = (loc[0] + 1, loc[1])
        case "north":
            loc = (loc[0] - 1, loc[1])
        case "east":
            loc = (loc[0], loc[1] + 1)
        case "west":
            loc = (loc[0], loc[1] - 1)
    return loc


def traverse(loc, dir, trav_loc: set = {(0, 0)}, memory={}):
    if not loc in memory or memory[loc] != dir:
        memory[loc] = dir
    else:
        return trav_loc

    loc = move_dir(loc, dir)
    while loc not in contrap_dict:
        if 0 > loc[0] or loc[0] >= len(grid) or 0 > loc[1] or loc[1] >= len(grid[0]):
            return trav_loc
        else:
            trav_loc.add(loc)
        loc = move_dir(loc, dir)

    dir = reflect(contrap_dict[loc], dir)
    trav_loc.add(loc)
    if isinstance(dir, tuple):
        dir1, dir2 = dir
        return traverse(loc, dir1, trav_loc, memory=memory).union(
            traverse(loc, dir2, trav_loc, memory=memory)
        )
    else:
        return traverse(loc, dir, trav_loc=trav_loc, memory=memory)


def part_one():
    lox = traverse((0, 0), "south")
    print(len(lox))


def part_two():
    traverse_list = []
    for i in tqdm(range(len(grid[0]))):
        traverse_list.append(
            len(traverse((0, i), "south", trav_loc={(0, i)}, memory={}))
        )

    for i in tqdm(range(len(grid[0]))):
        traverse_list.append(
            len(
                traverse(
                    (len(grid) - 1, i), "north", trav_loc={(len(grid), i)}, memory={}
                )
            )
        )

    for i in tqdm(range(len(grid))):
        traverse_list.append(
            len(traverse((i, 0), "east", trav_loc={(i, 0)}, memory={}))
        )

    for i in tqdm(range(len(grid))):
        traverse_list.append(
            len(
                traverse(
                    (i, len(grid) - 1), "west", trav_loc={(i, len(grid) - 1)}, memory={}
                )
            )
        )

    print(max(traverse_list))
