error = "Please enter a numeric value!"

hours = input("Enter hours: ")
try:
    hours = float(hours)
    rate = input("Enter rate: ")
    try:
        rate = float(rate)
    except:
        rate = -1
except:
    hours = -1

if hours > 0 and rate > 0:
    n = 40.0
    if hours > n:
        above_40 = (hours - n)*rate*1.5
        pay = (n*rate) + above_40
        print("Pay: ", pay)
    elif hours <= n:
        pay = hours*rate
        print("Pay: ", pay)
else:
    print(error)
    