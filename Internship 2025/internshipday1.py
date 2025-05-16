num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))

ans = num1 + num2
print(f"addition is:- {ans}")


#simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter time period (years): "))


simple_interest = (principal * rate * time) / 100


print(f"\nPrincipal Amount: ${principal:,.2f}")
print(f"Interest Rate: {rate}%")
print(f"Time Period: {time} years")
print(f"Simple Interest: ${simple_interest:,.2f}")
print(f"Total Amount: ${(principal + simple_interest):,.2f}")