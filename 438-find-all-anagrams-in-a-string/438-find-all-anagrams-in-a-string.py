class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c=collections.Counter(p)
        c1=collections.Counter(s[:len(p)])
        k=len(p)
        i=0
        l=[]
        if(sorted(p)==sorted(s[:len(p)])):l.append(0)
        while(k<len(s)):
            c1[s[i]]-=1
            c1[s[k]]+=1
            i+=1
            k+=1
            
            if(len(c-c1)==0 and len(c-c1)==0):
                l.append(i)
        return l