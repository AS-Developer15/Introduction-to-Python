# Var decleration
age = int(input("Type your age : "))
grades = int(input("Type your percentage : "))

# Worst Code Ever
if age >= 18 and grades >= 50:
    print("You are qualified ")
elif age >= 18 or grades >= 50:
    print("You are qualified ")
elif not age >= 18:
    print("You are not qualified")
