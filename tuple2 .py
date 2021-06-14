
#lis = [1, 2, 3, 4, "tenten", "tgc", True, 3.99]
#lis[0]="กทม." #list ทำได้ tup แก้ไข้ไม่ได้

#print(lis)
tup = (1, 2, 3, 4, "tenten", "tgc", True, 3.99)
print(tup[0])
lis = list(tup)
lis[0] = "กทม."
print(lis)
tup = tuple(lis)
print(tup[0])
#tuple >>> list >>>>tuple วิธีแก้ไข tuple
 