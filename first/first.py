import os
import numpy as np
import pandas as pd
import random as rand
# print("hello world")
# # print(os.listdir("C:/MinGW"))
# a = 6
# print(a,type(a))
# io = 45.7777
# print(int(io))
# if(not a>5):
#     print("Yes")
# else:
#     print("nop")    

# h = int(input("Enter the num\n"))
# print(type(h))
#practice set
# a =9
# i =7
# print(a+i)
# a = int(input("Enter the number: "))
# print(a%2)
# a = input("Enter: ")
# print(type(a))
# a = 34
# b = 80
# print(a>b)
# a = int(input("Enter num"))
# b = int(input("Enter num"))
# print("avg is",(a+b)/2)
# a = int(input("Enter num: "))
# print(a*a)
# a = 98
# h = "hello"
# print(h[0:3])
# print(h[-4:-1])
# jk = "justfkinkiddin"
# # print(jk[0::2])
# # print(jk.count("n"))
# # print(jk.capitalize())
# # print(jk.find("fkin"))
# # print(jk.upper())
# # print(jk.index("in"))
# # print(jk.rindex("in"))
# print(jk.replace("fkin","notfkin"))

#practice set
# a = input("Enter your name")
# print(a+" good afternoon")
# n = input("Enter naem")
# d = input("Enter date")
# a = '''Dear {}
# your date is {}
# ''',format(n,d)
# print(a)
# a = "hello  how  r  o ets"
# print(a.count("  "))
# print(a.replace("  "," "))
# a = "Dear maam\nit is my honour to\t fk u!"
# print(a)
# a = [1,2,3,5,67,8,9,0]
# temp = None
# for i in range(0,int(len(a)/2)):
#     temp = a[i]
#     a[i] = a[len(a)-i-1]
#     a[len(a)-i-1] = temp
# print(a)    
#list methods
# list = [1,24,3,7,9,47,3,8,2]
# list.sort()
# print(list)
# print(list.count(3))
# list.reverse()
# print(list)
# list.append(4)
# print(list)
# list.insert(4,866)
# print(list)
# list = [1,23,5,7,8,9,0,6]
# list.pop(4)
# print(list)
# list.remove(0)
# print(list)
#practice set
# list  = []
# for i in range(4):
#     ele = input()
#     list.append(ele)
# print(list)    
# marks = []
# for i in range(5):
#     ele = int(input("marks "))
#     marks.append(ele)
#     marks.sort()
# print(marks)    
# nums =[1,2,3,4,5]
# sum = 0
# for i in range(0,int(len(nums))):
#     sum+=nums[i]
# # print(sum)    
# list  = [7,0,8,0,0,9]
# print(list.count(0))
# t1 = (1,2,46,75,3,7,6,3,73,5,7,34)
# print(t1.count(7))
#Dictionaries and sets
# dict = {"hello":"sup","mfx":"mfs","anotherdict":{'dict2':'kill'},"list":[1,23,456,87,45]}
# print(dict['anotherdict']['dict2'])
# print(dict["list"])
#Dictionary methods
# dict = {
#     "key1":"Value1",
#     "key2":"Value2",
#     "Key3":"Value3"
# }
# dict2 ={
#     "key 6":"value6",
#     "key7":"value8"
# }
# print(dict.keys().__contains__("key2"))
# print(dict.values())
# dict.update(dict2)
# print(dict.items())
# print(dict.get('key2'))
#Sets
# a = set()
# #set methods
# a.add(34)
# a.add(54)
# a.add(99)
# a.add(89)
# a.remove(34)
# a.pop()
# print(a)
#practice set
# s = set();
# s.add(19)
# s.add("19")
# print(s)
# s = {};
# print(type(s))
# dict = {'vaha':'there','yaha':'here','aana':'come'}
# print(dict.keys())
# choose = input("Enter the key: ")
# print(dict.get(choose))
# set = set()
# for i in range(0,9):
#     a = int(input("Enter num: "))
#     set.add(a)
# print(set)
# set = set()
# set.add(20)
# set.add(20.2)
# set.add("20")
# print(len(set))
# dict = {};
# for i in range(4):
#     name = input("enter name: ")
#     f = input("Enter the value: ")
#     dic = {name:f}
#     dict.update(dic)
# print(dict)
# a =90;
# if(a>6):
#     print("Yo")
# elif(a>9):
#     print("sup")
# else:
#     print("Done")    
# age = int(input("Enter age: "))
# if(age>=18):
#     print("Greater")
# else:
#     print("Lesser")    
#IN and IS
# a = None
# if(a is None):
#     print("None")
# else:
#     print("Not None")
# list = [1,23,65,87,3]
# if(3 in list):
#     print("Yes")
# else:
#     print("no")    
#practice set
# a = 98
# b = 4399
# c = 5000
# d = 165
# if(a>b and a>c and a>d):
#     print("A is big")
# elif(b>a and b>c and b>d):
#     print("B is big")
# elif(c>a and c>b and c>d):
#     print("C is big")
# else:
#     print("D is big")    
# a = "buy now"
# list = ["make a lot of money","buy now"]
# spam = False
# for i in range(len(list)):
#     if(list[i] in a):
#         spam = True;
#     else:
#         spam = False  

