home = float(input("Enter the value of the house:"))
salary = float(input("Enter your salary: "))
years = int(input("Enter the numbers of years:"))
print(f"To pay a house of {home} in {years} years")
prest= home/(years*12)
print(f"The loan will be {prest}")
if prest <= (salary*0.3):
    print("Loan approved!")
else:
    print("Loan denied!")
