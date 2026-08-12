class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(1, n)
        if x == 0 or n == 1:
            return x
        elif n == 0:
            return 1
        else:           
            return x**n

        
        