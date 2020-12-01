# https://leetcode.com/problems/palindrome-number/

class Solution:
    def palindrome_number(self, number):
        number = str(number)
        reverse_number = ''
        for i in range(len(number) - 1, -1, -1):
            reverse_number += number[i]
        return number == reverse_number

if __name__ == '__main__':
    solution = Solution()
    print(solution.palindrome_number(int(input('Enter a number : '))))
