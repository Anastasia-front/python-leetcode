class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :returnType: int
        """
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict_exc = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,"CM":900}
        sum = 0
        double_num=''
        exceptions = ['IV','IX','XL','XC','CD',"CM"]
        coincidences=[]

        for exc in exceptions:
            # print(s.find(exc))
            coincidences+=[s.find(exc)]

        filter_coin=list(filter(lambda x:x>=0, coincidences))
        sorted_indices=filter_coin[::-1]
        plus_one_sorted_indices=list(map(lambda x:x+1,sorted_indices))

        # print(sorted_indices,plus_one_sorted_indices)

        for i, char in enumerate(s):
            if len(filter_coin)>0:
                
                if i in sorted_indices:
                    double_num=char
                    # print(f'first - {double_num}')

                elif i in plus_one_sorted_indices:
                    double_num+=char
                    # print(f'second - {double_num}')
                    sum+=dict_exc[double_num]
                else:
                    sum+=dict[char]
                    double_num=''
            else:
                sum+=dict[char]
        return sum

# Runtime 38 ms / Memory 11.6 mb
print("MySolution - Runtime 38 ms / Memory 11.6 mb")
solution = Solution()
result = solution.romanToInt("IV")
print(result)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :returnType: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0  # Keep track of the previous value to handle subtraction cases
        
        for char in reversed(s):
            current_value = roman_values[char]
            
            if current_value < prev_value:
                # If the current value is smaller than the previous, subtract it
                result -= current_value
            else:
                # Otherwise, add it to the result
                result += current_value
            
            # Update the previous value
            prev_value = current_value
        
        return result

# Runtime 22 ms / Memory 11.73 mb
print("SimpleSolution - Runtime 22 ms / Memory 11.73 mb")
solution = Solution()

# Test cases
print(solution.romanToInt("III"))       # Output: 3
print(solution.romanToInt("LVIII"))     # Output: 58
print(solution.romanToInt("MCMXCIV"))   # Output: 1994