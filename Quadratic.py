import math

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    tuple: Solutions of the quadratic equation, which can be real or complex.
    """
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

def get_input():
    """
    Gets and validates user input for the quadratic equation coefficients.
    
    Returns:
    tuple: Validated values for coefficients a, b, and c.
    """
    while True:
        try:
            a = float(input("Enter coefficient a (non-zero): "))
            if a == 0:
                print("Coefficient 'a' cannot be zero. Please enter a non-zero value.")
                continue
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            return a, b, c
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def display_solutions(solutions):
    """
    Displays the solutions of the quadratic equation in a user-friendly manner.
    
    Parameters:
    solutions (tuple): The solutions to display.
    """
    if len(solutions) == 1:
        print(f"The solution is: {solutions[0]}")
    elif len(solutions) == 2:
        if isinstance(solutions[0], complex):
            print(f"The solutions are complex: {solutions[0]} and {solutions[1]}")
        else:
            print(f"The real solutions are: {solutions[0]} and {solutions[1]}")

if __name__ == "__main__":
    print("Quadratic equation solver for equations in the form ax^2 + bx + c = 0")
    
    a, b, c = get_input()
    solutions = solve_quadratic(a, b, c)
    display_solutions(solutions)
