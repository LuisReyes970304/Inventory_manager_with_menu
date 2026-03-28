from time import sleep


def add_to_list(product_list: list, **product_object: dict):
    return product_list.append(product_object)
#This function shows the products in the list with a little animation to make it more fun.


def show_products(product_list):
    for product in product_list:
        output = f"""
Product name: ...............: {product["name"]}
Product price: ..............: {product["price"]}
Product cuantity: ...........: {product["amount"]}
Product subtotal: ...........: {product["subtotal"]}
.............................................................
"""
        for i in output:
            print(i, end="", flush=True)
            sleep(0.01)
#This function shows the total earnings and the total amount of products in the list with a little animation to make it more fun.


def show_total(product_list):
    total = sum(product["subtotal"] for product in product_list)
    for i in f"\nTotal earnings: {total}\n":
        print(i, end="", flush=True)
        sleep(0.01)
    total_products = sum(product["amount"] for product in product_list)
    for i in f"Total products: {total_products}\n":
        print(i, end="", flush=True)
        sleep(0.01)
#This function shows the menu of the program with a little animation to make it more fun.
        
