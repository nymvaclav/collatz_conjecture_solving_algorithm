import json
import os

class tc:
    white = '\033[0m' # White
    cyan = '\033[96m' # Light blue / cyan
    purple = '\033[95m' # Purple
    green = '\033[92m' # Green
    yellow = '\033[93m' # Yellow
    red = '\033[91m' # Red
    grey = '\33[90m' # Grey
    space = '     '

with open("preferences.json", "r") as file:
    data = json.load(file)

start_from_int = data["start_from_int"]
how_many_int_to_check = data["how_many_int_to_check"]
stop_at_int = data["stop_at_int"]
stop_if_loop_is_found = data["stop_if_loop_is_found"]
exclude_int = data["exclude_int"]
create_logs = data["create_logs"]
print_operations = data["print_operations"]
print_info = data["print_info"]
print_results = data["print_results"]


def operations(to_print):
    if print_operations:
        print(to_print)

def result(to_print):
    if print_results == 1 or print_results == 3:
        print(to_print)

def info(to_print):
    if print_info:
        print(to_print)

def check_even(int):
    return int % 2 == 0  # Returns True if even, False if odd

def loop_found(int):
    update_output_txt(f"Invalid ❌: {str(integer)}") # Update the output.txt

    if stop_if_loop_is_found == 1: # stop the program
        result(f"{tc.red}Checked ❌: {str(int)} >>> We are in a loop! Stopping the program based on your preferences!{tc.white}")
        exit()
    elif stop_if_loop_is_found == 2: # start calculating the next integer
        result(f"{tc.red}Checked ❌: {str(int)} >>> We are in a loop! Starting to calculate the next integer based on your preferences!{tc.white}")
        integer += 1
        return True # skip to the next integer

    elif stop_if_loop_is_found == 3: # continue calculating this integer and get stuck in a loop
        return False
    
def update_output_txt(text_to_append):
    if print_results == 2 or print_results == 3:
        with open("output.txt", "r") as file:
            data = file.read()
        with open("output.txt", "w") as file:
            data = f'{data}\n{text_to_append}'
            file.write(data)

def log_operation(operation):
    if create_logs:
        # create the file if it does not exist yet:
        if not os.path.exists(f"logs/{integer}.txt"):
            with open(f"logs/{integer}.txt", "w") as file:
                file.write(f"Starting Integer: {integer}\n\n")
        
        # log the new operation
        with open(f"logs/{integer}.txt", "r") as file:
            data = file.read()
        with open(f"logs/{integer}.txt", "w") as file:
            data = f'{data}\n{operation}'
            file.write(data)



global integer
integer = start_from_int

if how_many_int_to_check == 0:
    infinite_int_to_check = True # True = check infinite integers
else:
    infinite_int_to_check = False

while how_many_int_to_check > 0 or infinite_int_to_check:
    info(f"Integers left to check based on your preferences: {str(how_many_int_to_check)}")
    how_many_int_to_check -= 1

    # Check if this INT is in a list of INTs to exclude
    if integer in exclude_int:
        info(f"{tc.yellow}{str(integer)} is in the list of excluded integers. Skipping!{tc.white}")
        integer += 1
        continue

    # Check if this INT is equal to stop_at_int
    if integer == stop_at_int:
        info(f"{tc.red}You chose to stop at {str(stop_at_int)}, which has just been reached (reached: {str(integer)}) Stopping!{tc.white}")
        exit()

    info(f"Now: Checking {str(integer)}")
    
    # Start the algorithm:
    integers_checked = [integer]
    integer_calc = integer

    while integer_calc != 1:

        # Do the operation
        if check_even(integer_calc):
            operations(f"{tc.space}{tc.grey}EVEN: {tc.white}{integer_calc}{tc.grey} /2{tc.white}")
            log_operation(f"EVEN: {integer_calc} /2")
            integer_calc = integer_calc // 2
        else:
            operations(f"{tc.space}{tc.grey}ODD: {tc.white}{integer_calc}{tc.grey} *3+1{tc.white}")
            log_operation(f"ODD: {integer_calc} *3+1")
            integer_calc = integer_calc * 3
            integer_calc += 1
        
        # Check if we are in a loop
        if integer_calc in integers_checked:
            if loop_found():
                break

        # Update the list of integers used
        integers_checked = [integers_checked] + [integer_calc]
    else:
        result(f"{tc.green}Checked ✅: {str(integer)}{tc.white}")
        update_output_txt(f"Valid ✅: {str(integer)}")
        integer += 1