# -*- coding: utf-8 -*-
# Odd event sorting

"""
Снова итерации по попарному сравнению соседних элементов при движении слева-направо.
Только сначала сравниваем пары у которых первый элемент — нечётный по счёту,
а второй — чётный (т.е. первый и второй, третий и четвёртый, пятый и шестой и т.д.).
А потом наоборот — чётный + нечётный (второй и третий, четвёртый и пятый, шестой и седьмой и т.д.).
В этом случае многие крупные элементы массива на одной итерации одновременно делают один шаг вперёд
(в пузырьке самый крупный за итерацию доходит до конца,
но остальные немаленькие практически все остаются на месте).

Кстати, это изначально была параллельная сортировка со сложностью O(n)...
"""
from typing import List, Union


class OddEventSorting:

    def __init__(self, sequence):
        """Constructor"""
        self.sequence = sequence

    @staticmethod
    def MyOddEventSorting(sequence: List[Union[int, float]]) -> Union[List[Union[int, float]], int]:
        """
        :param sequence: sequence with int numbers
        :type sequence: List[Union[int, float]
        :return sequence: sequence with sorted int numbers
        :rtype sequence: List[Union[int, float]
        """

        if len(sequence) == 0:
            return 1
        # range
        rng = len(sequence)
        # Если мы не видим элементы, которые надо сортировать
        # После прохода туда по четным и нечетным стартовым позициям, то цикл завершается
        flag: bool = True
        while flag:
            # Пред установка флага для последующего выхода из цикла
            flag = False
            # Начиная с нечетного элемента. С шагом 2 (на 3-ей позиции в range)
            for i in range(0, rng - 1, 2):
                # Если условие выполняется в четном или нечетном случае, то будет +1 итерация цикла
                if sequence[i] > sequence[i + 1]:
                    sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                    flag = True
            # Начиная с четного элемента. С шагом 2 (на 3-ей позиции в range)
            for i in range(1, rng - 1, 2):
                # Если условие выполняется в четном или нечетном случае, то будет +1 итерация цикла
                if sequence[i] > sequence[i + 1]:
                    sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                    flag = True
        return sequence


lst = [[4, 1, 5, 90, 77, 3, 12, 0, 33, 31, 34, 35, 30], [5, 3, 8, 6, 7, 2], [5.1, 3.3, 3.4, 4.4, 4.35]]

for i in range(len(lst)):
    result = OddEventSorting(sequence=lst).MyOddEventSorting(sequence=lst[i])
    print(result)
