f=open("./weatherF.dat","r")
title=f.readline()[:-1].split("\t")
temp_list=[]
prec_list=[]
leng_list=[]
j=f.readline()[:-1].split("\t")
for i in range(1,11):
  sum_temp=0
  sum_prec=0
  sum_leng=0
  count=0
  while('2017/'+str(i) in j[0]):
    sum_temp+=float(j[1])
    sum_prec+=float(j[4])
    sum_leng+=float(j[5])
    count+=1
    j=f.readline()[:-1].split("\t")
  temp_list.append(round(sum_temp/count,2))
  prec_list.append(round(sum_prec/count,2))
  leng_list.append(round(sum_leng/count,2))

print("temp\n",temp_list)
print("precipitation\n",prec_list)
print("length\n",leng_list)