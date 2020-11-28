# https://leetcode.com/problems/two-sum/

class Solution:
    def two_sum(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]

if __name__ == '__main__':
    solution = Solution()
    print(solution.two_sum([2, 7, 11, 15], 9))
    print(solution.two_sum([3, 2, 4], 6))
    print(solution.two_sum([3, 3], 6))
