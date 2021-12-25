def computepay(hours, rate): 
    if (hours > 40):
        return (40 * rate) + ((hours - 40) * 1.5 * rate)
    else:
        return (hours * rate)

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    print(f"Pay: {computepay(hours, rate):,.2f}")
    
except:
    print("Error, please enter a numeric input")