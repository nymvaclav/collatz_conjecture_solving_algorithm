# 1) Run self-check - check if all required files exist.
import os
import json

files_and_directories_to_check = ["main.py", "preferences.json", "setup.py", "output.txt", "logs/"]
missing_files = []

for dir in files_and_directories_to_check:
    if not os.path.exists(dir): # if checks if file/directory does not exist
        missing_files += [dir]

if missing_files != []:
    print("\033[91mWarning! The folowing files or directories which are critical for this program to function correctly were not found:\033[0m")
    for file in missing_files:
        print(file)
    print("Please, clone this repository into your device for the most recent (and working) version of this program.")
    print("$ git clone https://github.com/nymvaclav/collatz_conjecture_solving_algorithm\n")

# 2) Preferences

def get_valid_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt + "\n> "))
            if min_value is not None and value < min_value:
                print(f"Please enter an integer greater than or equal to {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_valid_list(prompt):
    while True:
        value = input(prompt + "\n> ")
        if value == "0":
            return []
        try:
            return list(map(int, value.split(',')))
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

def get_yes_no(prompt):
    while True:
        value = input(prompt + "\n> ").strip().lower()
        if value in ('y', 'n'):
            return value == 'y'
        print("Please enter 'y' or 'n'.")

def get_choice(prompt, choices):
    while True:
        value = input(prompt + f"\n> ").strip()
        if value in choices:
            return int(value)
        print(f"Invalid input. Please choose from {choices}.")

# Get user input
a_start_from_int = get_valid_int("Which integer to start from? (1 or higher int)", 1)
a_how_many_int_to_check = get_valid_int("How many integers do you want to check? (0 to set no limit)")
a_stop_at_int = get_valid_int("Which integer do you want to stop at (100 means that all integers < 100 will be checked)? (0 to never stop)")
a_stop_if_loop_is_found = get_choice(
    "All integers that were used in one calculation are recorded. If one integer appears in the result of any calculation twice, a loop was found and the Collatz Conjecture is proven not valid. If this happens, do you want to stop the program (1), start calculating the next integer (2), or continue calculating this integer and get stuck in a loop (3)? (enter 1, 2 or 3)",
    ['1', '2', '3']
)
a_exclude_int = get_valid_list("Which integers do you want to exclude? (0 to exclude none, otherwise seperate all integers by commas: 3,17,28,67)")
a_create_logs = get_yes_no("Do you want to create logs? (y/n)")
a_print_operations = get_yes_no("Do you want to print each operation ('Int: 21 ODD; Calculating: 21*3+1') that is being calculated into the terminal? (y/n)")
a_print_info = get_yes_no("Do you want to print info about what the program is doing into the terminal? (y/n)")
a_print_results = get_choice(
    "After checking an integer, would you like to display '{integer} ✅' if Collatz Conjecture applies (or '{integer} ❌' if it does not) in the terminal (1), or save it to output.txt instead (2), or do both (3)? (enter 1, 2, or 3)",
    ['1', '2', '3']
)

# Print out all preferences into the terminal for the user to double check the preferences
print("#### These preferences will now be saved:\n\n")

print("Which integer to start from? (1 or higher int)")
print(str(a_start_from_int) + "\n")

print("How many integers do you want to check? (0 to set no limit)")
print(str(a_how_many_int_to_check) + "\n")

print("Which integer do you want to stop at? (0 to never stop)")
print(str(a_stop_at_int) + "\n")

print("All integers that were used in one calculation are recorded. If one integer appears in the result of any calculation twice, a loop was found and the Collatz Conjecture is proven not valid. If this happens, do you want to stop the program (1), start calculating the next integer (2), or continue calculating this integer and get stuck in a loop (3)? (enter 1, 2 or 3)",)
print(str(a_stop_if_loop_is_found) + "\n")

print("Which integers do you want to exclude? (0 to exclude none, otherwise seperate all integers by commas: 3,17,28,67)")
print(str(a_exclude_int) + "\n")

print("Do you want to print each operation ('Int: 21 ODD; Calculating: 21*3+1') that is being calculated into the terminal? (y/n)")
print(str(a_print_operations) + "\n")

print("Do you want to print info about what the program is doing into the terminal? (y/n)")
print(str(a_print_info) + "\n")

print("Do you want to create logs? (y/n)")
print(str(a_create_logs) + "\n")

print("After checking an integer, would you like to display '{integer} ✅' if Collatz Conjecture applies (or '{integer} ❌' if it does not) in the terminal (1), or save it to output.txt instead (2)? (enter 1 or 2)",)
print(str(a_print_results) + "\n\n")


# 3) Save the preferences

data = {
    "start_from_int": a_start_from_int,
    "how_many_int_to_check": a_how_many_int_to_check,
    "stop_at_int": a_stop_at_int,
    "stop_if_loop_is_found": a_stop_if_loop_is_found,
    "exclude_int": a_exclude_int,
    "create_logs": a_create_logs,
    "print_info": a_print_info,
    "print_operations": a_print_operations,
    "print_results": a_print_results
}

# Dump data into a JSON file
with open("preferences.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Your preferences have been saved successfully! Please, run main.py to start the algorithm.")