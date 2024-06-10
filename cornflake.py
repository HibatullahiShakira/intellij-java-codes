def list_of_ten_numbers(number: list) -> list:
    list_of_ten = []
    for num in number:
        if 1 < num < 50:
            list_of_ten.append(num)
    return list_of_ten[:10]


def create_length(collection):
    counter = 0
    for count in collection:
        counter += 1
    return counter


def sum_of_element_at_even_indexes(element: list):
    total = 0
    for indexes in range(0, create_length(element), 2):
        total += element[indexes]
    return total


def sum_of_element_at_odd_indexes(element: list):
    total = 0
    for indexes in range(1, create_length(element), 2):
        total += element[indexes]
    return total


def multiply_number_in_thid_element_bY_three(element):
    for indexes in range(2, create_length(element), 3):
        element[indexes] *= 3
    return element


def element_average(element: list):
    total = 0
    for indexes in range(0, create_length(element)):
        total += element[indexes]
    return total


def largest_number(collection: list):
    maximum = collection[0]
    for number in collection:
        if number > maximum:
            maximum = number
    return maximum


def smallest_number(collection: list):
    minimum = collection[0]
    for number in collection:
        if number < minimum:
            minimum = number
    return minimum


def strings(collection):
    strings_count = 0
    character_count = 0
    for string in collection:
        strings_count += 1
        for character in string:
            character_count += 1
            if character_count > 2 and string[0] == string[-1]:
                return string
    #return strings_count


def sequential_list_of_integer(integer: list):
    sequential_list = []
    for number in range(1, 16):
        sequential_list.append(number)
    return sequential_list

def

print(sequential_list_of_integer([1, 2, 3, 4, 5, 6]))
