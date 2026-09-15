"""
Program 9: Nest dictionaries - inventory of products with price and stock
Concept: Dictionaries: Dictionaries (nesting, access, update)
"""

def manage_product_inventory():
    """Manage a product inventory using nested dictionaries."""
    # Create inventory with nested dictionaries
    inventory = {
        "Laptop": {
            "price": 999.99,
            "stock": 15,
            "category": "Electronics"
        },
        "Mouse": {
            "price": 25.50,
            "stock": 50,
            "category": "Electronics"
        },
        "Keyboard": {
            "price": 75.00,
            "stock": 30,
            "category": "Electronics"
        },
        "Notebook": {
            "price": 8.99,
            "stock": 100,
            "category": "Stationery"
        }
    }
    
    print("Initial Inventory:")
    print("=" * 50)
    for product, details in inventory.items():
        print(f"{product}:")
        print(f"  Price: ${details['price']:.2f}")
        print(f"  Stock: {details['stock']} units")
        print(f"  Category: {details['category']}")
        print()
    
    # Access specific product information
    print("Accessing specific product info:")
    product_name = "Laptop"
    if product_name in inventory:
        price = inventory[product_name]["price"]
        stock = inventory[product_name]["stock"]
        print(f"{product_name}: ${price:.2f}, {stock} in stock")
    print()
    
    # Update stock after a sale
    print("Updating stock after selling 3 laptops...")
    if "Laptop" in inventory:
        inventory["Laptop"]["stock"] -= 3
        print(f"Laptop stock updated: {inventory['Laptop']['stock']} units remaining")
    print()
    
    # Add a new product
    print("Adding new product: Monitor")
    inventory["Monitor"] = {
        "price": 199.99,
        "stock": 25,
        "category": "Electronics"
    }
    print("Monitor added to inventory")
    print()
    
    # Show final inventory
    print("Final Inventory:")
    print("=" * 50)
    for product, details in inventory.items():
        print(f"{product}: ${details['price']:.2f} ({details['stock']} in stock)")

if __name__ == "__main__":
    manage_product_inventory()