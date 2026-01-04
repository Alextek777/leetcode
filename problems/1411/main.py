import sys
sys.setrecursionlimit(1000000)  

class Solution:
    def numOfWays(self, n: int) -> int:
        self.module = (10 ** 9) + 7

        arr1 = [0] * (3 * n)
        arr1[0] = 1

        self.cache = {}

        return (self.availavleWays(arr1, 1) * 3) % self.module
    

    def availavleWays(self, arr: list, i: int):
        if i == len(arr):
            return 1
        
        key = self.getKey(arr, i)
        if key in self.cache:
            return self.cache[key] 
            
        availableColors = self.availableColors(arr, i)

        sum = 0
        for _, color in enumerate(availableColors):
            arr[i] = color
            ways = self.availavleWays(arr, i+1) 
            sum = (sum + ways) 

        self.cache[key] = sum

        return sum

        
    def availableColors(self, arr: list, i: int):
        availableColors = [1, 2, 3]

        if (i % 3) != 0:
            availableColors.remove(arr[i-1])
        if i > 2 and arr[i-3] in availableColors:
            availableColors.remove(arr[i-3])

        return availableColors
    
    def getKey(self, arr: list, i: int):
        l1 = 0
        l2 = 0
        l3 = 0
        if i > 0:
            l1 = arr[i-1]
        if i > 1:
            l2 = arr[i-2]
        if i > 2:
            l3 = arr[i-3]

        return "{}|{}|{}|{}".format(l1, l2, l3, i)
    

s = Solution()

result = s.numOfWays(5000)
print(result)