class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        def binary_search(left, right):

            if left >= right:
                return -1

            mid = ((right-left)//2) + left
            # mid = n // 2
            print(left, mid, right)

            if target == nums[mid]:
                print("target", nums[mid])
                return mid
            elif target < nums[mid]:
                return binary_search(left, mid)
            elif target > nums[mid]:
                return binary_search(mid+1, right)

        return binary_search(0, n)
        

        