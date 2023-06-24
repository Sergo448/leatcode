"""
TASK
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
from typing import List


def removeDuplicates_v01(nums: List[int]):
    """

    :param nums: List of integer nums with duplicates or no
        :type nums: List[int]
    :return: count of duplicates
        :rtype: int
    """
    if len(nums) <= 1:
        return nums

    duplicates_list: list = []

    elems: dict = {}
    for i, num in enumerate(nums):
        if num not in elems:
            elems[num] = 1
        else:
            duplicates_list.append('_')

    result = list(elems.keys()) + duplicates_list
    return result


def removeDuplicates_v02(nums: List[int]) -> int:
    """

    :param nums: List of integer nums with duplicates or no
        :type nums: List[int]
    :return: count of duplicates
        :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)

    duplicates_list: list = []
    counts: list = []
    for i in range(0, len(nums) - 1, 1):
        if nums[i] == nums[i + 1]:
            duplicates_list.append('_')
        else:
            counts.append(nums[i])
    counts.append(nums[-1])
    nums = counts + duplicates_list
    return len(counts)


def removeDuplicates_v03(nums: List[int]) -> int:
    # Length of the update array
    i, j = 0, 0
    while j < len(nums):
        if nums[j] == nums[i]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
    return i + 1


def removeDuplicates(nums: List[int]):
    """

    :param nums: List of integer nums with duplicates or no
        :type nums: List[int]
    :return: count of duplicates
        :rtype: int
    """

    duplicates_list: list = []

    elems: dict = {}
    for i, num in enumerate(nums):
        if num not in elems:
            elems[num] = 1
        else:
            duplicates_list.append(num)

    not_duplicated_list = list(elems.keys())
    n = len(not_duplicated_list)
    nums[0:n] = not_duplicated_list
    return n


nums = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]

for sequence in nums:
    print(removeDuplicates_v03(nums=sequence))
