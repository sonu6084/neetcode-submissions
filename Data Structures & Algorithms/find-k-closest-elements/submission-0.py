class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closet_window = arr[:k]
        current_window = arr[:k]

        for r in range(k,len(arr)):
            if abs(current_window[0]-x) > abs(arr[r]-x):
                current_window.pop(0)
                current_window.append(arr[r])
            
            if abs(current_window[0]-x) == abs(arr[r]-x) and current_window[0] > x:
                current_window.pop(0)
                current_window.append(arr[r])

        return current_window
