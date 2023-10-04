import statistics as st
from bisect import bisect

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    # Funzione ausiliaria
    def get_median(lst: list[int]) -> float:

        L = len(lst)

        if L == 1:
            return lst[0]

        if len(lst) % 2 == 0:
            return (lst[L//2-1] + lst[L//2]) / 2
        else:
            return lst[L//2]
        
    # In caso di liste vuote
    if nums1 == []:
        return get_median(nums2)
    if nums2 == []:
        return get_median(nums1)

    # La lista nums1 viene prima di nums2
    if nums1[-1] > nums2[-1]:
        nums1, nums2 = nums2, nums1
    
    N = len(nums1)
    K = len(nums2)

    L = len(nums1) + len(nums2) 
    
    # Questo se le due liste sono disgiunte
    if nums1[-1] < nums2[0]:

        if L % 2 == 0:
            if L//2 > N:
                return (nums2[(L//2) - N - 1] + nums2[(L//2) - N]) / 2
            if L//2 == N:
                return (nums1[-1] + nums2[0]) / 2
            if L//2 < N:
                return (nums1[(L//2) - 1] + nums1[(L//2)]) / 2
            
        else:
            if L//2 > N:
                return nums2[(L//2) - N]
            if L//2 == N:
                return nums2[0]
            if L//2 < N:
                return nums1[L//2]
        
    # Se le due liste si sovrappongono allora
    # Per semplicità, la lista nums1 è più lunga

    if len(nums2) > len(nums1):
         nums1, nums2 = nums2, nums1
    
    N = len(nums1)
    K = len(nums2)

    # Numero di elementi <= di nums1[L//2]
    sx_index = bisect(nums2, nums1[N//2])

    # Numero di elementi > di nums1[L//2]
    dx_index = K - sx_index

    # Differenza
    difference = dx_index - sx_index

    if difference == 0:

        if L % 2 == 0:
            return (max(nums1[N//2-1], nums2[sx_index - 1]) + nums1[N//2]) / 2
        
        return nums1[N//2]

    dx = True if difference > 0 else False
    sx = True if difference < 0 else False

    i_1 = N//2
    i_2 = sx_index - 1

    median = nums1[i_1]
    pre    = nums2[i_2]
    k = 0
    print("Median n1:", median)
    print("Difference:", difference)
    print("Difference//2:", abs(difference) // 2)
    print("Bisect:", sx_index)

    try:
        print(nums1[i_1], nums2[i_2], median, pre)

        while k <= abs(difference) // 2:

            if sx:
                if nums1[i_1-1] <= nums2[i_2]:
                    pre = median
                    median = nums2[i_2]
                    i_2 -= 1
                elif nums1[i_1 - 1] > nums2[i_2]:
                    pre = median
                    i_1 -= 1
                    median = nums1[i_1]

                k += 1
            else:
                break
            print(nums1[i_1], nums2[i_2], median, pre)
    except:
        pass

    print("Mediana:", median)
    print("Pre:", pre)

    if L % 2 == 0:
        return (median + pre) / 2

    return pre
    
            
nums1 = [1, 2, 3, 3, 3,  4, 5, 8, 30, 30, 50, 51]
nums2 = [3, 9, 15, 25, 30, 30, 30, 37, 38, 39, 40, 46, 47, 48, 49, 50]

print(sorted(nums1 + nums2))
#print(findMedianSortedArrays(nums1, nums2))
print(st.median(sorted(nums1 + nums2)))
print(findMedianSortedArrays(nums1, nums2))