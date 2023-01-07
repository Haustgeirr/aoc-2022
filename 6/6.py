file = open('./6/input.txt', 'r')
data = file.readlines()


def find_array_in_array(array):
    for element in array:
        if array.count(element) > 1:
            return True

    return False


def solve(data, marker_length):
    i = 0
    data_stream = data[0]
    while i < len(data_stream) - marker_length:
        marker = data_stream[i:i + marker_length]
        duplicate = find_array_in_array(marker)
        if not duplicate:
            return i + marker_length

        i += 1


print(solve(data, 14))
