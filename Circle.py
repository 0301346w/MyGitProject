import math
 
def calculate_area(radius):
    return math.pi * radius ** 2
 
def calculate_circumference(radius):
    return 2 * math.pi * radius
 
 
 
def display_results(area, circumference, volume):
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")
 
def main():
    # Get user input
    radius = float(input("Enter the radius of the circle: "))
 
    # Perform calculations
    area_result = calculate_area(radius)
    volume_result = calculate_volume(radius)
 
    # Display the results
    display_results(area_result, volume_result)
 
if __name__ == "__main__":
    main()
