
s1=set(map(lambda x:(x[0],x[1]),net.A['Leuven_1_0050682'].edges))
s2=set(map(lambda x:(x[0],x[1]),net.A['Leuven_1_0050683'].edges))
jaccard=len(s1.intersection(s2))/len(s1.union(s2))
