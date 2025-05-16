print("Welcome to simple interest calculator")

principal_amount = int(input("\t\n Enter Principal amount"))

rate_of_interest = int(input("\t\n Enter rate of interest"))

time_period = int(input("\t\n Enter time period"))

Calculate_si = (principal_amount * rate_of_interest * time_period) / 100

print(f"\t\n Your simple interest is {Calculate_si}")