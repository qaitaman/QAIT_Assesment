l= int(input())
u= int(input())
li = []
a = 0
for num in range(l, u + 1):
   if num > 1:
       for i in range(2, num):
           
           if (num % i) == 0:
               break
       else:
           li.append(num)
           a += 1
print(li)
