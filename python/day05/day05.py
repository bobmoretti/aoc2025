def parse(fname):
    ranges, ids = open(fname).read().split("\n\n")
    ranges = ranges.splitlines()
    ids = ids.splitlines()

    def parse_range(line):
        x0, x1 = line.split("-")
        return int(x0), int(x1)

    ranges = [parse_range(line) for line in ranges]
    ids = [int(x) for x in ids]
    return ranges, ids


def is_in_range(id, r):
    r0, r1 = r
    return r0 <= id <= r1


def is_fresh(id, ranges):
    return any(is_in_range(id, r) for r in ranges)


def part1(fname="input"):
    ranges, ids = parse(fname)
    return len([id for id in ids if is_fresh(id, ranges)])


def merge_intervals(intervals):
    def first(x):
        return x[0]

    intervals_sorted = sorted(intervals, key=first)
    merged = [intervals_sorted[0]]
    for cur in intervals_sorted[1:]:
        last = merged[-1]
        should_merge = cur[0] <= last[1] + 1
        if should_merge:
            merged[-1] = (last[0], max(last[1], cur[1]))
        else:
            merged.append(cur)
    return merged


def part2(fname="input"):
    ranges, _ = parse(fname)
    intervals = []
    for r in ranges:
        intervals.append(r)
        intervals = merge_intervals(intervals)
    intervals

    return sum(x1 - x0 + 1 for x0, x1 in intervals)


print(part1())
print(part2())
