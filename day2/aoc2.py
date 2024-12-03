def _check_report(report: list) -> bool:
    if any(report == r for r in (sorted(report), sorted(report, reverse=True))):
        if all(0 < abs(earlier - later) <= 3 for earlier, later in zip(report, report[1:])):
            return True


def part_1(data: list) -> int:
    return sum([True for report in data if _check_report(report)])


def part_2(data: list) -> int:
    return sum(
        [
            True
            for report in data
            if _check_report(report)
            or any(_check_report(report[:idx] + report[idx + 1 :]) for idx in range(len(report)))
        ]
    )


def main():
    with open("input2.txt") as f:
        data = [list(map(int, x.strip().split(" "))) for x in f.readlines()]

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")


if __name__ == "__main__":
    main()
