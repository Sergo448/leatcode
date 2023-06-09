"""
TASK

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List


def containsDuplicate_v1(nums: List[int]) -> bool:
    # Создаем список в котром будут храниться все наши элементы по очереди
    # Кладем туда первый элемент списка
    uniques: dict = {nums[0]: 0}

    # Перебираем список начиная с 1-го индекса
    for i in range(1, len(nums)):
        # Если такой элемент существует, то возвращаем True
        if nums[i] in uniques:
            return True
        # Если нет, то добавляем в словарь этот элемент
        uniques[nums[i]] = i
    return False


def containsDuplicate_v2(nums: List[int]) -> bool:
    # Берем сортировку питона, которая сортирует, исключая повторы
    len_nuns: int = len(set(nums))
    # Если размеры массивов разные, то возвращаем True, иначе False
    if len_nuns == len(nums):
        return False
    return True


# Медленный
def containsDuplicate_v3(nums: List[int]) -> bool:
    # Пробегаемся по списку и смотрим есть ли там элемент
    elems: list = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] in elems:
            return True
        elems.append(nums[i])
    return False


nums = [
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 4]
]

for listofnums in nums:
    result = containsDuplicate_v3(nums=listofnums)
    print(result)
