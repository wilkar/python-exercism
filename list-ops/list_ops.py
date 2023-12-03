from typing import Callable


def append(list1: list, list2: list) -> list:
    for item in list2:
        list1.append(item)
    return list1


def concat(lists: list[list]) -> list:
    final_list: list = []

    for lst in lists:
        for item in lst:
            final_list.append(item)
    return final_list


def filter(function: Callable, list) -> list:
    return_list: list = []

    for item in list:
        if function(item) == True:
            return_list.append(item)

    return return_list


def length(list: list):
    return len(list)


def map(function: Callable, lst: list):
    return_list: list = []
    for item in lst:
        return_list.append(function(item))
    return return_list


def foldl(function: Callable, list: list, initial: int):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function: Callable, list: list, initial: int):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(lst: list):
    return_list: list = []
    for item in reversed(lst):
        return_list.append(item)
    return return_list
