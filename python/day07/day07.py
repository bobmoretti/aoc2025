import numpy as np

def parse(fname):
    lines = open(fname).read().splitlines()
    grid = np.array([np.array(list(line), dtype="U1") for line in lines])
    return grid

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def plot_counts(counts):
    import matplotlib.pyplot as pl
    pl.figure(figsize=[10, 10], dpi=128)
    pl.imshow(np.log10(counts), interpolation='nearest')
    
    pl.colorbar()
    pl.title("Number of paths (log scale)")
    pl.gcf().tight_layout()
    pl.savefig("day07.png")


def find_paths(fname):
    grid = parse(fname)
    counts = np.zeros(grid.shape, np.int64)
    start = np.where(grid[0] == 'S')
    grid[1][start] = '|'
    num_splits = 0
    counts[1][start] = 1
    for cur in range(2, len(grid)):
        prev_x = grid[cur-1] == '|'
        xs = np.where(prev_x)[0]
        for x in xs:
            if grid[cur][x] == '.':
                grid[cur][x] = '|'
                counts[cur][x] = counts[cur-1][x]
        split_x = grid[cur] == '^'
        xs = np.where(split_x)[0]
        for x in xs:
            split_left = grid[cur][x-1] == '.'
            split_right = grid[cur][x+1] == '.'
            split = split_left or split_right
            if grid[cur-1][x] == '|':
                num_splits += 1
            if split_left:
                grid[cur][x-1] = '|'

            if split_right:
                grid[cur][x+1] = '|'
            counts[cur][x-1] += counts[cur-1][x]
            counts[cur][x+1] += counts[cur-1][x]
    return grid, num_splits, counts

def part2(fname):
    grid = parse(fname)
    

grid, num_splits, counts = find_paths("input")
print_grid(grid)
plot_counts(counts)

print(f"part 1: {num_splits}")
print(f"part 2: {sum(counts[-1])}")
