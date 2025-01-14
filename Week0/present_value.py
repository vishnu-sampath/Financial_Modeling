# Input the Future Cash Flow, Discount Rate, and Number of Periods
future_cash_flow = float(input("Enter the Future Cash Flow (FCF): "))
discount_rate = float(input("Enter the Discount Rate (as a decimal, e.g., 0.05 for 5%): "))
number_of_periods = int(input("Enter the Number of Periods (n): "))

# Calculate Present Value
present_value = future_cash_flow / ((1 + discount_rate) ** number_of_periods)

# Output the result
print(f"The Present Value (PV) of the Future Cash Flow is: ${present_value:.2f}")
