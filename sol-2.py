import statistics as st
from bisect import bisect

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    
    L = len(nums1) + len(nums2)

    f = L % 2 == 0

    i = k = r = 0

    if nums1 == []:
            
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2 - 1] + nums2[len(nums2) // 2]) / 2
            return nums2[len(nums2) // 2]

    if nums2 == []:
        
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
        return nums1[len(nums1) // 2]


    while i < len(nums1) and k < len(nums2):

        if nums1[i] <= nums2[k]:
            if r == L // 2 - 1:

                if f:
                    if i+1 == len(nums1):
                        return (nums1[i] + nums2[k]) / 2
                    return (nums1[i] + min(nums1[i+1], nums2[k])) / 2
                else:
                    if i+1 == len(nums1):
                        return nums2[k]
                    return min(nums1[i+1], nums2[k])            
            i += 1
            
        elif nums1[i] > nums2[k]:
                
            if r == L // 2 - 1:
                if f:
                    if k +1 == len(nums2):
                        return (nums2[k] + nums1[i]) / 2
                    return (nums2[k] + min(nums1[i], nums2[k+1])) / 2
                else:
                    if k+1 == len(nums2):
                        return nums1[i]
                    return min(nums1[i], nums2[k+1])
            
            k += 1

        r += 1

        if i >= len(nums1):
            while k < len(nums2):
                if r == L // 2 - 1:
                    if f:
                        return (nums2[k] + nums2[k+1]) / 2
                    else:
                        return nums2[k+1]
                r += 1
                k += 1

        if k >= len(nums2):
            while i < len(nums1):
                if r == L // 2 - 1:
                    if f:
                        return (nums1[i] + nums1[i+1]) / 2
                    else:
                        return nums1[i+1]
                r += 1
                i += 1

            


nums1 = [1,2]
nums2 = [3,4]
#print(findMedianSortedArrays(nums1, nums2))
print(st.median(sorted(nums1 + nums2)))
print(findMedianSortedArrays(nums1, nums2))