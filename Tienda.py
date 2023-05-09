import sys

# Create a dictionary to store the items in the store.
items = {
    "Memoria Ram ": 750.00,
    "CPU Ryzen 7 3500": 0.50,
    "RTX 4080": 12500.05
}

# Create a function to add an item to the store.
def add_item(item, price):
    items[item] = price

# Create a function to remove an item from the store.
def remove_item(item):
    del items[item]

# Create a function to get the price of an item.
def get_price(item):
    return items[item]

# Create a function to print the list of items in the store.
def print_items():
    for item in items:
        print(item, items[item])

# Create a function to get the user's input.
def get_input():
    return input("Que deseas hacer? ")

# Create a main loop that keeps running until the user wants to quit.
while True:
    # Print the list of items.
    print("Lista de productos")
    print_items()

    # Get the user's input.
    command = get_input()

    # If the user wants to add an item, call the add_item function.
    if command == "agregar":
        item = input("Producto a agregar")
        price = input("Precio del Producto")
        add_item(item, float(price))

    # If the user wants to remove an item, call the remove_item function.
    elif command == "borrar":
        item = input("Articulo a remover ")
        remove_item(item)

    # If the user wants to get the price of an item, call the get_price function.
    elif command == "precio":
        item = input("Deseas saber el costo de algun articulo, ponlo aqui")
        print(get_price(item))

    # If the user wants to checkout, calculate the total price and print it.
    elif command == "cobro":
        total_price = 0
        for item in items:
            quantity = float(input("Numero de " + item + "a comprar"))
            total_price += quantity * float(items[item])
        print("El total de tu cuenta es: ", total_price)
        print("Proceder al pago? (Si/No)")
        proceed = input()
        if proceed == "Si":
            print("Gracias por su compra vuelva pronto")
            break
        else:
            print("Orden Cancelada")

    # If the user wants to quit, break out of the loop.
    elif command == "quit":
        break

