# To Reverse a number
# Enter a number
num = int(input("Enter a number : "))
# initialize the reversenumber = 0
reverseNumber = 0

# Reversing the number
while(num>0):
    lastdigit = num%10
    num = int(num/10)
    reverseNumber = reverseNumber * 10 + lastdigit

#print the reverse number
print(reverseNumber)