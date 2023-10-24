import math

def solve_equation(*args):
    if len(args) == 3:
        a, b, c = args
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return [x1, x2]
        elif discriminant == 0:
            x1 = -b / (2*a)
            return [x1]
        else:
            return ["*"]
    elif len(args) == 2:
        b, c = args
        if b == 0:
            if c == 0:
                return ["*"]
            else:
                return []
        else:
            x = -c / b
            return [x]
    elif len(args) == 1:
        c = args[0]
        if c == 0:
            return ["*"]
        else:
            return []

    return None

print(solve_equation(1, -3, 2))  # Две действительные корни
print(solve_equation(1, -2, 1))  # Один действительный корень
print(solve_equation(1, 2, 1))   # Один действительный корень
print(solve_equation(0, 2))      # Один действительный корень
print(solve_equation(0))         # Один действительный корень
print(solve_equation(1, 0, 1))   # Нет действительных корней
print(solve_equation(1, 1, 1))   # Нет действительных корней