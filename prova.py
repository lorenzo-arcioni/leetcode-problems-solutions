import statistics as st

def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
            
        if len(nums2) == len(nums1) == 1:
            return (nums1[0] + nums2[0]) / 2
        
        i = len(nums1)
        k = len(nums2)

        while True:
            print(nums1, nums2)
            i = len(nums1) // 2
            k = len(nums2) // 2

            if nums1[i] < nums2[k]:
                nums1 = nums1[i:]
                nums2 = nums2[:k+1]
            else:
                nums1 = nums1[:i+1]
                nums2 = nums2[k:]
            
            if len(nums2) == len(nums1) == 1:
                return (nums1[0] + nums2[0]) / 2
            
nums1 = [2, 3, 4]
nums2 = [3,4]
#print(findMedianSortedArrays(nums1, nums2))
print(st.median(sorted(nums1 + nums2)))