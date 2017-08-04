#coding = utf-8
import sys
DNA = "ATCG"
for line in sys.stdin:
    c = line
    num = 0
    maxLength =0
    for i in range(0,len(c)):
        if DNA.find(c[i]) != -1:
        #找到了符合的,从这个位置开始向后匹配
         start = i
         for j in range(i,len(c)):
            if( DNA.find(c[j])!= -1):
                num+=1
                if num > maxLength:
                    maxLength = num
            else:
                break;
        num = 0
    print(maxLength)