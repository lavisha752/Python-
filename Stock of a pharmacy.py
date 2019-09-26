# creating a list with items
stock=['paracetamol','bandage','antiseptic wipes','cough syrup','antibiotics']
print("Current Stock")
# User input and to choose the option
option = input("1. Add an item to the stock pharmacy.\n\
2. Remove item from stock.\n\
3. Insert item at a specific location.\n\
Please enter an option:")
# check for the statements in different choices
# Adding items
if option=="1":
    item=input("Enter the item you want to add in stock :")
    stock.append(item)
    print(stock)
# Removing items
elif option=="2":
    item = input("Enter the item you want to remove from stock :")
    stock.remove(item)
    print(stock)
# Inserting number at specific index
elif option == "3":
    pos_index = int(input("In which position would you like to add to the stock :"))
    item = input("Enter the item you want to insert in stock :")
 # An if condition to check for the correct position
    if pos_index < len(stock):
      stock.insert(pos_index,item)
      print(stock)
    else:
     print("Invalid Position")
# Message for choosing the wrong choice
else:
    print("Invalid choice")




