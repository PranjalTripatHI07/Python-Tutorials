'''
D. Discount Calculator:
Write a program that takes the total amount of a purchase and calculates the discount based on the following conditions:
If the total is greater than $100, apply a 10% discount.
If the total is greater than $50, apply a 5% discount.
Otherwise, no discount.

'''

print("\n Welcome to Discount Calculator:-")

total_amount = float(input("\n Enter total amount of the purchase:- "))

if total_amount >= 100:
    discount = 0.10
elif total_amount >= 50:
    discount = 0.05
else:
    discount = 0.00

discount_amount = total_amount * discount
final_amount = total_amount - discount_amount

print(f"\n Discount amount: ${discount_amount}")
print(f"\n Your final amount after discount: ${final_amount}")


