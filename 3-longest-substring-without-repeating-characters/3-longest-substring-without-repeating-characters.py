from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        ans=0
        l={}
        l=defaultdict(int)
        
        for i in range(len(s)):
            
            if(ord(s[i])==0):
                l[ord(s[i])]+=1
            else:
                k=start
                while(k<i):
                    if(s[i]==s[k]):
                        start=k+1
                        break
                    else:
                        l[ord(s[i])]=0
                        k+=1
            ans=max(ans,i-start+1)
        return ans