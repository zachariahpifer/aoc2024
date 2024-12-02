def part_1(left_list: list, right_list: list) -> int:
    return sum([abs(int(left) - int(right)) for left, right in zip(sorted(left_list), sorted(right_list))])


def part_2(left_list: list, right_list: list) -> int:
    return sum([int(val) * right_list.count(val) for val in left_list])


def main() -> None:
    with open("input.txt") as f:
        left_list, right_list = zip(*(i.rstrip().split("   ") for i in f.readlines()))

    print(f"Part 1: {part_1(left_list, right_list)}")
    print(f"Part 2: {part_2(left_list, right_list)}")


if __name__ == "__main__":
    main()
