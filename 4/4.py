file = open('./4/input.txt', 'r')
input = file.readlines()


def compare_assignments(elf_a, elf_b):
    sections_a = list(map(int, elf_a.split('-')))
    sections_b = list(map(int, elf_b.split('-')))

    # a containment is when when both the 0 and 1 are contained by the other 0 and 1
    # so when a0 > b0 and a1 < b1

    a_is_included = sections_a[0] >= sections_b[0] and sections_a[1] <= sections_b[1]
    b_is_included = sections_b[0] >= sections_a[0] and sections_b[1] <= sections_a[1]
    return a_is_included or b_is_included


def check_assignment_overlaps():
    pairs = 0
    for pair in input:
        assignments = pair.strip().split(',')
        has_included = compare_assignments(assignments[0], assignments[1])
        if has_included:
            pairs += 1

    return pairs


print(check_assignment_overlaps())
