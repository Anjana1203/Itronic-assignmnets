
def find_mean(count, mean):
    '''Method to find mean recursively

    Args:
        Count (int): Count of mean operation
        mean (float): Previous mean value

    Returns:
        Current mean value
    '''
    num = input("Enter a number (or 'x' to exit): ")
    if num == 'x':
        print("Program ended.")
        return
    try:
        # Mean value calculation
        mean = (((count-1) * mean) + float(num)) / count
        print("Mean value: {:.2f}".format(mean))
        find_mean(count+1, mean)
    except ValueError:
        print("Invalid input. Please enter a number or 'x' to exit.")
        find_mean(count, mean)

# Program start here
find_mean(1, 0.0)