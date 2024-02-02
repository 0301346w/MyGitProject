import math
 
def calculate_area(radius):
    return math.pi * radius ** 2
 

 
def display_results(area, circumference, volume):
    print(f"Area of the circle: {area:.2f}")

 
def main():
    # Get user input
    radius = float(input("Enter the radius of the circle: "))
 
    # Perform calculations
    area_result = calculate_area(radius)

 
    # Display the results
    display_results(area_result)
 
if __name__ == "__main__":
    main()