"""
TASK

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints
2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:

    # Список в котором сохраняется результат
    result = []
    # Словарь в котором хранится разница и ее индекс
    index_map = {}
    # Перебираем все элементы по очереди функцией enumerate, которая возвращает i - индекс эл-та массива и значение
    for i, num in enumerate(nums):
        # Смотрим разницу между целевым значением и элементом из списка
        difference = target - num
        if difference in index_map:
            # Проверяем, есть ли в словаре ключ, по величине равной разнице
            # Если такой ключ есть, то возвращаем индекс такого элемента в массиве и индекс последнего числа
            result.append(i)
            result.append(index_map[difference])
            # Выходим из списка
            break
        else:
            # В словаре храним num как 'key', а i как 'value'
            index_map[num] = i
    return result


nums = [[1, 2, 3, 4, 10, 19, 22, 13, 33, 41, 4, 1],
        [-1, 22, 12, 22, 45, 30],
        [0, 0, 0, 11, 18],
        [],
        ]


for lst in nums:
    res = twoSum(nums=lst, target=29)
    print(res)