# print(spam)        
# username = "xandar03"
# if(len(username)>=10):
#     print("its big")
# else:
#     print("it smole")    
# list = ["aayush","john","mio","mizu"]
# name = "aayh"
# if(name in list):
#     print("yes")
# post = str(input("Enter the post: "))
# if(post.find("Harry")>=0 or post.find("harry")>=0):
#     print("harry h")
# else:
#     print("Nop")    
# i = 10
# while(i>0):
#     print(i)
#     i = i-1
# num = 0
# while(num<=50):
#     print(num)
#     num = num +1
# list = [1,232,433,4,5,6,7,8]
# i = 0
# while(i<len(list)):
#     print(list[i])
#     i=i+1
# for item in list:
#     print(item)
# for i in range(1,11):
#     print(9*i)
#practice set
# i = 0;
# while i<=20:
#     if(i>=10):
#         print(i)
#     i = i+1    
# a = 9
# for i in range(1,11):
#     print(a,"X",i,"=",a*i)
# list = ["harry","sachin","soham","rahul"]
# for i in range(0,len(list)):
#     if(list[i].startswith('s')):
#         print("hello",list[i])
# a = 9
# i = 1
# while(i<=10):
#     print(a,"X",i,"=",a*i)
#     i = i+1
# a = int(input("Enter a num: "))
# if(a%2==0):
#     print("Its prime")
# else:
#     print("No")    
# i = 1
# sum=0;
# while(i<=10):
#     sum+=i
#     i=i+1
# print(sum)    
# i = 3
# fact= 1
# for o in range (1,i+1):
#     fact = fact*o
# print(fact)    
# p = 4
# for i in range(p):
#     print("#"*(i+1))
# n = 9
# for i in range (10,0,-1):
#     print(n*i)
# a = int(input("Enter a number\n"))
# for i in range(0,a+1):
#     print(f"{i}")
#functions and recursion
# def add(a , b):
#     return a+b

# a = add(5,5);
# print(a)
# def greet(st):
#     print("Hello "+str(st).upper())

# greet("aayush")    
# def fib(a):
#     if(a<=1):
#         return a;
#     else:
#         return fib(a-1) +fib(a-2)    

# fi = fib(6)
# print(fi)    
# def fact(a):
#     if(a == 0):
#         return 1
#     return int(a)*int(fact(a-1))

# fac = fact(4)
# print(fac)   
# def star(n):
#     if(n==0):
#         return
#     star(n-1)       
#     for i in range(n):
#         print("# ",end = "")
#     print(" ")   
   

# star(5)
#practice set
# def greatest(n , n1, n2):
#     if(n>n1 and n>n2):
#         print("1 is great")
#     elif(n1>n and n1>n2):
#         print("2 is great")
#     else:
#         print("3 is great")        

# greatest(14,6,1)        
# def convert(cel):
#     return (cel * 9/5) + 32

