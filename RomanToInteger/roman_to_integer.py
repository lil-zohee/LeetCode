# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def roman_to_integer(self, roman_num):
        number, i = 0, 0
        roman_num_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_nums = {'I': ('V', 'X'), 'X': ('L', 'C'), 'C': ('D', 'M')}
        while i < len(roman_num):
            if i < len(roman_num) - 1:
                if roman_num[i] in special_nums.keys() and roman_num[i + 1] in special_nums[roman_num[i]]:
                    number += roman_num_values[roman_num[i + 1]] - roman_num_values[roman_num[i]]
                    i += 2
                    continue
            number += roman_num_values[roman_num[i]]
            i += 1
        return number

if __name__ == '__main__':
    solution = Solution()
    print(solution.roman_to_integer('III'))
    print(solution.roman_to_integer('IV'))
    print(solution.roman_to_integer('IX'))
    print(solution.roman_to_integer('LVIII'))
    print(solution.roman_to_integer('MCMXCIV'))
