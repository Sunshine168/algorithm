#c solution
# void CalcAllPermutation(char* perm, int from, int to)
# {
#     if (to <= 1)
#     {
#         return;
#     }
#
#     if (from == to)
#     {
#         for (int i = 0; i <= to; i++)
#             cout << perm[i];
#         cout << endl;
#     }
#     else
#     {
#         for (int j = from; j <= to; j++)
#         {
#             swap(perm[j], perm[from]);
#             CalcAllPermutation(perm, from + 1, to);
#             swap(perm[j], perm[from]);
#         }
#     }
# }

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