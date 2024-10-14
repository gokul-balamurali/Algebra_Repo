import math

def solve_quadratic(a, b, c):
    """Solves a second-order polynomial equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        print("No real solutions, but there are complex solutions.")
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))
    elif discriminant == 0:
        # One real solution (double root)
        x = -b / (2 * a)
        return (x,)
    else:
        # Two real solutions
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

# Example usage
if __name__ == "__main__":
    print("Quadratic equation solver for equations in the form ax^2 + bx + c = 0")
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    solutions = solve_quadratic(a, b, c)
    print("The solutions are:", solutions)
