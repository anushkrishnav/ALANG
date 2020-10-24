comm1 = [20, 22, 25, 30, 36]
comm2 = [25, 30, 33, 44, 55]
weights =  2
Lr1 = [100, 110, 113.64, 120, 120]
Lr2 = [100, 120, 110, 133.33, 125]
leng=len(comm1)
wlr1 = []
wlr2 = []
swlr = []
i=1
while i < leng-1:
    wlr1.append(Lr1[i]*3)
    wlr2.append(Lr2[i]*3)
print(wlr2)
a = [100,115,11.82]