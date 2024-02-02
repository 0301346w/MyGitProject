import math
 
def calculate_area(radius):
    return math.pi * radius ** 2
 
def calculate_circumference(radius):
    return 2 * math.pi * radius
 
def calculate_volume(radius):
    return (4 / 3) * math.pi * radius ** 3
 
def display_results(area, circumference, volume):
    print(f"Area of the circle: {area:.2f}")
    print(f"Circumference of the circle: {circumference:.2f}")
    print(f"Volume of the sphere: {volume:.2f}")
 
def main():
    # Get user input
    radius = float(input("Enter the radius of the circle: "))
 
    # Perform calculations
    area_result = calculate_area(radius)
    circumference_result = calculate_circumference(radius)
    volume_result = calculate_volume(radius)
 
    # Display the results
    display_results(area_result, circumference_result, volume_result)
 
if __name__ == "__main__":
    main()
 
