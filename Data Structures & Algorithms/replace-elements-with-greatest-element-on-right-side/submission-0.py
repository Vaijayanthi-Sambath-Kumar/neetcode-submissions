class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range (len(arr)):
            high_right = float('-inf')
            for j in range(i+1, len(arr)):
                if arr[j] > high_right:
                    high_right = arr[j]
            arr[i] = high_right
        arr[-1] = -1
        return arr
        