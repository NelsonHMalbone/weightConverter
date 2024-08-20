# Date 08/24/2024
# BroCode Python Weight Converter Basic Converter

#follow up from the simple arithmetic calc for using if statements
#ibs to kg and kg to ibs

# creating a variable
# will be a float for useage of decimals and whole numbers
weight = float(input("Enter Your Weight: "))

# asking if unit is pounds or kg
# k = kilograms
# L = Pounds
unit = input("Kilograms or Pounds? (K or L): ")

# chekcing to see if unit is pound or kilogram
# reassigning units for either kgs or lbs
# placing print(f"Your weight is {weight} {unit}") inside of each if statesment to not get pass results with
# invaildated output
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {weight} {unit}")
elif unit == "L":
    weight = round(weight / 2.205, 3)
    unit = "Kgs."
    print(f"Your weight is {weight} {unit}")
else:
    print(f"{unit} was not vaild")

