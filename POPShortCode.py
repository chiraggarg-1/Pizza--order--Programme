size = input("What size of Pizza do you want to order (S/M/L)")
bill = 0
if size == 'S' or size == 's':
    bill+=100
    print(f"The Price of your Pizza is {bill}")

elif size == 'M' or size == 'm':
    bill+=200
    print(f'The Price of Medium Pizza is {bill}')

else:
    bill+=300
    print(f'The Price of large Pizza is {bill}')

add_Pepperoni = input("Do you want to add Pepperoni in your pizza (Y/N)")
if add_Pepperoni == 'Y'or add_Pepperoni == 'y':
    size_Pepperoni = input("What size of Pepperoni do you want to order (S/M)")
    if size_Pepperoni == 'S' or size_Pepperoni == 's':
     bill+=30
    else:
     bill+=50

add_cheese = input("Do you want to add Extra Cheese (Y/N)")
if add_cheese == 'Y' or add_cheese == 'y':
    bill+=20

print(f'Your total bill of Pizza is {bill}')



