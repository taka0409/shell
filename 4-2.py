rack_dict={"MAINTENANCE":0,"DISK_FAILURE":0,
"POWER_FAIRULE":0,"CPU_ERROR":0,
"MEMORY_ERROR":0,"UNKNOWN_ERROR":0}
count=0
for i in range(1,101):
  f=open("./racklogs/rack"+str(i)+".log","r")
  title=f.readline()
  for j in f.readlines():
    j=j[:-1].split("\t")
    if(j[3]=="MAINTENANCE"):
      rack_dict["MAINTENANCE"]+=1
    elif(j[3]=="DISK FAILURE"):
      rack_dict["DISK_FAILURE"]+=1
    elif(j[3]=="POWER FAILURE"):
      rack_dict["POWER_FAIRULE"]+=1
    elif(j[3]=="CPU ERROR"):
      rack_dict["CPU_ERROR"]+=1
    elif(j[3]=="MEMORY ERROR"):
      rack_dict["MEMORY_ERROR"]+=1
    else:
      rack_dict["UNKNOWN_ERROR"]+=1
    count+=1

for k,v in sorted(rack_dict.items(),key=lambda x: -x[1]):
  print(str(k)+" "+str(round(v/count,2))+"%")