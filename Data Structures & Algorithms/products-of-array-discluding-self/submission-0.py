class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n

        pre = 1
        for i in range(n):
            result[i] = pre
            pre = pre * nums[i]

        # print(result)

        post = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * post
            post = post * nums[i]

        # print(result)

        return result
    