file = open('./5/input.txt', 'r')
data = file.readlines()


class Operation:
    def __init__(self, count, source, dest):
        self.count = count
        self.source = source
        self.dest = dest


def get_separator_row(data):
    row_index = 0

    while row_index < len(data):
        is_row_empty = not data[row_index].strip()
        if is_row_empty:
            break

        row_index += 1

    return row_index


def get_stacks(data):
    stacks = [[] for _ in range(len(data[0]) // 4)]

    for row in data:
        i = 0
        while i < len(row):
            if row[i] == '[':
                stacks[i // 4].insert(0, row[i + 1])

            i += 4

    return stacks


def get_operations(data):
    operations = []
    for row in data:
        r = row.strip().split()
        operations.append(Operation(int(r[1]), int(r[3]) - 1, int(r[5]) - 1))

    return operations


def operate(stacks, operations):
    for op in operations:
        new_source = stacks[op.source][:-op.count]
        moved_items = stacks[op.source][-op.count:]
        # this line is all that needed as the difference between part 1 and 2
        # moved_items.reverse()
        stacks[op.dest] = stacks[op.dest] + moved_items
        stacks[op.source] = new_source

    return stacks


def get_last_elements(stacks):
    answer = ''
    for stack in stacks:
        answer += stack[-1]

    return answer


def solve(data):
    separator_row = get_separator_row(data)
    stacks = get_stacks(data[:separator_row])
    operations = get_operations(data[separator_row + 1:])
    result = operate(stacks.copy(), operations)

    return get_last_elements(result)


print(solve(data))
