import math

# write code to allow a user to access two different financial calculators:
# 1. an investment calculator
# 2. a home loan repayment calculator

print('''investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan''')

finance_calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
finance_calculator = finance_calculator.lower()
# ensure that the answer is not case sensitive
# ensure that if anything else is typed, an error message will appear to the user

# investment calculator
if (finance_calculator == "investment"): 
    print("You have chosen the investment calculator.")

    finance_calculator = "investment_calculator"
    deposit_amount = int(input("What is the total amount of money you are depositing? "))
    interest_rate = int(input("What is the interest rate? Please write the number without adding '%'. "))
    r = interest_rate / 100 # making sure the interest rate is added into the formula correctly
    investment_years = int(input("How many years do you plan to invest for? "))
    interest = (input("Do you want simple or compound interest? "))

    # simple interest calculator
    if interest == "simple":
        simple_interest = int(deposit_amount *(1 + r * investment_years))

        # making the result round to the nearest 2 decimals
        simple_interest = round(simple_interest,2)
        print("You will have £" + str(simple_interest) + " in total.")

    # compound interest calculator
    elif interest == "compound":
        compound_interest = (deposit_amount * math.pow((1 + r), investment_years))

        # making the result round to the nearest 2 decimals
        compound_interest = round(compound_interest,2)
        print("You will have £" + str(compound_interest) + " in total.")

    # error message
    else:
        print("Please try again and enter a valid answer. Please go back to the start.")

# bond calculator
elif (finance_calculator == "bond"): 
    print("You have chosen the bond calculator")

    finance_calculator = "bond_calculator"
    house_value = int(input("What is the current value of the house? "))
    interest_rate = int(input("What is the interest rate? Please write the number without adding '%'. "))
    i = (interest_rate / 100) / 12 # making sure the interest rate is added into the formula correctly
    months_to_repay = int(input("How many months do you plan to repay the bond in? "))

    # building the bond calculator formula from the variables above:
    monthly_repayment = ((i * house_value)/(1 - (1 + i)**(- months_to_repay)))

    # making the result round to the nearest 2 decimals
    monthly_repayment = round(monthly_repayment,2)
    print("You will have to pay £" + str(monthly_repayment) + " over " + str(months_to_repay) + " months.")

# error message
else:
    print("You have not selected either of the calculators being offered. Please go back to the start.")