number=input("enter a number:")
length=len(number)
sum=0
for digit in number:
    sum += int(digit)**length
    
if sum==int(number):
    print("true")
else:
    print("false")