class Solution:
    def reverse(self, x: int) -> int:
        r = str(abs(x))
        r = r.strip()
        r = r[::-1]
        a = int(r)
        
        if a >= 2** 31 -1 or a <= -2** 31:
            return 0
        elif x<0:
            return -1*a
        else:
            return a