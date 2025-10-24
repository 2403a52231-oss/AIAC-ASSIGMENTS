def calculate_power_bill():
    """
    Prompts the user to enter items and their prices, calculates GST for each,
    and displays the price of each item with GST as well as the total bill.
    """
    try:
        num_items = int(input("Enter the number of items in your bill: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    items = []
    GST_RATE = 0.18  # 18% GST

    for i in range(num_items):
        name = input(f"Enter the name of item {i+1}: ")
        try:
            price = float(input(f"Enter the price of {name}: "))
        except ValueError:
            print("Invalid price. Please enter a number.")
            return
        price_with_gst = price * (1 + GST_RATE)
        items.append((name, price, price_with_gst))

    print("\n--- Bill Details ---")
    total = 0
    for name, price, price_with_gst in items:
        print(f"{name}: Original Price = ₹{price:.2f}, Price with GST = ₹{price_with_gst:.2f}")
        total += price_with_gst
    print(f"\nTotal Bill (including GST): ₹{total:.2f}")

# Example usage:
calculate_power_bill()
