import re


def _mul_op(operation) -> int:
    left_op, right_op = operation.replace("mul(", "").replace(")", "").split(",")
    return int(left_op) * int(right_op)


def part_1(data) -> int:
    return sum([_mul_op(match) for line in data for match in re.findall(r"mul\(\d+,\d+\)", line)])


def part_2(data) -> int:
    sum = 0
    enabled = True
    for match in [match for line in data for match in re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line)]:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled:
            left_op, right_op = match.replace("mul(", "").replace(")", "").split(",")
            sum += int(left_op) * int(right_op)
    return sum


def main():
    with open("input3.txt") as f:
        data = f.readlines()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
