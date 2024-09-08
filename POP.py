Pizza_size = input("What's the size of pizza you want to order \n SMALL PIZZA (SP) \n MEDIUM PIZZA (MP) \n LARGE PIZZA (LP)")
if Pizza_size == 'SP' or Pizza_size == 'sp':
    Price = 100
    print(f"Price of your large Pizza is {Price}Rs")
    Pepperoni = input("Do You want Pepperoni (Y/N)")
    if Pepperoni == 'Y' or Pepperoni == 'y':
        Price = Price +30
        print("The Price of Pepperoni is Rs 30")
        print(f"The Price of Your Pizza is {Price}")
    Extra_Cheese = input("Do you want Extra Cheese (Y/N)")
    if Extra_Cheese == 'Y' or Extra_Cheese == 'y':
        Price = Price + 20
        print("The price of Extra Cheese is Rs 20")
        print(f"The price of Pizza is {Price}")
elif Pizza_size == 'MP' or Pizza_size == 'mp':
    Price = 200
    print(f"Price of your large Pizza is {Price}Rs")
    Pepperoni = input("Do You want Pepperoni (Y/N)")
    if Pepperoni == 'Y' or Pepperoni == 'y':
        Price = Price + 50
        print("The price of pepperoni is Rs 50")
        print(f"The price of Pizza is {Price}")
    Extra_Cheese = input("Do you want Extra Cheese (Y/N)")
    if Extra_Cheese == 'Y' or  Extra_Cheese == 'y':
       Price = Price + 20
       print("The price of Extra Cheese is Rs 20")
       print(f"The price of Pizza is {Price}")
else:
    Price = 300
    print(f"Price of your Pizza is {Price}Rs")
    Pepperoni = input("Do You want Pepperoni (Y/N)")
    if Pepperoni == 'Y' or Pepperoni ==  'y':
        Price = Price + 50
        print("The price of pepperoni is Rs 50")
        print(f"The price of Pizza is {Price}")
    Extra_Cheese = input("Do you want Extra Cheese (Y/N)")
    if Extra_Cheese == 'Y' or Extra_Cheese == 'y':
        Price = Price + 20
        print(f"The price of Extra Cheese is Rs 20")
        print(f"The price of Pizza is {Price}")



print(f"Total Price of Your Pizza is {Price}")