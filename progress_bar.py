import math
import colorama

# Define a function to print a progress bar
def progress_bar(progress, total, color=colorama.Fore.YELLOW):
    # Calculate the percentage of completion
    percent = 100 * (progress/ float(total))
    # Create a progress bar string with blocks and dashes
    bar = chr(9617) *int(percent) + '-' * (100- int(percent))
    # Print the progress bar
    print(color+ f"\r|{bar}| {percent:.2f}%", end="\r")
    # If progress is completed, print the progress bar in green color
    if progress == total:
        print(colorama.Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")
        # Reset the color to default
        print(colorama.Fore.RESET)

# Create a list of numbers to calculate factorials
number= [x* 5 for x in range(2000,3000)]
# Create an empty list to store the results
result = []

# Print the initial progress bar with progress = 0
progress_bar(0, len(number))

# Calculate the factorials of each number in the list
for i,x in enumerate(number):
    result.append(math.factorial(x))
    # Update the progress bar with each iteration
    progress_bar(i+1, len(number))


