class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=collections.Counter(s1)
        c1=collections.Counter(s2[:len(s1)])
        k=len(s1)
        i=0
        if(sorted(s1)==sorted(s2[:len(s1)])):return True
        while(k<len(s2)):
            c1[s2[i]]-=1
            c1[s2[k]]+=1
            i+=1
            k+=1
            
            if(len(c-c1)==0 and len(c-c1)==0):
                return True
        return False