# faren = convert(67)
# print(faren)    
# print("hello ",end="")
# print("World",end="\t")
# print("this is me")

# def recurSum(n):
#     if(n==0):
#         return 0
#     return n + recurSum(n-1)

# print(recurSum(10))

# def star(n):
#     for i in reversed(range(n+1)):
#         for j in reversed(range(i+1,n+1)):
#             print("# ",end="")
#         print(" ")    

# star(6)    
# def conInToCm(inn):
#     return float(inn)*2.54

# cms = conInToCm(12)
# print(cms)    

# def multi(n):
#     for i in range(1,11):
#         print(f"{n}X{i} = {n*i}")

# multi(2)        

# def multiRecur(n,i):
#     if( i > 10):
#         return
#     print(n*i)    
#     multiRecur(n,i+1)    

# print(multiRecur(2,1))
# def delete(str , list):
#     if str in list:
#         list.remove(str)

#     print(list)    

# list = ["hello","world","how u"]
# delete("hello",list)    
# def remNdStrip(st,sti):
#     new = st.replace(sti,"")
#     print(new.strip())

# this = "hello this a sentence "
# remNdStrip(this,"hello")    
# FIle  IO
# open("This.txt",'w')
# f = open("This.txt",'r')
# fg = open("This.txt",'w')
# fg.write("Hello mfs")
# fg.close()
# print(f.read())
# # print(f.read(3))
# f.close()
# f = open("This.txt",'r')
# print(f.readline())
# for i in f:
#     if 'life' in i:
#         print(i)
# f = open("This.txt",'rb')
# for line in f:
#     print(line)
# f = open("This.txt",'a')
# f.write("This is a line")
# f.close()
# with open("sample.txt",'w') as w:
#     w.write(input("Enter your text: "))

# f = open("sample.txt",'r')
# gg = f.readline()
# print(gg)
# f.close()
#Practice set
# poem = open("poems.txt")
# t = 0
# # for line in poem:
# #     if "twinkle" in line:
# #         t+=1
# print(t)
# def game():
#     counter = 0
#     score = 0
#     a = rand.randint(1,10)
#     while(counter!=5):
#         user = int(input("Enter your guess: "))
#         if(user == a):
#             print("same")
#             score+=10
        
#         elif(user>a):
#             print("Your number is bigger")
        
#         elif(user<a):
#             print("your number is smaller")    

#         else:
#             print("Enter valid command")    
#         counter+=1    
#     print("Game over")
#     score+=1
#     with open("hi-score.txt",'a') as hi:
#         hi.write(f"\n{score}")

# game()        
# os.makedirs("13 year old")
# table = open("13 year old/Tables.txt",'w')
# ta = 2
# while(ta!=21):
#     for i in range(1,11):
#         table.write(f"{ta}X{i}={ta*i}\n")
#     table.write("\n")
#     ta+=1
# don = open("donkey.txt",'r+');
# for line in open("donkey.txt","r"):
#     if "donkey" in line:
#         don.write(line.replace("donkey","######"))
# don.close()   

# list = ["bitch","slut","whore","fuck","mfs"]

# with open("cen.txt",'r') as f:
#     content = f.read()

# for word in list:
#     content = content.replace(word,"$%^%$")
#     with open("cen.txt",'r+') as le:
#         le.write(content)    

# with open("log.log") as log:
#     con = log.read()
#     if "python" in con:
#         with open("log.log",'r+') as ch:
#             con = con.replace("python","%$$@$%")
#             ch.write(con)     

# con = True
# i = 1
# with open("log.log") as log:
#     while con:
#         con = log.readline()
#         if 'python' in con:
#             print(i)
#         i+=1     

# fi = open("Ohis.txt",'w')
# with open("that.txt",'r') as f:
#     for line in f:
#         fi.write(line)

# with open("teo.txt",'w') as te:
#     for i in range(1,11):
#         te.write(f"2X{i}={2*i}\n")

# with open("ohis.txt",'w') as oh:
#     with open("teo.txt",'r') as p:
#         for line in p:
#             oh.write(line)
