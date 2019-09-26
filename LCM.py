# User input and storing data in variables
var1=int(input("Enter the first number:"))
var2=int(input("Enter the second number:"))
# Using an if statement to find the smallest number and storing in a variable called smallest
if(var1 > var2):
   smallest=var1

else:
    smallest=var2
# A while loop is used to test if the condition is true and the loop continues while the condition is true else it breaks
while(1):
# An if statement is used to check the smallest number and
# if it is divisible by the two digit and check for remainder when smallest divide by var2
    if(smallest % var1 ==0 and smallest % var2 ==0):
#while the condition is true , the output is displayed
        print("LCM is:",smallest)
# If the value is divisible , it breaks and moves out of the loop
        break
# Else there is an increment to continue the loop
    smallest=smallest+1




