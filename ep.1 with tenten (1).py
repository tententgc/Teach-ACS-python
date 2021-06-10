#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello")


# In[2]:


a = input()
print(a)


# In[23]:


#string => ข้อความ ตัวอักษร ' "" '''
#number => integer , float
#boolean => true , false
print(-1)
print(0)
print("1"+"9")
print(3.99)
print(True)
print(False)
print("tenten \n" + "TGC")


# In[22]:


# Data Type & Variable
# ชื่อตัวแปร = ค่าที่เก็บในตัวแปร

x = 20 #integer
y = 3.99 #float
z = True #logic
#print("ผลลัพธ์ = "+str(x))
# print(y)
# print(z)
print(type(y))
print(type("tentenTGC"))
print(type(z))


# In[8]:


#กฎการตั้งชื่อ

"""
1.ใส่ตัวเลข ตัวอักษร เครื่องหมาย 
2.ห้ามขึ้นต้นด้วยตัวเลขและสัญสักษณ์ ยกเว้น _ 
3.ห้ามซ้ำกับ keywords
4.case sensitive 
"""

name="A"
NAME="B"
nAmE="C"

print(name)
print(NAME)
print(nAmE)


# In[20]:


#Type Coversion
x = 10
y = 3.14
z = "20"

#"20" = > 20
# 10 => "10"

z1 =str(x)
print(z+z1)
# "10" + "20" ="1020" => result




# 10+3.14 = 13.14
print(x+y)




# string => int 
# int => string

#string => float
#float => string

# int => float
# float => int
# บวกเลข 
z=float(z)
z=z+50
print(z)


# In[1]:


# input
x=int(input("ป้อนตัวเลขตัวที่ 1 : ")) #รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร fname
y=int(input("ป้อนตัวเลขตัวที่ 2 : "))
#process & output 
print(x+y)


# In[20]:


# ตัวดำเนินการทางคณิตศาสตร์
x = 10
y = 3

