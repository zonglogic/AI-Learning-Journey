# 字典可变 无需,无下标
# 以键值对形式存储数据   key:value  通过键获取值,键不能重复,值可以重复

dict1={}
dict2={"name":"jh","gender":"nan","age":"20"}
dict3=dict([("name","jh")])    #二元组转字典

#访问字典元素 dict["key"]

print(dict2["name"])
print(dict2.get("age"))
print(dict2.get("性别"))   #key不存在不会报错

#向字典里添加元素
dict2["address"] = "北京"
print(dict2)

#检查成员是否为字典的key,值无法判断 is "name" in dict2
 
#字典的遍历

for k in dict2.keys():
    print(k)

#遍历所有的value

for v in dict2.values():
    print(v)

#遍历kv
for k in dict2.keys():
    print(f"{k}------{dict2[k]}")

for k,v in dict2.items():
    print(k,v)






