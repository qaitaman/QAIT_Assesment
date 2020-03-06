le = "The best programs are written badly."
# print('Total words:   ', len(le.split()))
flag = 0
a = "."
b=le[-1]
if a != b:
    flag=1
c = le.count('.')

print('sentenceCount    ', flag + c)
# print(flag)
# print(le[-1])
# print(a)
