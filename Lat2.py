def collect_customer_info():
    print("\n=== Customer Information ===")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    return name, age, address

def gather_purchase_details():
    print("\n--- Purchase Details ---")
    item_name = input("Enter the item you want to buy: ")
    price_per_item = float(input(f"Enter the price of '{item_name}': $"))
    quantity = int(input(f"Enter the quantity of '{item_name}': "))
    return item_name, price_per_item, quantity

def calculate_financials(price_per_item, quantity):
    subtotal = price_per_item * quantity
    discount = subtotal * 0.10
    grand_total = subtotal - discount
    return subtotal, discount, grand_total

def generate_sales_receipt(name, age, address, item_name, price_per_item, quantity, subtotal, discount, grand_total):
    print("\n===== Sales Receipt =====")
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Address : {address}")
    print("\nPurchase Details:")
    print(f"Item Name : {item_name}")
    print(f"Price : ${price_per_item:.2f}")
    print(f"Quantity : {quantity}")
    print(f"Subtotal : ${subtotal:.2f}")
    print(f"Discount : -${discount:.2f} (10%)")
    print(f"Grand Total: ${grand_total:.2f}")
    print("=========================")
    print("Thank you for your purchase!")
    print("~ Happy Exercising ~")

def main():
    name, age, address = collect_customer_info()
    item_name, price_per_item, quantity = gather_purchase_details()
    subtotal, discount, grand_total = calculate_financials(price_per_item, quantity)
    generate_sales_receipt(name, age, address, item_name, price_per_item, quantity, subtotal, discount, grand_total)

if __name__ == "__main__":
    main()

