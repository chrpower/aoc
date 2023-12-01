def extract_digit(text):
    for char in text:
        if char.isdigit():
            return char


total_sum = 0
with open("input/input.txt", "r") as file:
    for line in file:
        first_digit = extract_digit(line)
        last_digit = extract_digit(line[::-1])
        total_sum += int(first_digit + last_digit)

print(total_sum)
