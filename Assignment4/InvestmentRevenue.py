# Input Validation Loops using the walrus operator
while (monthly_investment := float(input("Enter a monthly investment amount: "))) <= 0:
    print("Error: investment must be a positive number")

while (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) <= 0:
    print("Error: yearly interest rate must be a positive number")

while (investment_years := int(input("Enter how many years to invest: "))) <= 0:
    print("Error: investment period must be a positive number of years")

# Convert yearly rate to monthly rate (as a decimal)
monthly_rate = (yearly_interest_rate / 100) / 12

# Initialize total revenue
total_revenue = 0.0

# Calculate total months
total_months = investment_years * 12

# Process: Compound investment revenue calculation month by month
for month in range(1, total_months + 1):
    # Add the monthly investment to the current total
    total_revenue += monthly_investment
    # Apply the monthly interest to the total
    total_revenue *= (1 + monthly_rate)
    
    # Output: Print the monthly revenue
    print(f"Month {month} revenue: {total_revenue}")

# Output: Print the final total investment revenue using an F-string
# Note: Using :,.2f to format with commas and 2 decimal places like the sample
print(f"After {investment_years} years, you will receive a total investment revenue of {total_revenue:,.2f} at a yearly rate of {yearly_interest_rate}")