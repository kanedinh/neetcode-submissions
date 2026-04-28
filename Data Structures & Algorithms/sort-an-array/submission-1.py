class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            l_arr = arr[l:m+1]
            r_arr = arr[m+1:r+1]
            i, j = 0, 0
            k = l

            while i < len(l_arr) and j < len(r_arr):
                if l_arr[i] <= r_arr[j]:
                    arr[k] = l_arr[i]
                    i += 1
                else:
                    arr[k] = r_arr[j]
                    j += 1
                k += 1
            
            while i < len(l_arr):
                arr[k] = l_arr[i]
                i += 1
                k += 1
            while j < len(r_arr):
                arr[k] = r_arr[j]
                j += 1
                k += 1

        def mergeSort(arr, l, r):
            if l < r:
                m = (l+r) // 2
                mergeSort(arr, l, m)
                mergeSort(arr, m + 1, r)
                merge(arr, l, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)