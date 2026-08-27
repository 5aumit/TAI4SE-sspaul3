"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""

class Solution:
    def areAlmostEqual(self, s1, s2):
        if not(len(s1) == len(s2)):
            return False

        differences = []
        for i in range(len(s1)):
            if not(s1[i] == s2[i]):
                differences.append(i)

        if len(differences) == 0:
            return True
        elif len(differences) == 2 and s1[differences[0]] == s2[differences[1]]:
            return True

        return False


if __name__ == "__main__":
    s = Solution()

    assert(s.areAlmostEqual("kelb", "kelb"))
    assert(s.areAlmostEqual("", ""))
    assert(not s.areAlmostEqual("abcd", "dcba"))
    assert(s.areAlmostEqual("abc", "cba"))
    assert(s.areAlmostEqual("abcdefghijklmnopqrstuvwxyz", "zbcdefghijklmnopqrstuvwxya"))
    assert(not s.areAlmostEqual("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxya"))
