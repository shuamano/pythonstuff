doubled = [1]

for value in range(10000000):
   double_this = doubled.pop()
   doubled.append(double_this * 2)  
   print(doubled)
#yay it works