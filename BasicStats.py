def find_sum(numbers):
    return sum(numbers)
 
def find_average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return "List is empty, cannot calculate average."
 
def find_max(numbers):
    if numbers:
        return max(numbers)
    else:
        return "List is empty."
 
def display_results(sum_result, average_result, max_result):
    print(f"Sum of the numbers: {sum_result}")
    print(f"Average of the numbers: {average_result}")
    print(f"Maximum number in the list: {max_result}")
 
def main():
    # Get user input for a list of numbers
    numbers_str = input("Enter a list of numbers separated by spaces: ")
    user_numbers = [float(num) for num in numbers_str.split()]
 
    # Perform list operations
    sum_result = find_sum(user_numbers)
    average_result = find_average(user_numbers)
    max_result = find_max(user_numbers)
 
    # Display the results
    display_results(sum_result, average_result, max_result)
 
if __name__ == "__main__":
    main()
