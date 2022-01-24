class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = 0
        n2 = 0
        current = 0
        prev = 0
        total_length = len(nums1) + len(nums2)
        mid = total_length//2
        while mid >= 0 and n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                prev = current
                current = nums1[n1]
                n1 += 1
            else:
                prev = current
                current = nums2[n2]
                n2 += 1
            mid -= 1
        while mid >= 0 and n1 < len(nums1):
            prev = current
            current = nums1[n1]
            n1 += 1
            mid -= 1
        while mid >= 0 and n2 < len(nums2):
            prev = current
            current = nums2[n2]
            n2 += 1
            mid -= 1
        return current if total_length % 2 == 1 else (prev + current)/2