# def function
def HCF(a, b):
    # choosing  the smaller number  and check if the condition is true
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        #checkiing if the number is divisible and if there is  remainder
        if ((a % i == 0) and (b % i == 0)):
            hcf = i
# ending the function
    return hcf

# user input
var1 = int(input("Enter a first digit number: "))
var2 = int(input("Enter a second digit number: "))

print ("HCF is = " ,HCF (var1, var2))