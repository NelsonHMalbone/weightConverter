# Conversion for inches to cm
# cm to inches

measure = float(input("Enter a measurement: "))
#uom = unit of measurement
uom = input("Convert Measurement (cm or in): ")

if uom == "cm":
    measure = round(measure * 2.54, 3)
    unit = 'centimeters'
    print(f"measurement is {measure} {unit}")
elif uom == "in":
    measure = round(measure / 2.54, 3)
    unit = 'inches'
    print(f"measurement is {measure} {unit}")
else:
    print(f'{uom} is not vaild')