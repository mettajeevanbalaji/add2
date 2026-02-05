purchase_amount = float(input("Enter the total purchase amount: $"))

# Apply discount based on conditions
if purchase_amount > 100:
    discount = 0.10  # 10% discount
elif purchase_amount > 50:
    discount = 0.05  # 5% discount
else:
    discount = 0.0   # No discount

# Calculate final amount
final_amount = purchase_amount - (purchase_amount * discount)

# Display the result
print(f"Original amount: ${purchase_amount:.2f}")
print(f"Discount applied: {discount*100:.0f}%")
print(f"Final amount after discount: ${final_amount:.2f}")
