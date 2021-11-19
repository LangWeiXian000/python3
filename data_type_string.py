
#一、使用方法修改字符串的大小写
a = "this is string. this is also a string"
b = 'this is string'
print(a.title())#将字符串首字母转换成大写
print(a.upper())#将字符串全部转换为大写
print(b.title())#将字符串首字母转换成大写
print(b.lower())#将字符串全部转换成小写
'''
title()以首字母大写的方式显示每个单词，即每个单词的首字母都大写，
这个很有用，因为你经常需要将名字视为信息。如：你可能希望将Ada/ADA/ada视为同一个名字，并将它们都显示为Ada
upper()将字符串全部转换成大写
lower()将字符串全部转换成小写
'''

#二、合并字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("hello,"+full_name.title()+"!")
#创建消息，再把整条消息都存储到一个变量中：
message = "hello,"+ full_name.title() + "!"
print(message)
#使用制表符或换行符来添加空白
print("\tmessage")#添加制表符\t
print("Languages:\nPython\nC\nJavascript")#添加换行符\n
print("Languages:\n\tPython\n\tC\n\tJavascript")#换行符和制表符可同时使用，意思是让python换行到下一行，并在下一行的开头添加一个制表符
#删除字符串中的空白
language = 'python '
print(language)
print(language.rstrip())#删除字符串末尾多余的空白
language = language.rstrip()#将删除空白后的字符串赋值给变量
print(language)
language1 = " hello python "
language2 = " hello"
print(language2.lstrip())#删除字符串开头的空白
print(language2)
print(language1.strip())#同时删除字符串两端的空白
print(language1)
'''
总结：
rstrip()删除字符串末尾的空白
strip()同时删除字符串两端的空白
lstrip()删除字符串开头的空白
'''
'''
练习题:
1、个性化消息：将用户名称存到一个变量中，并向改用户显示一条消息。消息为：“Hello Eric, would you like to learn some Python today?”
2、调整名称的大小写：将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名
3、名言：找一句名言，将这个名人的姓名和他的名言打印出来。
4、重复练习第3条，但将人的姓名存储在变量famous_person中，再创建要显示的信息，并将其存储在变量message中，然后打印这条消息
5、剔除人名中的空白，存储一个人名，并在其开头和结尾都包含一写空白字符。务必至少使用字符组合"\n"和"\t"各一次。
'''
#第一题
name = "Eric"
message = "hello "+ name + ", would you like to learn some Python today?"
print(message)
#第二题
name = "EriC"
print(name.lower(),name.upper(),name.title())
#第三题
name = "Albet Einstein"
quo = ' once said,"A person who never made a mistake never tried anything new."'
print(name+quo)
#第四题
famous_person = "Albet Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(famous_person + " once said," + message)
#第五题
name = ' Alice '
name1 = name.lstrip(),name.rstrip(),name.strip()
print(name1)
name2 = ' \tAlice'
name3 = '\nAlice '
name4 = '\n\t Alice '
print(name2.lstrip(),name3.rstrip(),name4.strip())