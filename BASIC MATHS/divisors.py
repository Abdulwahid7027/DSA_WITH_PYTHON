# To print the divisors of a number
# Enter a number
num = int(input("Enter a number : "))

for i in range(1,num+1):
    if num%i == 0:
        #print the divisors
        print(i)