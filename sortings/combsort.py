# -*- coding: utf-8 -*-
# Comb Sorting

"""
Самая удачная модификация пузырька. Алгоритм по скорости соперничает с быстрой сортировкой.

Во всех предыдущих вариациях мы сравнивали соседей.
А тут сначала рассматриваются пары элементов, находящиеся друг от друга на максимальном расстоянии.
При каждой новой итерации это расстояние равномерно сужается.
"""

from typing import List, Union


class CombSorting:

    def __init__(self, sequence):
        """Constructor"""
        self.sequence = sequence

    @staticmethod
    def MyCombSorting(sequence: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """
        gap: int = len(sequence)
        # Флаг для захода в цикл сортировки
        nead_to_swap: bool = True
        while gap > 1 or nead_to_swap:
            gap = max(1, int(gap / 1.25))
            nead_to_swap = False
            for i in range(len(sequence) - gap):

                j = i + gap
                item1 = sequence[i]
                item2 = sequence[j]
                if sequence[i] > sequence[j]:
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                    nead_to_swap = True
        return sequence


lst = [[4, 1, 5, 90, 77, 3, 12, 0, 33, 31, 34, 35, 30], [5, 3, 8, 6, 7, 2], [5.1, 3.3, 3.4, 4.4, 4.35]]

for i in range(len(lst)):
    result = CombSorting(sequence=lst).MyCombSorting(sequence=lst[i])
    print(result)
