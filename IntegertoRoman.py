class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            raise ValueError("Input must be between 1 and 3999")

        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        result = ""
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while num >= value:
                num -= value
                result += numeral

        return result
    

Solutionclass = Solution()    
print(Solutionclass.intToRoman(200))  # Output: False
print(Solutionclass.intToRoman(65))  # Output: True
print(Solutionclass.intToRoman(32))  # Output: True    