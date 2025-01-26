def greet(name):
    print(f"Hello, {name}!")

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius

name = input("Enter your name: ")
greet(name)

radius = float(input("Enter radius: "))
print(f"Area: {calculate_area(radius)}")
