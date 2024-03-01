def lengthofLongestsubstring(s):
    l=0
    k=set()
    res=0
    for r in range(len(s)):
        while s[r] in k:
            k.remove(s[l])
            l+=1
        k.add(s[r])
        res=max(res,len(k))
    return res
        
    
