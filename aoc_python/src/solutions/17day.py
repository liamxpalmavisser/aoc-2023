import heapq

with open("inputs/day17.txt", "r") as file:
    X = file.read().splitlines()
    grid = [[int(char) for char in line] for line in X]

dir_dict = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}
end_node = (len(grid) - 1, len(grid[0]) - 1)


def dijkstra(grid, mmin, mmax):
    visited = set()
    directions_to_go = [(0, 0, 0, dir_dict["east"], 1), (0, 0, 0, dir_dict["south"], 1)]

    while len(directions_to_go) > 0:
        heat_loss, y, x, direction, total_direction = heapq.heappop(directions_to_go)

        if (y, x, direction, total_direction) in visited:
            continue
        else:
            visited.add((y, x, direction, total_direction))

        if total_direction > mmax:
            continue

        loc = (y + direction[0], x + direction[1])

        if (
            loc[0] < 0
            or loc[0] >= len(grid)
            or loc[1] < 0
            or loc[1] >= len(grid[0])
        ):
            continue

        heat_loss += grid[loc[0]][loc[1]]

        if (
            total_direction >= mmin
            and loc[0] == end_node[0]
            and loc[1] == end_node[1]
        ):
            return heat_loss

        for dir in dir_dict.values():
            if dir[0] + direction[0] == 0 and dir[1] + direction[1] == 0:
                continue
            if dir != direction and total_direction < mmin:
                continue
            if dir != direction:
                new_total_dir = 1
            else:
                new_total_dir = total_direction + 1

            heapq.heappush(
                directions_to_go, (heat_loss, loc[0], loc[1], dir, new_total_dir)
            )


def main():
    # print(dijkstra(grid, 0, 3))
    print(dijkstra(grid, 4, 10))


main()
