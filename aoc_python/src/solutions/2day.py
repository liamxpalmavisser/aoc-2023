from dataclasses import dataclass


@dataclass
class Color:
    name: str
    value: int


@dataclass
class Set:
    colors: list[Color]


@dataclass
class Game:
    id: int
    sets: list[Set]


def parse_color(color_str):
    value, name = color_str.strip().split()
    return Color(name, int(value))


def parse_set(set_str):
    color_strs = set_str.split(", ")
    colors = [parse_color(color_str) for color_str in color_strs]
    return Set(colors)


def parse_game(game_str):
    game_name, sets_str = game_str.split(": ")
    set_strs = sets_str.split("; ")
    sets = [parse_set(set_str) for set_str in set_strs]
    game = game_name.split(" ")[-1]
    return Game(game, sets)


def is_set_too_big(max_set: list[Color], set2: list[Color]) -> bool:
    max_color_dict = {color.name: color.value for color in max_set}
    set_color_dict = {color.name: color.value for color in set2}

    for color, count in set_color_dict.items():
        if count > max_color_dict[color]:
            return True
    return False


with open("inputs/day02.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    games = [parse_game(line) for line in lines]


def main():
    oversized_games = 0
    for game in games:
        max_set = [Color("red", 12), Color("green", 13), Color("blue", 14)]
        for setje in game.sets:
            if is_set_too_big(max_set, setje.colors):
                oversized_games += int(game.id)
                break

    print(oversized_games)


if __name__ == "__main__":
    main()
