class Solution:
    def lastIndex(self, s: str) -> int:
        # code here
        n =len(s)
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                return i
        return -1;
