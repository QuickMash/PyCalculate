from sympy import sympify, sqrt

def evaluate_expression(eq):
    try:
        result = sympify(eq).evalf()
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Geometry Calculator")
    print("Type 'exit' to quit")
    print("Use 'help' for list of commands")
    while True:
        eq = input("> ")
        if eq.lower() in ["exit", "quit"]:
            break
        elif eq.lower() == "help":
            print("Available commands: area, perimeter, volume, pythagorean")
            print("Use '[command] help' for more information on a specific command")
        elif eq.lower() == "area help":
            print("Calculates the area of a rectangle, circle, or triangle.")
            print("Usage: area, area circle, area triangle")
        elif eq.lower() == "perimeter help":
            print("Calculates the perimeter of a rectangle, circle, or triangle.")
            print("Usage: perimeter, perimeter circle, perimeter triangle")
        elif eq.lower() == "volume help":
            print("Calculates the volume of a rectangular prism, sphere, cone, or cylinder.")
            print("Usage: volume, volume sphere, volume cone, volume cylinder")
        elif eq.lower() == "pythagorean help":
            print("Solves for the hypotenuse or a leg of a right triangle using the Pythagorean theorem.")
            print("Usage: pythagorean")
        elif eq.lower() == "area":
            width = input("Width > ")
            height = input("Height > ")
            result = evaluate_expression(f"{width} * {height}")
            print(f"Area: {result}")
        elif eq.lower() == "area circle":
            radius = input("Radius > ")
            result = evaluate_expression(f"pi * {radius}**2")
            print(f"Area of Circle: {result}")
        elif eq.lower() == "area triangle":
            base = input("Base > ")
            height = input("Height > ")
            result = evaluate_expression(f"0.5 * {base} * {height}")
            print(f"Area of Triangle: {result}")
        elif eq.lower() == "perimeter":
            width = input("Width > ")
            height = input("Height > ")
            result = evaluate_expression(f"2 * ({width} + {height})")
            print(f"Perimeter: {result}")
        elif eq.lower() == "perimeter circle":
            radius = input("Radius > ")
            result = evaluate_expression(f"2 * pi * {radius}")
            print(f"Perimeter of Circle: {result}")
        elif eq.lower() == "perimeter triangle":
            side1 = input("Side 1 > ")
            side2 = input("Side 2 > ")
            side3 = input("Side 3 > ")
            result = evaluate_expression(f"{side1} + {side2} + {side3}")
            print(f"Perimeter of Triangle: {result}")
        elif eq.lower() == "volume":
            width = input("Width > ")
            height = input("Height > ")
            depth = input("Depth > ")
            result = evaluate_expression(f"{width} * {height} * {depth}")
            print(f"Volume: {result}")
        elif eq.lower() == "volume sphere":
            radius = input("Radius > ")
            result = evaluate_expression(f"(4/3) * pi * {radius}**3")
            print(f"Volume of Sphere: {result}")
        elif eq.lower() == "volume cone":
            radius = input("Radius > ")
            height = input("Height > ")
            result = evaluate_expression(f"(1/3) * pi * {radius}**2 * {height}")
            print(f"Volume of Cone: {result}")
        elif eq.lower() == "volume cylinder":
            radius = input("Radius > ")
            height = input("Height > ")
            result = evaluate_expression(f"pi * {radius}**2 * {height}")
            print(f"Volume of Cylinder: {result}")
        elif eq.lower() == "pythagorean":
            print("Choose what to solve for: hypotenuse, leg")
            choice = input("> ")
            if choice.lower() == "hypotenuse":
                leg1 = input("Leg 1 > ")
                leg2 = input("Leg 2 > ")
                result = evaluate_expression(f"sqrt({leg1}**2 + {leg2}**2)")
                print(f"Hypotenuse: {result}")
            elif choice.lower() == "leg":
                hypotenuse = input("Hypotenuse > ")
                leg = input("Known Leg > ")
                result = evaluate_expression(f"sqrt({hypotenuse}**2 - {leg}**2)")
                print(f"Unknown Leg: {result}")
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()