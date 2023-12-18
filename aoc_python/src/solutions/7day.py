from dataclasses import dataclass, field

with open("inputs/day07.txt", "r") as file:
    X = file.readlines()

cardcharacters = "J23456789TQKA"


@dataclass
class Hand:
    cards: str
    type = None
    strengths: list[int] = field(default_factory=list)
    card_dict: dict = field(default_factory=dict)

    def card_strength(self, char: str) -> int:
        match char:
            case "J":
                return 0
            case "2":
                return 1
            case "3":
                return 2
            case "4":
                return 3
            case "5":
                return 4
            case "6":
                return 5
            case "7":
                return 6
            case "8":
                return 7
            case "9":
                return 8
            case "T":
                return 9
            case "Q":
                return 10
            case "K":
                return 11
            case _:
                return 12

    def get_card_dict(self):
        self.card_dict: dict[str, int] = {}
        for card in self.cards:
            self.strengths.append(self.card_strength(card))

            if card not in self.card_dict:
                self.card_dict[card] = 1
            else:
                self.card_dict[card] += 1

    def check_type(self):
        if len(set(self.cards)) == 1:
            self.type = 6

        if len(set(self.cards)) == 5:
            self.type = 0

        self.get_card_dict()

        if (len(self.card_dict) == 2) & (1 in set(self.card_dict.values())):
            self.type = 5

        if (len(self.card_dict) == 2) & (3 in set(self.card_dict.values())):
            self.type = 4

        if (len(self.card_dict) == 3) & (3 in set(self.card_dict.values())):
            self.type = 3

        if (len(self.card_dict) == 3) & (max(self.card_dict.values()) == 2):
            self.type = 2

        if len(self.card_dict) == 4:
            self.type = 1


def make_ranking(hands: list[Hand], bids: list[int]):
    hand_bid_combo = list(zip(hands, bids))
    sorted_hands = sorted(
        hand_bid_combo,
        key=lambda x: (-x[0].type, *[-strength for strength in x[0].strengths]),
    )

    sorted_bids = [int(bid[1]) for bid in sorted_hands]
    return sorted_bids


hand_list = []
bid_list = []
for line in X:
    hand, bid = line.split(" ")
    hand = Hand(hand)
    hand.check_type()
    hand_list.append(hand)
    bid_list.append(bid)

sorted_bids = make_ranking(hand_list, bid_list)
total_winnings = 0
for i in range(len(sorted_bids)):
    total_winnings += sorted_bids[i] * (len(sorted_bids) - i)


print(total_winnings)
