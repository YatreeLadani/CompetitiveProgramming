class Solution:
    def reverseString(self, a: List[str]) -> None:
        x = 0
        y = len(a)-1
        
        while(x<y):
            a[x],a[y] = a[y],a[x]
            x+=1
            y-=1