from types import resolve_bases
from typing import Union

with open("inputs/day01.txt", "r") as file:
    X = file.readlines()

pattern_dict: dict[str, str] = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern_set = set(pattern_dict)


def is_digit_in_string(input_str: str) -> Union[str, None]:
    for pattern in pattern_set:
        if pattern in input_str:
            return pattern_dict[pattern]
    return None


def extract_first_left_digit(input_string: str) -> Union[str, None]:
    spelled_out_int_list: list[str] = []
    for char in input_string:
        if char.isdigit():
            return char
        else:
            spelled_out_int_list.append(char)
            if is_digit_in_string("".join(spelled_out_int_list)):
                return is_digit_in_string("".join(spelled_out_int_list))
    return None


def extract_first_right_digit(input_string: str) -> Union[str, None]:
    spelled_out_int_list: list[str] = []
    for char in reversed(input_string):
        if char.isdigit():
            return char
        else:
            spelled_out_int_list.append(char)
            if is_digit_in_string("".join(reversed(spelled_out_int_list))):
                return is_digit_in_string("".join(reversed(spelled_out_int_list)))
    return None


def main(input: list[str]):
    relevant_digits: list[int] = []
    for line in input:
        left_digit = extract_first_left_digit(line)
        right_digit = extract_first_right_digit(line)

        assert (
            left_digit is not None and right_digit is not None
        ), "Something ain't right"

        total_digits = int(left_digit + right_digit)
        relevant_digits.append(total_digits)
    print(sum(relevant_digits))  # Print the individual total_digits, not the list


main(X)
