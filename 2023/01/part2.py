DIGIT_MAP = {
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

REVERSED_DIGIT_MAP = {word[::-1]: digit for word, digit in DIGIT_MAP.items()}


def extract_value(text, digit_map):
    for index, char in enumerate(text):
        if char.isdigit():
            return char
        for num_word in digit_map:
            if text[index:].startswith(num_word):
                return digit_map[num_word]


total_sum = 0
with open("input/input.txt", "r") as file:
    for line in file:
        first_value = extract_value(line, DIGIT_MAP)
        last_value = extract_value(line[::-1], REVERSED_DIGIT_MAP)
        total_sum += int(first_value + last_value)

print(total_sum)
