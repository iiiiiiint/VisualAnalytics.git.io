#打开和创建相关文件
fp1=open("1-850.csv","r")
data=fp1.read().splitlines()
fp2=open("node.csv","w")
fp3=open("edge.csv","w")
fp4=open("database.txt","w")
fp5=open("nodedep.csv","w")

sum=0    #将用来记录所有节点的出度之和
sum1=0    #将用来记录不依赖其他库的库的个数  
sum2=0    #将用来记录不被其他库依赖的库的个数
verticle=[]  #一个存放节点的集合
degree={}    #查询节点的入度的字典，注意是入度
dict1={}    #存放所有被依赖的节点的字典，其值为被多少个库依赖
out_degree={}  #查询出度为某一值的节点个数，比如出度为5的节点有2个 out_degree[5]=2
in_degree={}   #查询入度为某一值的节点个数，比如入度为5的节点有3个 in_degree[5]=3
dict2={}       #存放所有依赖其他库的节点的字典，其值为依赖多少库
set3=set()     #存放所有被依赖的库的集合
setall=set()
for s in data:
    a=s.split(',') 
    b=[]
    setall.add(a[0])
    for i in a[1:]:
        if(i==""):
            continue
        b.append(i)    #将此节点的依赖的库存入b这个列表
        setall.add(i)    
    dict2[a[0]]=len(b)
    verticle.append(a[0])
    for i in b:
        try:
            dict1[i]+=1    #这个字典中存放了所有被依赖的元素
        except:
            dict1[i]=1
        set3.add(i)
        try:
            degree[i]+=1   #这是入度。
        except KeyError:
            degree[i]=1
    sum+=len(b)   #每个点的出度加起来
    try:
        out_degree[len(b)]+=1
    except KeyError:
        out_degree[len(b)]=1
    if len(b)==0:
        sum1+=1  #sum1是不依赖别的库的库的数量
fp4.write("total:{}\n".format(sum))
fp4.write("average:{}\n".format(sum/len(data)))  #平均度数
fp4.write("not dep:{}\n".format(sum1))




setall=list(setall)
for i in range(0,len(setall)):
    fp2.write(str(i))
    fp2.write(',')
    fp2.write(setall[i])
    fp2.write('\n')
for s in data:
    a=s.split(',') 
    b=[]
    aa=setall.index(a[0])
    for i in a[1:]:
        if(i==""):
            break
        try:
            bb=str(setall.index(i))
            fp3.write(str(aa))
            fp3.write(',')
            fp3.write(bb)
            fp3.write('\n')
        except:
            bb=1
fp4.write("not dep-ed:{}\n".format(len(verticle)-len(set3)))
fp4.write("the number of dep-ed:{}\n".format(len(set3))) #输出被依赖的库的个数
for i in setall:
    try:
        t=degree[i]
    except KeyError: 
        t=0
    try:
        in_degree[t]+=1    #计算度为某一值的库的数量
    except KeyError:
        in_degree[t]=1
d1=sorted(degree,key=degree.__getitem__,reverse=True)
d2=sorted(out_degree,key=out_degree.__getitem__,reverse=True)
d3=sorted(in_degree,key=in_degree.__getitem__,reverse=True)
d4=sorted(dict1,key=dict1.__getitem__,reverse=True)
d5=sorted(dict2,key=dict2.__getitem__,reverse=True)

fp4.write("out_degree:\n")
for i in range(0,9):
    fp4.write("{{value:{},name:'{}'}},\n".format(out_degree[d2[i]],d2[i]))
sum3=0
for i in d2[9:]:
    sum3+=out_degree[i]
fp4.write("{{value:{},name:'others'}}\n\n".format(sum3))
fp4.write("in_degree:\n")

for i in range(0,3):
    fp4.write("{{value:{},name:'{}'}},\n".format(in_degree[d3[i]],d3[i]))
sum4=0
for i in d3[3:]:
    sum4+=in_degree[i]
fp4.write("{{value:{},name:'others'}}\n\n".format(sum4))

fp2.close()
fp3.close()
fp6=open("node.csv","r")
fp7=open("edge.csv","r")
haha=fp6.read().splitlines()
dict3={}
list1=[]
for s in haha:
    a=s.split(",")
    dict3[a[1]]=a[0]
fp5.write("dependented:\n")
for i in range(0,100):
    fp5.write("{},{}".format(dict3[d4[i]],d4[i]))
    fp5.write("\n")
    list1.append(dict3[d4[i]])
# fp5.write("\ndependent:\n")
# for i in range(0,50):
#     fp5.write("{}:{}".format(d5[i],dict2[d5[i]]))
#     fp5.write("\n")
fp8=open("edgedep.csv","w")
haha1=fp7.read().splitlines()
for k in haha1:
    a=k.split(",")
    if a[0] in list1 and a[1] in list1:
        fp8.write("{},{}\n".format(a[0],a[1]))

fp9=open("order.txt","w")
for i in range(0,100):
    fp9.write("{}:{}\n".format(d4[i],dict1[d4[i]]))

fp1.close()
fp4.close()
fp5.close()
fp6.close()
fp7.close()
fp8.close()