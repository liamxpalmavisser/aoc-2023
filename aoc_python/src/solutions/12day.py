from os import confstr
from typing import Callable
from tqdm import tqdm
from functools import cache


with open("inputs/day12.txt", "r") as file:
    X = file.readlines()


@cache
def find_possibilities(spring_conf, records):
    result = 0

    if spring_conf == "":
        if records == ():
            return 1
        else:
            return 0

    if records == ():
        if "#" in spring_conf:
            return 0
        else:
            return 1

    if spring_conf[0] in ".?":
        result += find_possibilities(spring_conf[1:], records)

    if spring_conf[0] in "#?":
        if (
            (len(spring_conf) >= records[0])
            and ("." not in spring_conf[: records[0]])
            and (len(spring_conf) == records[0] or not spring_conf[records[0]] == "#")
        ):
            result += find_possibilities(spring_conf[records[0] + 1 :], records[1:])
    return result


def parse(lines):
    spring_confs = []
    records_list = []
    for line in lines:
        spring_conf, records = line.split()
        records = tuple(map(int, records.split(",")))
        spring_confs.append(spring_conf)
        records_list.append(records)
    return spring_confs, records_list


def part_one(lines):
    possibility_sum = 0
    spring_confs, records = parse(lines)
    for spring_conf, record in zip(spring_confs, records):
        possibility_sum += find_possibilities(spring_conf, record)
    print(possibility_sum)


def part_two(lines):
    possibility_sum = 0
    spring_confs, records = parse(lines)
    for spring_conf, record in zip(spring_confs, records):
        spring_conf = "?".join([spring_conf] * 5)
        record = record * 5

        possibility_sum += find_possibilities(spring_conf, record)
    print(possibility_sum)


def main():
    part_two(X)


if __name__ == "__main__":
    main()
