from collections import Counter
from itertools import product
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # output_arr = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in nums:
        #         if nums[i]>j:
        #             count+=1
        #     output_arr.append(count)
        # return output_arr
        output_arr = [sum(1 for j in nums if nums[i] > j) for i in range(len(nums))]
        return output_arr
    
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i
            else: return 0
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        const_dict = {
            "1":[],
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z'],
            "0":[],
        }
        arr_item = []
        output_arr = []
        if digits:
            for val in digits:
                if val in const_dict.keys():
                    arr_item.append(const_dict[val])
            for item in product(*arr_item):
                comb = ''
                for j in item:
                    comb += j
                output_arr.append(comb)
            return output_arr
        return []
    
    def numTilePossibilities(self, tiles):
        def dfs(cnt: Counter):
            ans = 0
            for i, x in cnt.items():
                if x > 0:
                    ans += 1
                    cnt[i] -= 1
                    ans += dfs(cnt)
                    cnt[i] += 1
            return ans

        cnt = Counter(tiles)
        return dfs(cnt)

obj = Solution()
# data = obj.smallerNumbersThanCurrent([8,1,2,2,3])
# snumber = obj.singleNumber([4,1,2,1,2])
# comb = obj.letterCombinations("")
tiles = obj.numTilePossibilities("AAB")
print(tiles)