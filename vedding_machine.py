class OutOfSTock(Exception):
    """Nope"""
    pass

class WrongCode(Exception):
    "wrong code"
    pass

def SelectedPodycts(product):
    try:
        product_id = int(input("Enter product ID: "))
        if product_id not in product:
            raise WrongCode("Nah man wrong code")
        if product[product_id] == "0":
             raise OutOfSTock("Nema qdene, begai")
        return product_id
    except ValueError:
        print("Invalid input! Please enter a number.")
        return select_product(products)
    except InvalidInputError as e:
        print("meow, meow error", e)
        return select_product(products)
    except OutOfStockError as e:
        print(e)
        return select_product(products)

def VendingMachine():
    products = {
        1: {'name': 'Coke', 'price': 1.5, 'quantity': 5},
        2: {'name': 'Chips', 'price': 2.0, 'quantity': 0},
        3: {'name': 'Water', 'price': 1.0, 'quantity': 10}
    }


try:
    print("Available products:")
    for pid, details in products.items():
        print(f"ID: {pid}, Name: {details['name']}, Price: ${details['price']}, Quantity: {details['quantity']}")

    product_id = select_product(products)
    print(f"You selected {products[product_id]['name']} costing ${products[product_id]['price']}")

    payment = float(input("Enter payment amount: "))
    if payment < products[product_id]['price']:
        raise InvalidInputError("Insufficient funds.")

    # Update quantity
    products[product_id]['quantity'] -= 1
    change = payment - products[product_id]['price']
    print(f"Thank you! Your change is ${change:.2f}")

except InvalidInputError as e:
    print(e)
except ValueError:
    print("Please enter a valid payment amount.")
finally:
    print("Thank you for using the vending machine!")

vending_machine()
