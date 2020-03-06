print("Enter Number Of Games You Want To Play")
GT = int(input())
SPP = {'SP':100,'CL':50,'HT':-100,'DD':-50}
PP = []
PP1 = []
PP2 = []
P1 = 1000
P2 = 1000
# def get_key(val): 
#     for key, value in SPP.items(): 
#          if val == value: 
#              return key 
  
# SP = 100
# CL = 50
# HT = -100
# DD = -50
print("Enter Person 1")
for i in range(0,GT):
    for j in range(0, 2):
        PP = input()
        A = SPP[PP]
        P1 +=A
print("Enter Person 2")
for i in range(0,GT):
    for j in range(0, 2):
        PP = input()
        A = SPP[PP]
        P2 +=A
        
if P1>P1:
    print("player1")
else:
    print("player2")
    
# print(P1)

