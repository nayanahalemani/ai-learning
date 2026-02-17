#bug tracking using conditions and loops
#using list, Dictionary, for loop, while loop and reuse Severity logic



# Initialize an empty dictionary to store bug input
bug_data = {}
exit_criteria='Exit'


while True:
    bug_id= input("Enter Bug ID: ")
    value = input(f"Enter the valueSeverity for '{bug_id}': ")
    
    # Store the key-value pair in the dictionary
    bug_data[bug_id] = value
    
    exit_criteria= input("Enter 'Exit' to finish or press enter to continue: ")

    if exit_criteria == 'Exit':
        break

# Print the collected data
print("\n--- Collected Data ---")

# Iterate through the dictionary and print each key-value pair using the .items() method
for bug_id, value in bug_data.items():
    print(f"{bug_id}: {value}")
