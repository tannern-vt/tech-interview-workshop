class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        ans_list_1 = set1 - set2
        ans_list_2 = set2 - set1

        return [ans_list_1, ans_list_2]
