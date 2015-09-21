def  maxXor( l,  r):
    res = []
    for i in range(l,l+abs(l-r)):
        for j in range(0,abs(l-r)):
            res.append(i^(r-j))
                      
    return max(res)
                      
l = int(raw_input());


r = int(raw_input());

res = maxXor(l, r);
print(res)
