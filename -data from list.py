#remove, pop,del,clear
number = [1, 2, 3, 4, 5, 6, 10]
fruit = ["mango", "grape", "apple"]
fruit.append("dgt")
fruit.append("water melon")
fruit.insert(1, "มะนาว")
print(fruit)
#remove ลบออกไป
fruit.remove("mango")
print(fruit)
#pop เอาตัวสุดท้ายออก
fruit.pop()
print(fruit)
#del - index ใช้ลบโดยระบุ index
del fruit[0]
#ถ้าใช้ del fruit เฉยๆจะลบหน่วยความจำออกไปเลย ลบตัวแปรออกไปเลย
print(fruit)
#clear เอาออกทุกอย่าง เหลือกล่องเปล่า
fruit.clear()
print(fruit)
