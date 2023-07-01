"""
TASK

You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n..
"""

from typing import List


def MergeSortedArray(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    :param nums1: first imput array, sorted in non-decreasing order
        :type nums1: List[int]
    :param nums2: second input aray, sorted in non-decreasing order
        :type nums2: List[int]
    :param m: count of nums from array 1 to merge 
        :type m: int
    :param n: count of nums from array 2 to merge 
        :type n: int

    :return None:
    """
    i = m - 1
    j = n - 1
    index = m + n - 1
    # Если массив 1 не пуст и массив 2 не пуст
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:         # Если элемент nums1[i] < nums2[j],
            nums1[index] = nums2[j]     # то nums1[index=m+n-1] устанавливаем = nums2[j] 
            j -= 1                      # уменьшаем на 1 второй указатель
        else:
            nums1[index] = nums1[i]     # Иначе в первый массив на место = индексуустанавливаем значение массива 1 = указателю 1
            i -= 1                      # Уменьшаем на 1 первый указатель
        index -= 1                      # Уменьшаем на 1 индекс при любом раскладе, чтобы идти на уменьшение с шагом -1
    # Для случаев, когда m = 0
    while j >= 0:
        nums1[index] = nums2[j]
        j -= 1
        index -= 1

    


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

MergeSortedArray(nums1=nums1, m=m, nums2=nums2, n=n)
print(nums1)
