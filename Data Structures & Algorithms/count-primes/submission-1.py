class Solution:
    def countPrimes(self, n: int) -> int:

        arr = [False] * n
        result = []

        for num in range(2, n):
            if not arr[num]:
                result.append(num)
                for i in range(num*num, n, num):
                    arr[i] = True

        # print(result)
        return len(result)        