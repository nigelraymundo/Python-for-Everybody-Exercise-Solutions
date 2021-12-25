hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if (hours > 40):
    pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
else:
    pay = (hours * rate)

print(f"Pay: {pay:,.2f}")