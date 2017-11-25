OK=0
DOWN=0
rack_dict={}
for i in range(1,101):
  f=open("./racklogs/rack"+str(i)+".log","r")
  title=f.readline()
  sum_hour=0
  count=0
  for j in f.readlines():
    j=j[:-1].split("\t")
    if(j[1]=="OK"):
      OK+=1
    else:
      DOWN+=1
    sum_hour+=int(j[2])
    count+=1

  rack_dict["rack"+str(i)]=sum_hour/count
  sorted_list=sorted(rack_dict.items(),key=lambda x: x[1])
for i in range(1,4):
  print(sorted_list[-i][0])
print("percentage\n",round(OK/(OK+DOWN),3))