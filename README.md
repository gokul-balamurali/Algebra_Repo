# Quadratic Equation Solver

This is a Python-based quadratic equation solver. It solves second-order polynomial equations of the form:

## How it Works

The program takes three coefficients `a`, `b`, and `c` as inputs, representing the quadratic equation `ax^2 + bx + c = 0`. It then uses the **quadratic formula** to find the roots of the equation. The formula is:


### Types of Solutions:
- If the **discriminant** (`b^2 - 4ac`) is **positive**, the program returns two real solutions.
- If the **discriminant** is **zero**, the program returns one real solution (a repeated root).
- If the **discriminant** is **negative**, the program returns two complex solutions.

## Usage

1. Clone this repository:

2. Navigate to the repository:

3. Run the solver:

4. Enter the coefficients `a`, `b`, and `c` when prompted.

### Example:

Enter coefficient a: 1 Enter coefficient b: -3 Enter coefficient c: 2 The solutions are: (2.0, 1.0)


### Complex Solutions Example:

Enter coefficient a: 1 Enter coefficient b: 2 Enter coefficient c: 5 The solutions are: ((-1+2j), (-1-2j))


## Requirements

- Python 3.x
- Math module (comes pre-installed with Python)

## Contributing

Feel free to open issues or submit pull requests if you'd like to improve the solver or add new features!
