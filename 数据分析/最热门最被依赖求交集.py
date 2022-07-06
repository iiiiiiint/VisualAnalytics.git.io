fp1=open("order.txt","r")
fp2=open("hot100.csv","r")
fp3=open("nodehot.csv","w")
fp4=open("edgehot.csv","w")
fp5=open("node.csv","r")
fp6=open("edge.csv","r")
dict1={}
dict2={}
data0=fp5.read().splitlines()
for i in data0:
    a=i.split(",")
    dict1[a[1]]=a[0]
    dict2[a[0]]=a[1]
list1=[]
data1=fp1.read().splitlines()
for i in data1:
    a=i.split(":")
    list1.append(a[0])
sum=0
list2=[]
data2=fp2.read().splitlines()
fp3.write("id,label\n")
for k in data2:
    if k in list1:
        sum+=1
        fp3.write("{},{}\n".format(dict1[k],k))
        list2.append(dict1[k])
fp4.write("source,target\n")
data3=fp6.read().splitlines()
for i in data3:
    a=i.split(",")
    if a[0] in list2 and a[1] in list2:
        fp4.write("{},{}\n".format(a[0],a[1]))

print(sum)
fp1.close()
fp2.close()