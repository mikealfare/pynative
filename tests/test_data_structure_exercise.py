from typing import List, Dict, Set, Tuple

import pytest

from .conftest import data_structure_exercise


@pytest.mark.parametrize('odd_list,even_list,expected', [
    ([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28], [6, 12, 18, 4, 12, 20, 28]),
    ([3, 6, 9, 12, 15, 18], [4, 8, 12, 16, 20, 24, 28], [6, 12, 18, 4, 12, 20, 28])
])
def test_shuffle_lists(odd_list: list, even_list: list, expected: list):
    assert data_structure_exercise.shuffle_lists(odd_list, even_list) == expected


@pytest.mark.parametrize('input_list,expected', [
    ([34, 54, 67, 89, 11, 43, 94], [34, 54, 11, 67, 89, 43, 94, 11])
])
def test_move_element(input_list: list, expected: list):
    assert data_structure_exercise.move_element(input_list) == expected


@pytest.mark.parametrize('input_list,size,expected', [
    ([11, 45, 8, 23, 14, 12, 78, 45, 89], 3, [[11, 45, 8], [23, 14, 12], [78, 45, 89]])
])
def test_get_groups(input_list: list, size: int, expected: List[list]):
    assert [result for result in data_structure_exercise.get_groups(input_list, size)] == expected


@pytest.mark.parametrize('input_list,expected', [
    ([11, 45, 8, 23, 14, 12, 78, 45, 89], [[8, 45, 11], [12, 14, 23], [89, 45, 78]])
])
def test_get_reversed_thirds(input_list: list, expected: List[list]):
    assert data_structure_exercise.get_reversed_thirds(input_list) == expected


@pytest.mark.parametrize('input_list,expected', [
    ([11, 45, 8, 11, 23, 45, 23, 45, 89], {11: 2, 45: 3, 8: 1, 23: 2, 89: 1})
])
def test_create_counter(input_list: list, expected: Dict[int, int]):
    assert data_structure_exercise.create_counter(input_list) == expected
    assert isinstance(expected, dict)


@pytest.mark.parametrize('list_1,list_2,expected', [
    (
            [2, 3, 4, 5, 6, 7, 8],
            [4, 9, 16, 25, 36, 49, 64],
            {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)})
])
def test_get_zipped_pairs(list_1: list, list_2: list, expected: Set[Tuple[int, int]]):
    assert data_structure_exercise.get_zipped_pairs(list_1, list_2) == expected


@pytest.mark.parametrize('target,elements_to_remove,expected', [
    ({65, 42, 78, 83, 23, 57, 29}, {67, 73, 43, 48, 83, 57, 29}, {65, 42, 78, 23})
])
def test_remove_elements(target: set, elements_to_remove: set, expected: set):
    assert data_structure_exercise.remove_elements(target, elements_to_remove) == expected


@pytest.mark.parametrize('set_1,set_2,expected_set_1,expected_set_2', [
    ({57, 83, 29}, {67, 73, 43, 48, 83, 57, 29}, set(), {67, 73, 43, 48, 83, 57, 29})
])
def test_empty_the_subset(set_1: set, set_2: set, expected_set_1: set, expected_set_2: set):
    data_structure_exercise.empty_the_subset(set_1, set_2)
    assert set_1 == expected_set_1
    assert set_2 == expected_set_2


@pytest.mark.parametrize('my_list,my_dict,expected', [
    (
            [47, 64, 69, 37, 76, 83, 95, 97],
            {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97},
            [47, 69, 76, 97]
    )
])
def test_get_subset_of_keys_in_dict(my_list: list, my_dict: dict, expected: list):
    assert data_structure_exercise.get_subset_of_keys_in_dict(my_list, my_dict) == expected


@pytest.mark.parametrize('my_dict,expected', [
    ({
        'jan': 47,
        'feb': 52,
        'march': 47,
        'April': 44,
        'May': 52,
        'June': 53,
        'july': 54,
        'Aug': 44,
        'Sept': 54
    },
     [47, 52, 44, 53, 54]
    )
])
def test_get_singletons_in_order(my_dict: dict, expected: list):
    assert data_structure_exercise.get_singletons_in_order(my_dict) == expected


@pytest.mark.parametrize('my_list,expected', [
    ([87, 45, 41, 65, 94, 41, 99, 94], (41, 99))
])
def test_get_min_max(my_list: list, expected: Tuple[int, int]):
    assert data_structure_exercise.get_min_max(my_list) == expected
