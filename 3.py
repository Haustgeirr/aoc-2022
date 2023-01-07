file = open('./3/3.txt', 'r')
input = file.readlines()


def get_letter_value(letter):
    letter_value = ord(letter)
    if letter_value < 97:
        return letter_value - 38

    return letter_value - 96


def get_matching_letter():
    found_items = []
    for rucksack in input:
        item_count = len(rucksack)

        for i in range((item_count // 2)):
            if rucksack[i] in rucksack[item_count // 2:]:
                found_items.append(get_letter_value(rucksack[i]))
                break

    return found_items


print(sum(get_matching_letter()))
