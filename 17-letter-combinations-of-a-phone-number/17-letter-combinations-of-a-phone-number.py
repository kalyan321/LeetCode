from collections import defaultdict
def dfs(g,index,mainstring,substring,l1):
    if(index<len(mainstring)):
        for i in g[mainstring[index]]:
            dfs(g,index+1,mainstring,substring+i,l1)
    else:
        l1.append(substring)
class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        g=defaultdict(list)
        l=[list('abc'),list('def'),list('ghi'),list('jkl'),list('mno'),list('pqrs'),list('tuv'),list('wxyz')]
        for i in digits:
            g[i]+=l[int(i)-2]
        l1=[]
        dfs(g,0,digits,"",l1)
        return [] if len(digits)<1 else list(set(l1))
            