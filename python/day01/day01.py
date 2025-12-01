import numpy as np


def parse(filename="day01.txt"):
    def parse_line(line):
        sign = -1 if line[0] == "L" else 1
        return sign * int(line[1:])

    lines = open(filename).read().splitlines()
    return np.array([50] + [parse_line(l) for l in lines])


def part1():
    deltas = parse()
    states = np.cumsum(deltas) % 100
    print(np.sum(states == 0))


def part2():
    deltas = parse()
    states = np.cumsum(deltas)
    total_zero_crossings = sum(np.abs(np.diff(states // 100)))

    # Because we represented the states canonically from 0..99 inclusive, integer
    # division will see the rollover from 99 back to 0 and correctly count the
    # number of zero crossings.

    # But for left turns, we both overcounted and undercounted.
    (left_turns,) = np.where(deltas < 0)
    # if we landed directly on a zero during a left rotation, we need to count that
    left_undercounts = sum(states[left_turns] % 100 == 0)
    # BUT now we've counted some of those twice, so we need to remove cases where
    # we had previously landed directly on a zero during a left rotation
    left_overcounts = sum(states[left_turns - 1] % 100 == 0)
    print(total_zero_crossings + left_undercounts - left_overcounts)


part1()
part2()
