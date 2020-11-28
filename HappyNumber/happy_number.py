# https://leetcode.com/problems/happy-number/

class Solution:
    def happy_number(self, number):
        original_number = number
        while number != 1:
            number = sum([int(char) ** 2 for char in str(number)])
            if number == original_number:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.happy_number(20))
