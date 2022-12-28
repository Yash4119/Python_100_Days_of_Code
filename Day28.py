# F-Strings in Python

# old python string formatting
letter = "Hey my name is {1} and I am from {0}"

name = "Yash"
country = "India"
salary = 23.2

print(letter.format(name,country))
print(letter.format(country,name))

# New Python String formatting technique
# Using f string in Python
# Newly introduced from Python 3.6 onwards

letter = f"Hey, my name is {name} and I am from {country}. I have a salary of {salary:.2f}LPA"

print(letter)
print(f"{2*45.4356:.3f}")

# If we want to print our curly brackets as it is we can print as follows

name = "Yash Jayram Ambekar"

print(f"{name}")
print(f"{{name}}")