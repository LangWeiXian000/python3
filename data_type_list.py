import style as style

bicycles = ['test1', 'test2', 'test3', 'test4']
print(bicycles)
'''
列表用方括号[]来表示，并用都好来分隔其中的元素
'''
# 访问列表元素
print(bicycles[0])  #索引从左往右0，1,2,3，从右往左-1，-2，-3，-4
print(bicycles[0:2])  # 从左往右到第2个元素，不包括2，即打印0,1
print(bicycles[0].title())
#访问列表中的各个值
message = "My first bicycle was a " + bicycles[-2].title() + "."#取bicycles中的倒数第2个元素并将其首字母大写
print(message)
'''
练习题：
1、将姓名存储在names列表中，依次访问列表中的每个元素
2、用第一题中的列表，为没人打印一条消息，每条都包含相同的问候语，但抬头为相应朋友的姓名
3、创建一个列表，根据该列表打印相应的消息
'''
#第一题
names = ['zhouhui','karl','wenqi','alice']
print(names[0:4])
#第二题
message = " you're beautiful!"
message1 = " you're cool!"
print(names[0]+message)
print(names[1]+message1)
print(names[2]+message)
print(names[3]+message)
#第三题

#修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'honda1'
print(motorcycles)
motorcycles.append('ducati')#append()在列表末尾添加新元素
print(motorcycles)

motorcycles1 = []#创建一个空列表，添加列表的元素
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)

#在列表中插入元素
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(2,'test')#insert()指定新元素的索引和值
print(motorcycles)
del motorcycles[2]#del语句删除指定位置的元素
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del_motorcycle = (motorcycles).pop()
print(motorcycles)
print(del_motorcycle)

#例子:假设列表中的摩托车是按购买时间存储的，就可以使用pop()打印一条消息，指出最后购买的是哪款摩托车
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
test = motorcycles.pop(0)#pop()可以用来删除列表中任何的元素，需要在括号中指定要删除的元素的索引即可
print(test)
'''
如何判断是使用del语句还是pop()方法？判断标准：
如果你要从列表中删除一个元素且不再以任何方式使用它，就用del语句
如果你要在删除元素后还要使用它，就用pop()方法
'''

#根据值删除元素可以使用remove()方法
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')#直接删除ducati值
print(motorcycles)

#使用remove()删除元素时，也可以接着用他的值，下面删除值ducati并打印一条消息，指出从列表删除的原因
motorcycles = ['honda','yamaha','suzuki','ducati']
too_exp = 'ducati'
motorcycles.remove(too_exp)
print(motorcycles)
print("\nA "+too_exp.title() + " is too expensive for me")
'''
注意：remove()方法只删除第一个指定的值，如果删除的值可能在列表中出现多次，就要使用循环来判断是否删除了所有这样的值
'''


#组织列表
# sort（）可以对列表进行排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()#不带参数，默认按字母顺序排列
print(cars)
cars.sort(reverse=True)#加入参数，变成字母倒序排列
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("This is :")
print(cars)

print("\nThis is sorted list :")
print(sorted(cars))#不带参数，默认按字母顺序排列

print("\nThis is again list :")
print(sorted(cars,reverse=True))#加入参数，变成字母倒序排列
'''
sort()对列表永久排序
sorted()对列表临时排序
以上两个方法都可以带reverse=True参数，可按字母进行倒序排列，不带参数时默认按字母顺序排列
reverse()可以反转列表元素的排列顺序
注意：reverse()不是指按字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
'''
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)
print(len(cars))#获取列表的长度，python计算列表元素时从1开始

#题目
list = ['test','test2','eat','shanghai','five']
print(list)
print(sorted(list))
print(list)
print(sorted(list,reverse=True))
print(len(list))


