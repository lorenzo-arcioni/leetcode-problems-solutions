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
    
    len_nums1 = N = len(nums1)
    len_nums2 = K = len(nums2)

    L = len(nums1) + len(nums2) 
    
    # Questo se le due liste sono disgiunte
    if nums1[-1] < nums2[0]:

        if L % 2 == 0:
            if L//2 > len_nums1:
                return (nums2[(L//2) - len_nums1 - 1] + nums2[(L//2) - len_nums1]) / 2
            if L//2 > len_nums1 - 1:
                return (nums1[-1] + nums2[0]) / 2
            if L//2 < len_nums1:
                return (nums1[(L//2) - 1] + nums2[(L//2)]) / 2
            else: # Caso L//2 = len_nums1
                return (nums1[-1] + nums2[0]) / 2
            
        else:
            if L//2 > len_nums1:
                return nums2[(L//2) - len_nums1]
            if L//2 > len_nums1 - 1:
                return nums2[0]
            if L//2 < len_nums1:
                return nums1[L//2]
            else: # Caso L//2 = len_nums1
                return nums2[0]
        
    # Se le due liste si sovrappongono allora

    # Troviamo l'indice in nums1 che corrisponde alla posizione del primo valore della lista nums2
    key_index = bisect(nums1, nums2[0]) - 1 # Se non è presente il valore esatto teniamo l'indice del valore subito prima

    # Ora abbiamo che nums1[key_index:] è la porzione della lista che ha una sovrapposizione con nums2.

    # Se key_index > L - key_index, allora la mediana si trova nella prima parte della lista nums1.

    print("Il key_index è: ", key_index)

    if key_index + 1 > L - K - (N - key_index):

        half_index = L//2

        # Quindi possiamo trovare la mediana facendo...
        if L % 2 == 0:
            return (nums1[half_index - 1] + nums1[half_index]) / 2
        else:
            return nums1[half_index]
        
    # Se L - N - (N - key_index) > N + (N - key_index), allora la mediana si trova nella seconda parte della lista nums2.
    if L - N - (N - key_index) > N + (N - key_index):

        half_index = L//2

        # Quindi possiamo trovare la mediana facendo...
        if L % 2 == 0:
            return (nums2[half_index - 1] + nums2[half_index]) / 2
        else:
            return nums2[half_index]
        
    # Altrimenti vuol dire che la mediana si trova nella sovrapposizione delle due liste.
    # Sappiamo che la sovrapposizione delle due liste, in sequenza, ha lunghezza pari; in quanto la lunghezza delle due sovrapposizioni è la stessa per nums1 e nums2.
    # Quindi adesso possiamo trovare la mediana facendo...



            
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [4, 8, 10]
#print(findMedianSortedArrays(nums1, nums2))
print(st.median(sorted(nums1 + nums2)))
print(findMedianSortedArrays(nums1, nums2))