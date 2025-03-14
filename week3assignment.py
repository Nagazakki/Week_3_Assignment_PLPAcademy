price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage:"))
discounted_price = price * (1 - discount_percentage / 100)

def calculate_discount(price,discount_percentage):
    if discount_percentage >= 20:
        return price * (1 - discount_percentage / 100)
    else:
        return price

if discount_percentage >= 20:
    print(f"You are eligible for a discount.")
    print(f"Your discounted price is $",discounted_price,".")
else:
    print("You are not eligible for a discount.")
    print("Your price is still $",price,".")

