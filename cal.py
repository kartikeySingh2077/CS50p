# user input
x = float(input("What's x? "))
y = float(input("What's y? "))
f = input("What do you want to do (plus, minus, multiply, divide)? ")

# perform calculation
if f == ("plus"):
    z = (x + y)

elif f == ("minus"):
    z = (x - y)
elif f == ("multiply"):
    z = (x*y)
elif f == ("divide"):
    if y != 0:
        z = (x / y)
else:
    z = "Error: Division by zero!"
else:
if x > 0:
z = "Invalid operation!"
print(z)
