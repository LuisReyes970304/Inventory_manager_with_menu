from inventory import add_to_list, show_total, show_products
from validation import name_validator, price_validator, amount_validator
from messages import welcome_message_fun, bye_message_function, menu_function
from validation import name_validator, price_validator, amount_validator
#This is the main file in which run all the functions. 

product_list = []

#Welcome message
welcome_message_fun()

#Start of the loop
active = True
while active:
    menu_function()
    option = input("Please select an option: ").upper()
    if option == "1":
        name = name_validator()
        price = price_validator(name)
        amount = amount_validator(name)
        add_to_list(product_list, name=name, price=price, amount=amount, subtotal=price*amount)
    elif option == "2":
        show_products(product_list)

    elif option == "3":
        show_total(product_list)

    elif option == "4":
        active = False

    elif option not in ["1", "2", "3", "4"]:
        print("Invalid option. Please try again.")
        
#Bye message
bye_message_function()
    


