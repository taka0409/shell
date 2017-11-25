f=open("./weatherF.dat","r")
title=f.readline()[:-1].split("\t")
highest_day=[]
lowest_day=[]
highest_data=[]
lowest_data=[]

param=f.readline()[:-1].split("\t")
for i in range(1,len(param)):
  highest_day.append(param[0])
  highest_data.append(float(param[i]))
  lowest_day.append(param[0])
  lowest_data.append(float(param[i]))

for i in f.readlines():
  i=i[:-1].split("\t")
  for j in range(len(i)-1):
    if(float(i[j+1])>highest_data[j]):
      highest_data[j]=float(i[j+1])
      highest_day[j]=i[0]
    elif(float(i[j+1])<lowest_data[j]):
      lowest_data[j]=float(i[j+1])
      lowest_day[j]=i[0]

print("highest day\n",highest_day)
print("lowest day\n",lowest_day)
