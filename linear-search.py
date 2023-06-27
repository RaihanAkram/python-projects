# function for linear search
def linear_search(array, target):
    for index, value in enumerate(array): #enumerate used to check for both value and the index simultaneously.
        if value == target:
            return index  # index of target element is returned
    return -1  # target element not found

array_1 = [3, 6, 2, 1, 2]
target_number = 1

result = linear_search(array_1, target_number)
if result != -1:
    print(f"Target number {target_number} found at index {result}.")
else:
    print("Target number not found in the list.")


