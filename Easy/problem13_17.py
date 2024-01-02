class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in digits:
            num += str(i)
        return [int(x) for x in str(int(num)+1)]
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_number = max(len(a), len(b))
        na = a.zfill(max_number)
        nb = b.zfill(max_number)
        carry = 0
        binary_sum = ''
        for i in range(max_number-1, -1, -1):
            n_sum = int(na[i]) + int(nb[i]) + carry
            binary_sum=str(n_sum%2)+binary_sum
            carry = n_sum // 2
        if carry != 0:
            binary_sum = str(carry)+binary_sum
        return binary_sum
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        ways = [0] * (n + 1)
        ways[0]= 1
        ways[1] = 1
        print(ways, "before loop")
        for i in range(2, n+1):
            ways[i] =ways[i-1]+ways[i-2]
        return ways[n]            
obj = Solution()
op = obj.climbStairs(20)
print(op, "---")