import textwrap


def parse(s):
    x0, x1 = s.split("-")
    return int(x0), int(x1)


def does_it_repeat(index):
    s = str(index)
    l = len(s)
    if l % 2 == 1:
        return False

    else:
        return s[: l // 2] == s[l // 2 :]


def all_substrs_repeat(s, substr_len):
    substrs = textwrap.wrap(s, substr_len)
    return len(set(substrs)) == 1


def has_any_repeating_substring(index):
    s = str(index)
    l = len(s)
    max_substr_size = l // 2
    return any(all_substrs_repeat(s, k) for k in range(1, max_substr_size + 1))


def total_valids_in_range(x0, x1):
    return sum(ii for ii in range(x0, x1 + 1) if does_it_repeat(ii))


def total_valids_in_range2(x0, x1):
    return sum(ii for ii in range(x0, x1 + 1) if has_any_repeating_substring(ii))


vals = [parse(x) for x in open("input").read().split(",")]


def part1():
    return sum(total_valids_in_range(x0, x1) for x0, x1 in vals)

print(part1())
print(part2())



def part2():
    return sum(total_valids_in_range2(x0, x1) for x0, x1 in vals)
