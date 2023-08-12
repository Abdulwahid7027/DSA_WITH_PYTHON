# To check whether a number is palindrome or not
# Enter a number
num = int(input("Enter a number : "))

temp = num
reverseNumber = 0

# Reversing the number
while(num>0):
    lastdigit = num%10
    num = int(num/10)
    reverseNumber = reverseNumber * 10 + lastdigit

#Checking palindrome or not
if(temp == reverseNumber):
    print("Palindrome")
else:
    print("Not a Palindrome")