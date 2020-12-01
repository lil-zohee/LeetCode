# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def is_isomorphic(self, string1, string2):
        isomorphic_counter = {'s1': {}, 's2': {}}
        count = 0
        for s1, s2 in zip(string1, string2):
            for letter, dict_key in ((s1, 's1'), (s2, 's2')):
                if letter in isomorphic_counter[dict_key]:
                    isomorphic_counter[dict_key][letter].append(count)
                else:
                    isomorphic_counter[dict_key][letter] = [count]
            count += 1
        if tuple(isomorphic_counter['s1'].values()) == tuple(isomorphic_counter['s2'].values()):
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.is_isomorphic(input('String 1 : '), input('String 2 : ')))
