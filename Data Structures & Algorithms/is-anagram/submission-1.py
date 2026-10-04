class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp_s = ''.join(sorted(s))
        temp_t = ''.join(sorted(t))

        if len(s) != len(t):
            return False

        for l,n in zip(temp_s, temp_t):
            if l == n:
                continue
            else: 
                return False

        return True
            