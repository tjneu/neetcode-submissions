class Solution:
    def countPrimes(self, n: int) -> int:

        arr = [False] * n
        result = 0

        for num in range(2, n):
            if not arr[num]:
                result += 1
                for i in range(num*num, n, num):
                    arr[i] = True

        return result