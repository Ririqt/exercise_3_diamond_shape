# Creating Function of the Diamond Shape
def print_diamond(n):
    # Condition for the Odd Integer
    if n % 2 == 0:
        return "Please Provide an odd integer."
    # Creating the Upper Part of the Diamond
    for i in range(n // 2 + 1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
    # Creating the Lower Part of the Diamond
    for i in range(n // 2 - 1, -1, -1):
        print(" " * (n // 2 - i) + "*" * (2 * i + 1))
# Calling the Function
print_diamond(5)     
