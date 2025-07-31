import random

list = []

for i in range(0,10):
   list.append(random.random())

   sum = 0 
for l in list:  
 sum += l
print(sum)
