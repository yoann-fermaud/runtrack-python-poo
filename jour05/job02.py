def power(x, n):
    if n > 0:
        return x * power(x, n - 1)
    else:
        return 1


integer = int(input("Enter an integer: "))
integer_power = int(input("Enter a power: "))

print("Result:", power(integer, integer_power))
