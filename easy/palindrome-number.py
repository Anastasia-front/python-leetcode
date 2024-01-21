class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :returnType: bool
        """
        str_x = str(x)
        rev_x = str_x[::-1]

        length = len(str_x)

        if length==1:
            return True

        iteration = (length // 2)+1


        for i in range(iteration):
            if str_x[i] == rev_x[i]:
                if iteration-1 == i:
                    return True
                continue
            else:
                return  False


solution = Solution()
result = solution.isPalindrome(1011301)
print(result)
