from math import gcd
from dataclasses import dataclass

with open("inputs/day08.txt", "r") as file:
    X = file.readlines()


@dataclass
class Node:
    L: str
    R: str


def parse_sequence(lines) -> str:
    return lines[0].strip()


def parse_nodes(lines) -> dict[str, Node]:
    return {
        node: Node(*map(str.strip, definition_str[1:-1].split(",")))
        for node, definition_str in (line.strip().split(" = ") for line in lines[2:])
    }


def traverse_node(
    sequence: str, nodes: dict[str, Node], start_node: str, part: int
) -> tuple[int, str]:
    current_node = start_node
    for n_char, char in enumerate(sequence):
        current_node = getattr(nodes[current_node], char)

        if current_node.endswith("ZZZ" if part == 1 else "Z"):
            return n_char + 1, current_node

    return n_char + 1, current_node


def find_lcm_of_list(numbers) -> int:
    result = numbers[0]
    for n in numbers[1:]:
        result = abs(result * n) // gcd(result, n)

    return result


def part_one(lines):
    sequence = parse_sequence(lines)
    nodes = parse_nodes(lines)

    # The 100 is a bit goofy but it makes the code much easier to read
    n_char, _ = traverse_node(sequence * 100, nodes, "AAA", part=1)
    print(n_char)


def part_two(lines):
    sequence = parse_sequence(lines)
    nodes = parse_nodes(lines)

    start_nodes = [node for node in nodes if node.endswith("A")]
    n_steps_list = [
        traverse_node(sequence * 100, nodes, start_node, part=2)[0]
        for start_node in start_nodes
    ]

    result_lcm = find_lcm_of_list(n_steps_list)
    print(result_lcm)


def main():
    part_two(X)


if __name__ == "__main__":
    main()
