klist = ["No", "Name","sem","grade"]
datalist = [(10,"pradip",2,8),(20,"kavy",3,9),(30,"varun",4,10),(40,"kavya",5,11)]
dblist=[]

for i in range(len(datalist)):
  d1={}
  for j in range(len(klist)):
    d1[klist[j]] = datalist[i][j]
  #print(d1)
  dblist.append(d1)
print(dblist)