x = input("Enter Hours: ")
y = input("Enter Rate: ")

try:
    x = int(x)
    y = int(y)
except:
    x = -1
    y = 1
print("Pay: ",x*y)
