def _check_report(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(0 < abs(earlier - later) <= 3 for earlier, later in zip(report, report[1:])):
            return True


def part_1(data):
    return sum([True for report in data if _check_report(report)])


def part_2(data):
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

    print(part_2(data))


if __name__ == "__main__":
    main()
