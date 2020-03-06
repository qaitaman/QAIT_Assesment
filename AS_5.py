list1 = []
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    list1.append(ele)
def myfunction(x):
  return list(dict.fromkeys(x))

mylist = myfunction(list1)
print(mylist)
