from dataclasses import dataclass


@dataclass
class Color:
    name: str
    value: int


@dataclass
class Set:
    colors: list[Color]

    def to_dict(self):
        return {color.name: color.value for color in self.colors}


@dataclass
class Game:
    id: int
    sets: list[Set]

    def get_largest_set(self) -> dict:
        return {
            color: max(
                set_instance.to_dict().get(color, 0) for set_instance in self.sets
            )
            for color in {
                color.name
                for set_instance in self.sets
                for color in set_instance.colors
            }
        }


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


def power(largest_color: dict) -> int:
    power = 1
    for n_cubes in largest_color.values():
        power *= n_cubes

    return power


def is_set_playable(max_set: list[Color], set2: Set) -> bool:
    max_color_dict = {color.name: color.value for color in max_set}
    set_color_dict = set2.to_dict()

    return all(
        count <= max_color_dict.get(color, 0) for color, count in set_color_dict.items()
    )


def part_one(lines):
    games = [parse_game(line) for line in lines]
    playable_games = 0
    max_set = [Color("red", 12), Color("green", 13), Color("blue", 14)]
    for game in games:
        if all(is_set_playable(max_set, set_instance) for set_instance in game.sets):
            playable_games += int(game.id)
    print(playable_games)


def part_two(lines):
    games = [parse_game(line) for line in lines]
    power_sum = sum(power(game.get_largest_set()) for game in games)
    print(power_sum)


def main():
    with open("inputs/day02.txt", "r") as file:
        lines = file.readlines()

    part_one(lines)


if __name__ == "__main__":
    main()
