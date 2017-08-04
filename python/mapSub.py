#coding = utf-8
import sys
for line in sys.stdin:
    c = line
    store = {}
    for x in line:
     if isinstance(x,str) :
        if(not x in store):
            store[x] = 0
        store[x]+=1
        s = [(k, store[k]) for k in sorted(store, key=store.get, reverse=True)]
    print(store)

