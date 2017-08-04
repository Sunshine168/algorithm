def CalcAllPermutation(perm,begin,to):
    perm = list(perm)
    if to<= 1:
        return ;
    if to == begin:
        print("".join(perm))
    else:
        for j in range(begin,to):
            perm[j],perm[begin] = perm[begin],perm[j]
            CalcAllPermutation(perm,begin+1,to)
            perm[j], perm[begin] = perm[begin], perm[j]

a =  "abc"
CalcAllPermutation(a,0,len(a))