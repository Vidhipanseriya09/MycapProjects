def print_positive_numbers(list1, list2):
    # Filter positive numbers from list1
    positive_list1 = [num for num in list1 if num > 0]
    # Filter positive numbers from list2
    positive_list2 = [num for num in list2 if num > 0]
    
    # Convert list of positive numbers to comma-separated string for list1
    output1 = ', '.join(map(str, positive_list1))
    # Convert list of positive numbers to comma-separated string for list2
    output2 = ', '.join(map(str, positive_list2))
    
    # Print the outputs in the desired format
    print(f"Input: list1 = {list1} Output: {output1}")
    print(f"Input: list2 = {list2} Output: {output2}")

# Example input lists
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Call the function with example inputs
print_positive_numbers(list1, list2)
