file = open('./4/input.txt', 'r')
input = file.readlines()


def compare_assignments(elf_a, elf_b):
    sections_a = list(map(int, elf_a.split('-')))
    sections_b = list(map(int, elf_b.split('-')))

    return sections_a[0] <= sections_b[1] and sections_b[0] <= sections_a[1]


def check_assignment_overlaps():
    pairs = 0
    for pair in input:
        assignments = pair.strip().split(',')
        has_included = compare_assignments(assignments[0], assignments[1])
        if has_included:
            pairs += 1

    return pairs


print(check_assignment_overlaps())
