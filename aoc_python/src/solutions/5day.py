from functools import cache
from tqdm import tqdm

with open("inputs/day05.txt", "r") as file:
    X = file.readlines()


def parse(lines):
    seedlist = map(int, lines[0].strip().split(": ")[1].split(" "))
    seed_map: list[list[list[int]]] = []
    for line in lines[1:]:
        if line[0].isdigit():
            seed_map[-1].extend([list(map(int, line.strip().split(" ")))])
        if line == "\n":
            seed_map.append([])

    location_list = []
    seedlist = list(seedlist)
    real_seedlist = seedlist[::2]
    range_list = seedlist[1::2]

    maps = seed_map

    # @cache
    # def apply_range_map(seed, ranges):
    #     if apply_map(maps, seed) == (apply_map(maps, seed + ranges) + ranges):
    #         return apply_map(maps, seed)
    #
    #
    #     mid = seed + ranges // 2
    #
    #
    #     if apply_map(maps, seed) == (apply_map(maps, mid) + mid):
    #         return apply_map(maps, seed)
    #
    #     if apply_map(maps, mid) == (apply_map(maps, seed + ranges) + ranges):
    #         return apply_map(maps, mid)
    #
    #     left_result = apply_range_map(seed, ranges // 2)
    #     right_result = apply_range_map(mid, ranges // 2)
    #
    #     return min([left_result, right_result])
    @cache
    def apply_map(seed: int, i=0):
        if i == len(maps):
            return seed
        current_map = maps[i]
        for mapje in current_map:
            if mapje[1] <= seed <= mapje[1] + mapje[2]:
                i += 1
                return apply_map(seed=(seed + mapje[0] - mapje[1]), i=i)
        i += 1
        return apply_map(seed=seed, i=i)

    @cache
    def apply_range_map(seed, ranges):
        # print(f"Depth: {depth}, Seed: {seed}, Ranges: {ranges}")

        if apply_map(seed) == (apply_map(seed + ranges) + ranges):
            return apply_map(seed)

        mid = seed + ranges // 2

        if apply_map(seed) == (apply_map(mid) + mid):
            return apply_map(seed)

        if apply_map(mid) == (apply_map(seed + ranges) + ranges):
            return apply_map(mid)

        # Increment the depth for recursive calls
        left_result = apply_range_map(seed, ranges // 2)
        right_result = apply_range_map(mid, ranges // 2)

        return min([left_result, right_result])

    for seed, ranges in tqdm(zip(real_seedlist, range_list)):
        location_list.append(apply_range_map(seed, ranges))

    print(min(location_list))

    # for seed in seedlist:
    #     location_list.append(apply_map(seed_map, seed))
    #
    # print(location_list)


parse(X)
