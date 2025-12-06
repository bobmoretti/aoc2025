import numpy as np
from math import prod


def parse(fname="input"):
    lines = open(fname).read().splitlines()
    operands = lines[-1].split()
    grid = np.array([[int(x) for x in line.split()] for line in lines[:-1]])
    return grid, operands


def parse2(fname="input"):
    lines = open(fname).read().splitlines()
    grid = np.array([np.array(list(line), dtype="U1") for line in lines])
    return grid


def part1(fname="input"):
    grid, operands = parse(fname)

    ops = {"*": prod, "+": sum}
    return int(sum(ops[op](col) for op, col in zip(operands, grid.T)))


def part2(fname="input"):
    grid = parse2(fname)
    (col_starts,) = np.where(grid[-1] != " ")
    col_starts = [int(x) for x in col_starts]
    # add a last column end since it's after the end of the array
    col_starts.append(len(grid[-1]) + 1)
    total = 0
    ops = {"*": prod, "+": sum}

    def apply_operations(start, stop, op):
        nums = grid[:-1]

        def col_to_val(col_idx):
            return int("".join(nums.T[col_idx]).strip())

        return op(col_to_val(col_idx) for col_idx in range(start, stop - 1))

    for start, stop in zip(col_starts[:-1], col_starts[1:]):
        op = ops[grid.T[start, -1]]
        total += apply_operations(start, stop, op)
    return total


print(f"{part1()=}")
print(f"{part2()=}")
