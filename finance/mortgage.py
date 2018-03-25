loan = input('Enter Loan Amount: ')
loan = float(loan)

years  = input('Enter Loan payments in years: ')
numberOfPayments = float(years) * 12

interest = input('Annual interest Rate: ')
interest = float(interest)/100/12


#                                                raised to power of 
monthlyPayments = loan * (interest * (1 + interest) ** numberOfPayments) / ((1 + interest) ** numberOfPayments - 1)

print("\n\n")
print("*" * 40)
print("Your payments are: " + str(round(monthlyPayments)) + "a month for " + str(years) + " years")
print("Welcome to being in debt :(")
print("*" * 40)
