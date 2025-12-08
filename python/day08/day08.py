from math import prod
import numpy as np
from itertools import combinations


def parse(fname):
    def line2vec(line):
        return np.array([int(x) for x in line.split(",")])

    lines = open(fname).read().splitlines()
    vectors = [line2vec(line) for line in lines]
    return vectors


def part2(fname="input"):
    vectors = parse(fname)
    combos = list(combinations(range(len(vectors)), 2))

    def distance(pair):
        x0, x1 = pair
        y0 = vectors[x0]
        y1 = vectors[x1]
        return np.linalg.norm(y1 - y0)

    distances = sorted(
        [(combo, distance(combo)) for combo in combos], key=lambda x: x[1]
    )

    segments = [[x] for x in range(len(vectors))]
    count = 0
    while True:
        (x0, x1), _ = distances[0]
        distances = distances[1:]
        # find out if x0 or x1 is already in a segment
        seg0 = seg1 = None
        for seg in segments:
            if x0 in seg:
                seg0 = seg
            if x1 in seg:
                seg1 = seg
        if seg0 is not None and seg1 is not None:
            if seg0 != seg1:
                # merge segments
                seg0.extend(seg1)
                segments.remove(seg1)
        elif seg0 is not None:
            seg0.append(x1)
        elif seg1 is not None:
            seg1.append(x0)
        else:
            segments.append([x0, x1])

        count += 1
        if count == 1000:
            part1 = prod(
                len(x) for x in sorted(segments, key=lambda x: len(x), reverse=True)[:3]
            )
            print(f"part1: {part1}")

        if len(segments) == 1:
            part2 = vectors[x0][0] * vectors[x1][0]
            print(f"part2: {part2} after {count} iterations")
            return


part2()
