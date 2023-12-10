with open("inputs/day04.txt", "r") as file:
    X = file.readlines()


def points_from_numbers(
    winning_number_list: list[int], your_number_list: list[int]
) -> int:
    n_winning = sum([number in winning_number_list for number in your_number_list])

    if n_winning == 0:
        return 0
    else:
        points = 1
        for i in range(n_winning - 1):
            points += 2**i

        return points


def parse_numbers(line: str) -> tuple[int, list[int], list[int]]:
    card, numbers = line.split(":")
    card = int(card.split(" ")[-1])
    winning_numbers, your_numbers = map(str.split, numbers.split("|"))
    winning_numbers = map(int, winning_numbers)
    your_numbers = map(int, your_numbers)
    return card, list(winning_numbers), list(your_numbers)


def simulate_winnings(card_id, winners_dict):
    if card_id not in winners_dict or winners_dict[card_id] == 0:
        return 1

    total_winnings = 1

    for next_card_id in range(card_id + 1, card_id + 1 + winners_dict[card_id]):
        total_winnings += simulate_winnings(next_card_id, winners_dict)

    return total_winnings


def part_one(lines):
    sum_points = 0
    for line in lines:
        _, winning_numbers, your_numbers = parse_numbers(line)
        points = points_from_numbers(winning_numbers, your_numbers)

        sum_points += points
    print(sum_points)


def part_two(lines):
    total_cards = 0
    card_dict = {}
    for line in lines:
        card, winning_numbers, your_numbers = parse_numbers(line)
        n_winning = sum([number in winning_numbers for number in your_numbers])
        card_dict[card] = n_winning

    for card_id in card_dict.keys():
        total_cards += simulate_winnings(card_id, card_dict)

    print(total_cards)


def main():
    part_two(X)


if __name__ == "__main__":
    main()
