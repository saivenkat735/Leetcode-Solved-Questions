def totalFruit(fruits):
    k={}
    l=0
    res=0
    for r in range(len(fruits)):
        r_fruits=fruits[r]
        if r_fruits not in k:
            k[r_fruits]=1
        else:
            k[r_fruits]+=1
        while len(k)>2:
            l_fruits=fruits[l]
            k[l_fruits]-=1
            if k[l_fruits]==0:
                del k[l_fruits]
            l+=1
        res=max(res,r-l+1)
    return res
            
                   
