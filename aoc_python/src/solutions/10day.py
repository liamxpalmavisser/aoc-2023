from math import perm


with open("inputs/day10.txt", "r") as file:
    X = file.readlines()

grid = [[char for char in line] for line in X]


class Tile:
    def __init__(
        self,
        symbol: str,
        location: list[int],
        prev_outgoing_dir: str,
    ) -> None:
        self.symbol = symbol
        self.location = location
        self.prev_outgoing_dir = prev_outgoing_dir
        self.incoming_dir: None | str = None
        self.outgoing_dir: None | str = None

    def _prev_loc_to_dir(self):
        match self.prev_outgoing_dir:
            case "north":
                self.incoming_dir = "south"
            case "east":
                self.incoming_dir = "west"
            case "south":
                self.incoming_dir = "north"
            case "west":
                self.incoming_dir = "east"

    def _symbol_action(self):
        self._prev_loc_to_dir()
        match self.symbol, self.incoming_dir:
            case ("|", "north"):
                self.outgoing_dir = "south"
            case ("|", "south"):
                self.outgoing_dir = "north"
            case ("-", "east"):
                self.outgoing_dir = "west"
            case ("-", "west"):
                self.outgoing_dir = "east"
            case ("L", "north"):
                self.outgoing_dir = "east"
            case ("L", "east"):
                self.outgoing_dir = "north"
            case ("J", "north"):
                self.outgoing_dir = "west"
            case ("J", "west"):
                self.outgoing_dir = "north"
            case ("7", "south"):
                self.outgoing_dir = "west"
            case ("7", "west"):
                self.outgoing_dir = "south"
            case ("F", "south"):
                self.outgoing_dir = "east"
            case ("F", "east"):
                self.outgoing_dir = "south"
            case ("S", _):
                self.outgoing_dir = self.outgoing_dir
            case (_, _):
                self.outgoing_dir = "wrong turn"

    def next_location(self):
        self._symbol_action()
        match self.outgoing_dir:
            case "north":
                new_location: list[int] = [
                    x + y for x, y in zip(self.location, [0, -1])
                ]
            case "east":
                new_location: list[int] = [x + y for x, y in zip(self.location, [1, 0])]
            case "south":
                new_location: list[int] = [x + y for x, y in zip(self.location, [0, 1])]
            case "west":
                new_location: list[int] = [
                    x + y for x, y in zip(self.location, [-1, 0])
                ]

        return new_location


def find_symbol(grid: list[list[str]], symbol: str = "S"):
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == symbol:
                return row_idx, col_idx
    return None


def traverse_loop(
    grid: list[list[str]],
    start_location: tuple[int, int],
    prev_outgoing_dir: str = "east",
):
    x, y = start_location
    n = 1
    while grid[y][x] != "S":
        tile = Tile(
            symbol=grid[y][x], location=[x, y], prev_outgoing_dir=prev_outgoing_dir
        )
        x, y = tile.next_location()
        prev_outgoing_dir = tile.outgoing_dir
        n += 1
        print(tile.symbol, n)

    return n


def part_one():
    if grid is not None:
        y, x = find_symbol(grid)
    for dir in ["north", "east", "south", "west"]:
        if dir == "north":
            new_x, new_y = x, y - 1
        if dir == "east":
            new_x, new_y = x + 1, y
        if dir == "south":
            new_x, new_y = x, y + 1
        if dir == "west":
            new_x, new_y = x - 1, y

        tile = Tile(
            symbol=grid[new_y][new_x], location=[new_x, new_y], prev_outgoing_dir=dir
        )
        # breakpoint()
        tile._symbol_action()
        if tile.outgoing_dir != "wrong turn":
            x, y = tile.location
            break

    n = traverse_loop(grid, start_location=[x, y], prev_outgoing_dir=dir)
    print(n / 2)


part_one()
