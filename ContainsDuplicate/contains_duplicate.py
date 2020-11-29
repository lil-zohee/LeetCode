# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def contains_duplicate(self, numbers):
        if len(numbers) != len(set(numbers)):
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.contains_duplicate([1, 2, 3, 1]))
    print(solution.contains_duplicate([1, 2, 3, 4]))
    print(solution.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
