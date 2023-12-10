from itertools import islice
from dataclasses import dataclass


def parse(line: str) -> list[int]:
    line = line.strip()
    characters = line.split(" ")
    numbers = [int(number) for number in characters]
    return numbers


with open("inputs/day09.txt", "r") as file:
    lines = map(parse, file.readlines())
    X = list(lines)


class History:
    def __init__(self, values: list[int]):
        self.values = values
        self.layers: list[list[int]] = [values]

    def _add_layer(self, values) -> list[int]:
        return [values[i + 1] - values[i] for i in range(len(values) - 1)]

    def add_layers(self):
        if self.layers == []:
            self.layers.append(self._add_layer(self.values))
        else:
            i = 1
            while not all(element == 0 for element in self.layers[-1]):
                self.layers.append(self._add_layer(self.layers[i - 1]))
                i += 1

    def add_extras(self):
        self.layers[-1].append(0)
        for i in range(len(self.layers) - 1):
            self.layers[-i - 2].append(
                self.layers[-i - 2][-1] + self.layers[-i - 1][-1]
            )

    def add_extras_backwards(self):
        self.layers[-1] = [0] + self.layers[-1]
        for i in range(len(self.layers) - 1):
            self.layers[-i - 2].insert(
                0, self.layers[-i - 2][0] - self.layers[-i - 1][0]
            )


def part_one():
    last_extra_sum = 0
    for values in X:
        history = History(values)
        history.add_layers()
        history.add_extras()
        last_extra_sum += history.values[-1]
        # breakpoint()

    print(last_extra_sum)


def part_two():
    last_extra_sum = 0
    for values in X:
        history = History(values)
        history.add_layers()
        history.add_extras_backwards()
        last_extra_sum += history.values[0]
        # breakpoint()

    print(last_extra_sum)


def main():
    part_two()


if __name__ == "__main__":
    main()
