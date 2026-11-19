class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        curr = 0
        best = 0

        n = len(height)
        if n == 2:
            return min(height[0], height[1])

        i = 0
        j = n-1

        while i < n and j > 0 and i < j:
            
            curr = min(height[i], height[j]) * (j-i)
            best = max(best, curr)
            # print(i, j, curr, best)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return best