# Two Pointers
from typing import List, Union


class TwoPointers:

    @staticmethod
    def TwoSum(sequence: List[Union[int, float]], target: Union[int, float]) -> Union[list[int], int]:
        """

        :param sequence: sequence of int or float elements
        :type sequence: List[Union[int, float]]
        :param target: target value
        :type target: Union[int, float]
        :return list: list of 2 elements, which summ == target
        :rtype list: Union[list[int], int]
        """
        sequence.sort()
        # represents first pointer
        left = 0
        # represents second pointer
        right = len(sequence) - 1

        while left < right:

            # If we find a pair
            if sequence[left] + sequence[right] == target:
                return [left, right]

            elif sequence[left] + sequence[right] < target:
                left += 1
            else:
                right -= 1

        return 0

    @staticmethod
    def TwoSubstraction(sequence: List[Union[int, float]], target: Union[int, float]) -> Union[list[int], int]:
        """
        :param sequence: sequence of int or float elements
        :type sequence: List[Union[int, float]]
        :param target: target value
        :type target: Union[int, float]
        :return list: list of 2 elements, which summ == target
        :rtype list: Union[list[int], int]
        """

        sequence.sort()
        # represents first pointer
        left = 0
        # represents second pointer
        right = 1

        while right <= len(sequence):

            # If we find a pair
            if sequence[right] - sequence[left] == target:
                return [left, right]

            elif sequence[right] - sequence[left] < target:
                right += 1
            else:
                left += 1

        return 0


arr = [3, 5, 9, 2, 8, 10, 11, 13, 15, 11]
# [3, 5, 9, 2, 8, 10, 11] -> [2, 3, 5, 8, 9, 10, 11]
print(TwoPointers().TwoSum(sequence=arr, target=11))
print(TwoPointers().TwoSubstraction(sequence=arr, target=2))
