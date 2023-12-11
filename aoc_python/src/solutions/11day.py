with open("inputs/day11.txt", "r") as file:
    X = file.readlines()


def get_galaxies(lines: list[str]):
    galaxy_list = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char == "#":
                galaxy_list.append([x, y])

    return galaxy_list


def find_empty_space(galaxy_list: list[list[int]], lines: list[str]):
    x_set = set()
    y_set = set()
    for x, y in galaxy_list:
        x_set.add(x)
        y_set.add(y)

    x_empty = set()
    y_empty = set()
    for x in range(len(lines[0].strip())):
        if x not in x_set:
            x_empty.add(x)

    for y in range(len(lines)):
        if y not in y_set:
            y_empty.add(y)

    return x_empty, y_empty


def expand_galaxies(
    galaxy_list: list[list[int]], x_empty: set[int], y_empty: set[int]
) -> list[list[int]]:
    expanded_galaxy_list = []
    for x, y in galaxy_list:
        # The following can be set to 1 in case of part 1
        x = x + (1000000 - 1) * sum([x > x_0 for x_0 in x_empty])
        y = y + (1000000 - 1) * sum([y > y_0 for y_0 in y_empty])
        expanded_galaxy_list.append([x, y])

    return expanded_galaxy_list


def main():
    galaxy_list = get_galaxies(X)
    x_empty, y_empty = find_empty_space(galaxy_list, X)
    expanded_galaxy_list = expand_galaxies(galaxy_list, x_empty, y_empty)
    distance_list = []
    for i in range(len(expanded_galaxy_list)):
        distance_list.extend(
            [
                sum(
                    [
                        abs(x1 - x2)
                        for x1, x2 in zip(
                            expanded_galaxy_list[i], expanded_galaxy_list[i + j]
                        )
                    ]
                )
                for j in range(1, len(expanded_galaxy_list) - i)
            ]
        )
    print(sum(distance_list))


if __name__ == "__main__":
    main()
