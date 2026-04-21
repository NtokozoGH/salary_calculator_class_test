# ---------------------------------------------------------
# PYTHON CHALLENGE: THE NET SALARY CALCULATOR (SARS 2026/27)
# ---------------------------------------------------------

# QUESTION 1: 
# Create three variables to get user input (floats):
# - monthly_gross_salary
monthly_gross_salary=float(input("insert your gross salary:R"))
# - medical_aid_premium
medical_aid_premium=float(input("what is your medical aid premium:R"))
# - num_dependents (for medical credits)
num_dependents=float(input("how many dependants are on your medical aid?:"))

# QUESTION 2:
# Calculate the monthly UIF contribution. 
# Remember: It is 1% of gross salary, but it is capped at R177.12.
# Hint: Use an 'if' statement or the min() function.
uif= monthly_gross_salary*0.01
if uif > 177.12:
        uif=177.12
print("unemployment insurance fund:",uif)
# QUESTION 3:
# To calculate tax (PAYE), we need the annual salary.
# Create a variable 'annual_gross' by multiplying monthly salary by 12.
annual_gross= monthly_gross_salary*12
paye=annual_gross*0.18
print("Pay as you earn:",paye)

# QUESTION 4:
# Using the 2026/27 Tax Brackets, create an if/elif/else structure
# to calculate the 'base_tax' on the 'annual_gross'.
# Example: 
# If income <= 245100, tax is 18%.
# If income > 245100 and <= 383100, tax is 44118 + 26% of amount above 245100.
if annual_gross<= 245100:
        base_tax=annual_gross*0.18
elif annual_gross > 245100 and annual_gross <= 383100:
        base_tax= 44118 + (annual_gross-245100)*0.26
elif annual_gross > 383100 and annual_gross <= 530200:
        base_tax= 79998 + (annual_gross-383100)*0.31
elif annual_gross > 530200 and annual_gross <= 695800:
        base_tax= 125599 + (annual_gross-530200)*0.36
elif annual_gross > 695800 and annual_gross <= 887000:
        base_tax= 185215 + (annual_gross-887000)*0.39
elif annual_gross > 887000 and annual_gross <= 1878600:
        base_tax= 259783 + (annual_gross-1878600)*0.41
else: base_tax= 666339 + (annual_gross-1878600)*0.45

print("base tax:",base_tax)
        


# QUESTION 5:
# Everyone gets a Primary Rebate of R17,820 per year.
# Subtract this rebate from your 'base_tax'. 
# Note: Tax cannot be less than zero!
primary_rebate=17820
rebate=(base_tax-primary_rebate)
print("primary rebate:", rebate)

# QUESTION 6:
# Medical Tax Credits (MTC) reduce your tax.
# For 2026, the main member gets R376 off per month.
# Calculate the 'monthly_tax' by dividing annual tax by 12, 
# then subtract the R376 credit.
mtc_dis= 376
monthly_tax=(base_tax/ 12)-mtc_dis
print("med aid disc:",monthly_tax)



# QUESTION 7:
# Final Step! Calculate the 'net_salary'.
# Formula: Gross - Monthly Tax - UIF - Medical Aid Premium.
net_salary= monthly_gross_salary-monthly_tax-uif-medical_aid_premium
print("net salary:", net_salary)
# QUESTION 8:
# Print a professional payslip showing:
# Gross Salary, UIF Deduction, Tax Paid, and the final Net Salary.
monthlytax=paye/12
print("----------Payslip----------")
print("monthly gross:",monthly_gross_salary)
print("uif deductions:", uif)
print("pay as you earn:",monthlytax)
print("med aid contribution:",medical_aid_premium)
print("--------------------")
#print("net salary:",f{net_salary:.2f})
#price = 19.999
#print(f"{price:.2f}")
#print(f"net salary: R{net_salary:.3f}")
#value = net_salary
#formatted_value = "{:.2f}".format(value)
#print("net salary:",formatted_value)
number = net_salary
#print("net salary:r%.2f" % number)
print(f" net salary: R {number:.0f}")