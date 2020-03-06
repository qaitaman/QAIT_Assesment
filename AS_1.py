list1 = "The best programs are written badly"
count = len(list1)
a = 0
for i in range(0, count):
    if list1[i] == " ":
        a+=1
    
print(count - a)