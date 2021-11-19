names = ['zhouhui','karl','test','alice']
for name in names:
    print("\n"+name.title()+" is so best!")
    print("you best for me, " +name.title() + "." )
print("\nthank you!")

pizzas = ['Beefpizza','Tomatopizza','Onionspizza']
for pizza in pizzas:
    print("\n"+pizza)
    print("I like "+ pizza + "!")
print("\nI really love pizza!")


animals = ['dog','pig','rabbit','tiger']
for animal in animals:
    print("\n"+animal)
    print("A "+ animal + " would make a great pet.")
print("\nAny of these animals would make a great pet!")

for value in range(2,6):#输出不包含第二个值
    print(value)

#使用range()创建数字列表
numbers = list(range(1,6))
print(numbers)
#使用range()指定步长
numbers = list(range(2,11,3))#从2开始不断加3（这里是指步长），直到超过终值11
print(numbers)

#遍历1-10的平方
squares = []
for value in range(1,11):
    square = squares.append(value **2)
print(squares)