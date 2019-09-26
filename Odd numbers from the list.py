# Creating empty lists where list_3 will contain the odd numbers and even numbers
list_1 = []
list_2 = []
list_3 = []

# user to input in  list_1
var1= int(input("Please enter how many value you want in the list 1: "))

# range used from index 0
for i in range(1,var1+1):
    # value from user'input  and sum  it to the list while input for the values
    list_1.append(input("Please enter the value " + str(i) + ": "))

# user input in list_2
var2= int(input("Please enter how many value you want in the list 2: "))

# range used from index 0
for x in range(1, var2 + 1):
    # value from user's input  and sum  it to the list while input for the values
    list_2.append(input("Please enter value " + str(x) + ": "))

# each number is read and divides by two to check for odd number
for i in list_1:
    if (int(i) % 2) == 1:
        # if number when divided by 2 gives a decimal value, it is added to list_3
        list_3.append(i)

# each number is read and divides by two to check if it is even number
for i in list_2:
    if (int(i) % 2) != 1:
        # if number when divided by 2 gives remainder, it is added to list_3
        list_3.append(i)

print("Odd number from list_1 and even number from list_2: ",list_3)