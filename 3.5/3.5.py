file = open('./3.5/input.txt', 'r')
input = file.readlines()


def get_letter_value(letter):
    letter_value = ord(letter)
    if letter_value < 97:
        return letter_value - 38

    return letter_value - 96


def find_in_two_arrays(item, array_a, array_b):
    return item in array_a and item in array_b


def get_matching_letter():
    found_items = []
    for i in range(0, len(input), 3):
        for letter in input[i]:
            if find_in_two_arrays(letter, input[i+1], input[i+2]):
                found_items.append(get_letter_value(letter))
                break

    return found_items


print(sum(get_matching_letter()))
