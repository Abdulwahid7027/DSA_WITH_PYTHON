#Enter a Number
num = int(input("Enter a number : "))
#Counter
count = 0
#Counting no. of digits in the given number
while(num>0):
    num = int(num/10)
    count = count + 1

#Prints no. of digits in the given number
print(count)
