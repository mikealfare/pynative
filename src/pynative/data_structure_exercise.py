from typing import List, Dict, Set, Tuple
import math
from collections import Counter


def shuffle_lists(odd_list: list, even_list: list) -> list:
    """
    Exercise Question 1:
    Given two lists. Create a third list by picking the odd-index elements from the first list
    and the even index elements from the second.
    """
    return odd_list[1::2] + even_list[::2]


def move_element(input_list: list) -> list:
    """
    Exercise Question 2:
    Given an input list, remove the element at index 4 and:
        - add it to the 2nd position
        - add it at the end of the list
    """
    fourth_element = input_list.pop(4)
    input_list.insert(2, fourth_element)
    input_list.append(fourth_element)
    return input_list


def get_groups(input_list: list, size: int) -> list:
    for group in range(0, len(input_list), size):
        yield input_list[group:group + size]


def get_reversed_thirds(input_list: list) -> List[list]:
    """
    Exercise Question 3:
    Given a list, slice it into 3 equal length lists and reverse each list
    """
    list_length = math.ceil(len(input_list) / 3)
    return [group[::-1] for group in get_groups(input_list, list_length)]


def create_counter(input_list: list) -> Dict[int, int]:
    """
    Exercise Question 4:
    Given a list iterate it and count the occurrence of each element
    and create a dictionary to show the count of each element.
    """
    return Counter(input_list)


def get_zipped_pairs(list_1: list, list_2: list) -> Set[Tuple[int, int]]:
    """
    Exercise Question 5:
    Given two lists of equal size, create a set such that it shows the element from both lists
    in the pair
    """
    return set(zip(list_1, list_2))


def remove_elements(target: set, elements_to_remove: set) -> set:
    """
    Exercise Question 6:
    Given two sets, find the intersection and remove those elements from the first set
    """
    return target.difference(elements_to_remove)


def empty_the_subset(set_1: set, set_2: set):
    """
    Exercise Question 7:
    Given two sets, check if one set is a subset or superset of the other set.
    If a subset is found, delete all elements from that subset
    """
    if set_1.issubset(set_2):
        set_1.clear()
    elif set_2.issubset(set_1):
        set_2.clear()


def get_subset_of_keys_in_dict(my_list: list, my_dict: dict) -> list:
    """
    Exercise Question 8:
    Iterate a given list and check if a given element already exists in a dictionary
    as a key’s value. If not delete it from the list.
    """
    return [item for item in my_list if item in my_dict.values()]


def get_singletons_in_order(my_dict: dict) -> list:
    """
    Exercise Question 9:
    Given a dictionary, get all values from the dictionary and add them in a list
    but don’t add duplicates.
    """
    my_list = []
    for val in my_dict.values():
        if val not in my_list:
            my_list.append(val)
    return my_list


def get_min_max(my_list: list) -> Tuple[int, int]:
    """
    Exercise Question 10:
    Remove duplicates from a list and create a tuple. Then find the minimum and maximum numbers.
    """
    return min(my_list), max(my_list)
