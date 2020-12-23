class Solution:
    def is_valid(self, parentheses):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        if (len(parentheses) % 2 != 0 or
            parentheses[0] in pairs or
            parentheses[-1] in ('(', '[', '{')):
            return False
        for i in range(len(parentheses)):
            if parentheses[i] in ('(', '[', '{'):
                stack.append(parentheses[i])
            elif stack == [] or pairs[parentheses[i]] != stack[-1]:
                return False
            else:
                del stack[-1]
        return not stack

if __name__ == '__main__':
    solution = Solution()
    print(solution.is_valid(input('Enter a set of parentheses: ')))