print("ผลบวก" , x+y)
print("ผลลบ" , x-y)
print("ผลคูณ", x*y)
#n=x/y
#print("ผลหาร",round(n,2))
#print("ผลหาร",round(x/y,2))
#print("ผลหาร",f'{x/y:.2f}')
print("หารปัดเศษ", x//y)
print("ยกกำลัง",x**y)
print("หารเอาเศษ",x%y)


# In[23]:


a = 6.789809823
print('%.2f' %a)
print("ผลหาร",round(a,2))
print("ผลหาร",f'{a:.2f}')
print ("{0:.2f}".format(a)) 


# In[27]:


import math
x=2.0164565
math.ceil(x) # ข้ามไปก่อนค่อยมาสอน


# In[31]:


#ตัวดำเนินการเปรียบเทียบ(เช็ค logic)

# นำข้อมูลอย่างน้อย 2 ค่ามาเปรียบเทียบกัน
# ชนิดข้อมูลเหมือนกัน
# คำตอบ 2 คำตอบ => จริง / เท็จ

x,y,z = 8, 7,5

#print("ค่า x มากกว่า y หรือไม่ ? : ",x>y)
# print("ค่า x น้อยกว่า y หรือไม่ ? :", x<y)
# print("ค่า x เท่ากับ y หรือไม่ ? :", x==y)
# print("ค่า x ไม่เท่ากับ y หรือไม่ ?",x!=y)

# print("ค่า x มากกว่า หรือ เท่ากับ ค่า y หรือไม่ ?",x>=y)
# print("ค่า x น้อยกว่า หรือ เท่ากับ ค่า y หรือไม่ ?", x<=y)

#และ
print("ค่า x มากกว่า y และ y มากกว่า z หรือไม่ ? : ",x>y>z)
print("ค่า x น้อยกว่า y และ y น้อยกว่า z หรือไม่ ? : ",x<y<z)


# In[38]:


#ตัวดำเนินการทางตรรกศาสตร์

#AND = และ
#OR = หรือ
#NOT = ไม่

#คำตอบที่ได้ => จริง / เท็จ

x = (10>5) #ค่า x = bool
y = (10==5) #ค่า y = bool

#z = (5>10) and (10==5)
# 5>10 and 10 == 5 
#z = (10>5) or (10==5)

print(not z)


# In[40]:


x=10
print("ก่อน",x)
# x+=5 # x=x+5
# x-=15 # x = x-15
# x*=5 # x=x*5
# x/=5 # x=x/5
# x//=5
# x**=2 # x= x**2
x%=3 # หาเศษที่เหลือของกรหาร
print("หลัง",x)


# In[58]:


#ลำดับความสำคัญของตัวดำเนินการทางคณิตศาสตร์

x=5+2/10*2-1# 5+0.4-5
print(x)


# In[67]:


#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)
# input / convert to integer
weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
print("BMI = ",round (weight/(high**2),2))
# ไว้สอนเขียน tkinter + if else  แสดงค่าผอมมากผอมน้อยทีหลัง


# In[69]:


age=int(input("ป้อนอายุของคุณ :"))
#35
if age>=15 and age <=20:
    print("วัยรุ่น")
elif age>=20 and age<=29:
    print("วัยหนุ่มสาว")
elif age>=30 and age<=39:
    print("วัยผู้ใหญ่")
elif age>=80:
    print("วัยชรา")
else :
    print("วัยเด็ก")

print("จบโปรแกรม")

# 15 - 20 => วัยรุ่น
# 21 - 29 => วัยหนุ่มสาว
# 30 - 39 => วัยผู้ใหญ่


# and or not 


# ดัชนีมวลกาย (BMI)   =   น้ำหนักตัว (กิโลกรัม)
# 
#                                    ส่วนสูง (เมตร)2
# 
#             โดยสามารถแปลผลค่า BMI ได้ดังนี้
# 
# ค่า BMI < 18.5              แสดงถึง            อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม
# 
# ค่า BMI 18.5 – 22.90     แสดงถึง            อยู่ในเกณฑ์ปกติ
# 
# ค่า BMI 23 – 24.90        แสดงถึง            น้ำหนักเกิน
# 
# ค่า BMI 25 – 29.90        แสดงถึง            โรคอ้วนระดับที่ 1
# 
# ค่า BMI 30 ขึ้นไป            แสดงถึง            โรคอ้วนระดับที่ 2

# In[72]:


weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
BMI = round (weight/(high**2),2)
if BMI<18.5:
    print("อยู่ในเกณฑ์น้ำหนักน้อยหรือผอม")
elif BMI>=18.5 and BMI<23:
    print("อยู่ในเกณฑ์ปกติ")
elif BMI>=23 and BMI<25:
    print("น้ำหนักเกิน")
elif BMI>=25 and BMI<30:
    print("โรคอ้วนระดับที่ 1")
else :
    print(" โรคอ้วนระดับที่ 2")
print(BMI)


# In[ ]:


BMI=int(input("ป้อนอายุของคุณ :"))
#Ternary Operator
print("วัยรุ่น") if BMI>=15 else print("วัยเด็ก")

print("จบโปรแกรม")

# 15 - 20 => วัยรุ่น


# and or not 


# In[73]:


# if ซ้อน if
age=int(input("ป้อนอายุของคุณ : "))

if age<=15:
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")


# In[74]:


# pass
age=int(input("ป้อนอายุของคุณ : "))

if age<=15:
    if age==15:
        pass
    elif age==14:
        pass
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")


# In[75]:


# เขียนโปรแกรมหาตัวเลข มาก / น้อย

a=int(input("ป้อนตัวเลขที่ 1 :"))
b=int(input("ป้อนตัวเลขที่ 2 :"))

if a>b :
    print(a," มากกว่า ",b)
else :
    print(a," น้อยกว่า ",b)


# In[76]:


#หาเลขคู่ / คี่

number = int(input("ป้อนตัวเลขของคุณ :"))

# ถ้าหาร 2 ลงตัว => คู่
if number % 2 == 0:
    print("เป็นเลขคู่")
else :
    print("เป็นเลขคี่")


# In[77]:


#แลกเงินและหาจำนวนแบงค์

# 2000 => 1000 => 2 ใบ
# 1500 => 1 ใบ , 500 = 1 ใบ
# 1800 => 1 ใบ , 500 = 1 ใบ , 100 => 3 ใบ
# 100 => 50 => 2 ใบ

number = int(input("ป้อนจำนวนเงินของคุณ : "))

# 1500
if number>=1000:
    print("1000 บาท = ",number//1000,"ใบ") # 1 ใบ
    number%=1000 # 1500 % 1000 = 500

if number>=500:
    print("500 บาท = ",number//500,"ใบ")
    number%=500

if number>=100:
    print("100 บาท = ",number//100,"ใบ")
    number%=100

if number>=50:
    print("50 บาท = ",number//50,"ใบ")
    number%=50

if number>=20:
    print("20 บาท = ",number//20,"ใบ")
    number%=20


# In[78]:


# แปลง ค.ศ เป็น พ.ศ
# แปลง พ.ศ เป็น ค.ศ

number = int(input("ป้อน พ.ศ :"))

# แปลง ค.ศ เป็น พ.ศ + 543
# แปลง พ.ศ เป็น ค.ศ - 543
number=number-543

print("เป็น ค.ศ = ",number)


# In[80]:


name="11504566"

if name.endswith("11504566"):
    print("ถูกหวย")
else :
    print("ไม่ถูกหวย")


# In[88]:


#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศาเช่น 45C or 20f ) :") #45C

degree= int(temp[:-1]) #45
unit=temp[-1].upper() #C


if unit=="C" :
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"

print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ","{0:.2f}".format(result))


# In[93]:


# โครงสร้างควบคุมแบบทำซ้ำ
summation=0

for i in range(1,11): # summation
    print("รอบที่  = ",i)
    summation += i #summation = summation + i

print("ผลรวม = ", summation)
print("เฉลี่ย = ", summation/10)


# In[97]:


# Loop ซ้อน Loop
i=1
while i<=3 :
    j=1 # ตัวนับ
    while j<=5:
        print("รอบที่ = ",i," ตำแหน่งที่ = ", j)
        j+=1
    i+=1


for i in range(1,4):
    print("รอบที่ = ",i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ", j)


# In[98]:


start=int(input("ป้อนแม่สูตรคูณเริ่มต้น = ")) # 1
stop=int(input("ป้อนแม่สูตรคูณสุดท้าย = ")) # 4

for x in range(start,stop+1):
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,'x',y ," = ",(x*y))


# In[99]:


for i in range(1,11):
    print(i)
    if(i==5):
        break

print("จบโปรแกรม")


# In[103]:


sum_input = int (input("ใส่จำนวนที่ต้องการบวก"))
start , stop = 1,sum_input
sum ,avg =0,0
while (start<=stop):
    number=int(input("ป้อนตัวเลขของคุณ :"))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    start+=1

avg=sum/stop
print("ผลรวม = ", sum)
print("ค่าเฉลี่ย  = ",round(avg,2))


# In[106]:


sum = 0 
while True:
    number=int(input("ป้อนตัวเลขของคุณ :"))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    if sum>=100:
        break
    print("ผลรวม = ", sum)
print(sum)


# In[3]:


# ค้นหาตัวเลข มากสุด / น้อยสุด

max ,min = 0,9999
while True :
    number=int(input("ป้อนตัวเลขของคุณ :")) 
    #กระโดดออกจาก loop
    if number<0 :
        break
    if number>max :
        max=number
    if number<min:
        min=number

print("ค่าสูงสุด = ", max)
print("ค่าต่ำสุด = ",min)


# In[5]:


# ตัวเลขขั้นบันได

"""
input = 10

1
12
123
1234
12345
123456

"""

last=int(input("ป้อนตัวเลข = "))

for row in range(1,last+1): 
    for column in range(1,row+1):
        print(column,end='')
    print(" ")

"""
input = 3

row = 1 , 3
column 1,2
1

row 2
column 1, 3
12

row 3
column 1,4
123

"""


# In[12]:


#สร้างภาพวาด 4 เหลี่ยมจตุรัส

"""
3x3
xxx
xxx
xxx

2x2
xx
xx

5x5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx

"""

number=int(input("ป้อนขนาด  = ")) # 5 => 0,1,2,3,4

"""

"""
for row in range(number) :
    for column in range(number):
        print("x",end="") #end =" "  = ให้ขึ้นยรรทัดเดิม
    print(" ")


# In[15]:


# ตารางหมากฮอต

"""
xxx
xxx
xxx

x = สีน้ำตาล
o = สีขาว
"""
number=int(input("ป้อนขนาด  = "))
for row in range(number) :
    for column in range(number):
        print("x",end=" ") if (row+column)%2 == 0 else print("o",end=" ")

    print(" ")

# 3 x 3 
# row = 0 +  column = 0  
# row = 0 +  1 
# row = 0 +  2

# row = 1 +  column = 0  
# row = 1 +  1 
# row = 1 +  2

# row = 2 +  column = 0  
# row = 2 +  1 
# row = 2 +  2


"""
xox
oxo
xox
"""


# In[19]:


# สร้างขอบตาราง

number=int(input("ป้อนขนาด  = ")) 
for row in range(number) :
    for column in range(number):
        if row==0 or row==number-1 or column==0 or column==number-1:
           print("x",end="")
        else:
            print(" ",end=" ")
    print(" ")


# In[1]:


# เกมทายเลขลูกเต๋า
# 1,2,3,4,5,6

import random
#สุ่มเลขลูกเต๋า
myrandom = random.randrange(1,7) # 1 - 6
k=1
correct=False
print("คุณมีโอกาสตอบ 3 ครั้ง \n")
#print(myrandom)
while True:
    number=int(input("ป้อนคำตอบของคุณ = "))
    correct=(number==myrandom) # true / false
    if not correct :
        if(number>myrandom):
            print("น้อยกว่า")
        if(number<myrandom):
            print("มากกว่า")

    if correct :
        print("ตอบถูกรับไปเลย 1 ล้านบาท")
        break
    if number<0 or k==3:
        break
    k+=1

if not correct :
    print("เสียใจด้วยนะ")
    print("เฉลย =" , myrandom)


# In[ ]:




