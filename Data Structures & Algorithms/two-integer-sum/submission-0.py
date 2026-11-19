class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices_map = {value:i for i, value in enumerate(nums)}
        # print(indices_ma)

        for i, num in enumerate(nums):
            if target - num in indices_map and indices_map[target-num] != i:
                return [i, indices_map[target-num]]
        
