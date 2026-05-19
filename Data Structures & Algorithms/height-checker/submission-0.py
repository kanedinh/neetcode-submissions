class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
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
                m = (l+r)//2
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)
                merge(arr, l, m, r)
            return arr

        # expected = mergeSort(heights, 0, len(heights) - 1)
        expected = sorted(heights)
        print(expected)
        res = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res