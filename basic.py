from sympy import sympify

def evaluate_expression(eq):
    try:
        result = sympify(eq).evalf()
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Basic Calculator")
    print("Type 'exit' to quit")
    while True:
        eq = input("Enter expression: ")
        if eq.lower() in ["exit", "quit"]:
            break
        result = evaluate_expression(eq)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()