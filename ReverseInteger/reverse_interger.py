# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse_integer(self, number):
        reverse_num = ''
        number = str(number)
        if number[0] == '-':
            reverse_num = '-'
            number = number.replace('-', '')
        for i in range(len(number) - 1, -1, -1):
            reverse_num += number[i]
        reverse_num = int(reverse_num)
        if not -2147483648 <= reverse_num <= 2147483647:
            return 0
        return reverse_num

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse_integer(-120))
