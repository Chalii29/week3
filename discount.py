def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Test the function
original_price = 50000
discount_percentage = 25  # 25% discount
final_price = calculate_discount(original_price, discount_percentage)
print("Final Price after applying a discount:", final_price)

# Get user input for the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price after applying the discount
if final_price < original_price:
    print("Final Price after applying a discount: ${:.2f}".format(final_price))
else:
    print("No discount applied. Original Price: ${:.2f}".format(original_price))