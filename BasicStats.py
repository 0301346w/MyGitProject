def find_sum(numbers):
    return sum(numbers)
 

 
def display_results(sum_result):
    print(f"Sum of the numbers: {sum_result}")

 
def main():
    # Get user input for a list of numbers
    numbers_str = input("Enter a list of numbers separated by spaces: ")
    user_numbers = [float(num) for num in numbers_str.split()]
 
    # Perform list operations
    sum_result = find_sum(user_numbers)

 
    # Display the results
    display_results(sum_result)
 
if __name__ == "__main__":
    main()