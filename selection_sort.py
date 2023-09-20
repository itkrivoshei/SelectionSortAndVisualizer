def selection_sort(numbers):
    """Sort a list of numbers using the selection sort algorithm."""
    
    # Determine the number of elements in the list
    length = len(numbers)

    # Iterate over each element in the list
    for current_index in range(length):
        # Start by assuming the current element is the smallest
        smallest_index = current_index

        # Iterate over the unsorted portion of the list
        for next_index in range(current_index + 1, length):
            # If a smaller element is found, update the smallest_index
            if numbers[next_index] < numbers[smallest_index]:
                smallest_index = next_index

        # Swap the current element with the smallest found element
        # (if they are different)
        if smallest_index != current_index:
            numbers[current_index], numbers[smallest_index] = (
                numbers[smallest_index], numbers[current_index]
            )

    # Return the sorted list
    return numbers
