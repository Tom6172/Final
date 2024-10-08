DATA = """
100
200
300

400
250

100

600
700
900

300
"""

def find_value_of_largest_order():
    # Print statement for debugging to ensure the function runs
    print("Function is running...")
    
    # Split the data by double newlines to separate each order
    orders = DATA.strip().split("\n\n")
    
    max_order_value = 0
    
    # Loop through each order
    for order in orders:
        # Split each order's lines into individual values
        product_values = order.split("\n")
        # Convert the string values to integers and sum them
        total_value = sum(int(value) for value in product_values)
        # Print the total value for debugging
        print("Total order value:", total_value)
        # Update the max order value if this order's total is higher
        if total_value > max_order_value:
            max_order_value = total_value
    
    # Print the largest order value
    print("Largest order value:", max_order_value)

if __name__ == "__main__":
    # Print statement to confirm the script starts executing
    print("Starting the script...")
    find_value_of_largest_order()
