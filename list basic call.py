a = 1
a1 = 2
a2 = 3
number = []  # list ว่าง
number = [1, 2, 3, 4, 5, 6]  # list สมาชิก1-6
name = ["นายA", "นายb", "นายc"]  # list name สมาชิกเป็นชื่่อ คน OBJ = str
all_list = [9, "นาย A", 3.14, True, -1]
#constructor
#number=list(["นายA","นายb","นายc"])
#how to call for use list
print(name)
print(all_list)
print(type(name))
print(number[1])
print(name[0])
print(type(name[0])) #ถ้าเรียกคอลตำแหน่ง จะแสดง ประเภทของข้อมูลตัวนั้นออกมา
print(number[0]+number[1]) # เรียกค่าลิสต์มาบวกกันเป็นนการเรียกตัวแปรมารวมกัน
print(name[0]+name[1]) #if ใส่ index เกิน list จะเป็น out of range
print(all_list[2])
print(all_list[-2]) #เอาค่ามาจากข้างหลัง
print(all_list[1:4])
print(all_list[-3:-1])# ก่อน -1  
print(all_list[:-1])
print(all_list[1:]) #จุดเริ่มต้นไปจุดสุดท้าย
