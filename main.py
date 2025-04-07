import importlib
import os

calcs = {
    "basic": "basic",  # Basic equations e.g. Addition, Subtraction, Multiplication, Division
    "graphing": "graphing",  # Graphing equations e.g. y = mx + b
    "trig": "trig",  # Trigonometric equations e.g. sin, cos, tan
    "stats": "stats",  # Statistics equations e.g. mean, median, mode
    "geometry": "geometry",  # Geometry equations e.g. area, perimeter
    "algebra": "algebra",  # Algebra equations e.g. quadratic formula
    "calculus": "calculus",  # Calculus equations e.g. derivative, integral
}

def main():
    prompt_valid = False
    print("QuickMash's PyCalculate\nA python calculator for all your needs\n")
    print("Type Help for list of calculators\n")
    while not prompt_valid:
        prompt = input("> ")
        if prompt.lower() == "help":
            print("Available calculators:")
            for calc in calcs:
                print(f"- {calc}")
            print("\nGeneral Commands:")
            print("- Help: List available calculators\n- Clear: Clear screen\n- Exit: Exit the program")
        elif prompt.lower() == "clear":
            if os.name == 'nt':
                os.system('cls')
            elif os.name == 'posix':
                os.system('clear')
            elif os.name == 'mac':
                os.system('clear')
            elif os.name == 'os2':
                os.system('cls')
            elif os.name == 'ce':
                os.system('cls')
            elif os.name == 'java':
                os.system('clear')
            else:
                try:
                    os.system('clear')  # Fallback for other OS
                except:
                    print("Unable to clear screen for this OS\nFallback Failed!")
        elif prompt.lower() in ["exit", "quit", "bye"]:
            print("Exiting...")
            exit()
        elif prompt.lower() in calcs:
            print(f"Loading {prompt.capitalize()} calculator...")
            module_name = calcs[prompt.lower()]
            module = importlib.import_module(module_name)
            module.main()
            prompt_valid = True
        else:
            print("Invalid input. Type 'Help' for list of calculators.")

if __name__ == "__main__":
    main()