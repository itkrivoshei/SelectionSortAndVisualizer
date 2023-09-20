import tkinter as tk
from tkinter import scrolledtext

import matplotlib.pyplot as plt

from selection_sort import selection_sort


# Dracula color palette
class DraculaColors:
    BACKGROUND = '#282a36'
    CURRENT = '#ff79c6'
    NEXT = '#50fa7b'
    DEFAULT = '#f8f8f2'
    COMMENT = '#6272a4'
    GREEN = '#50fa7b'
    RED = '#ff5555'


def run_test(test_name, function_to_test, input_value, expected_output,
             test_results):
    # Make a copy of the input_value to preserve its original state
    input_copy = input_value.copy()
    result = function_to_test(input_copy)
    if result == expected_output:
        test_results.append((test_name, True, input_value, result))
    else:
        test_results.append((test_name, False, input_value, result))


def display_results_in_window(test_results, on_close_callback=None):
    # Create a new tkinter window
    root = tk.Tk()
    root.title("Test Results")

    # Set the window to full screen
    root.attributes('-fullscreen', True)

    # Set the background color to Dracula theme
    root.configure(bg=DraculaColors.BACKGROUND)

    # Use a scrolled text widget to display the results
    st = scrolledtext.ScrolledText(
        root,
        width=70,
        height=20,
        bg=DraculaColors.BACKGROUND,
        fg=DraculaColors.DEFAULT
    )
    st.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    for test_name, passed, input_data, result in test_results:
        st.insert(tk.END, f"{test_name}: ")
        color = DraculaColors.GREEN if passed else DraculaColors.RED
        status = "PASSED" if passed else "FAILED"
        st.insert(tk.END, f"{status}\n", (color,))

        if passed:
            st.insert(tk.END, "  Input: ", (DraculaColors.DEFAULT,))
            st.insert(tk.END, f"{input_data}\n", (DraculaColors.CURRENT,))
            st.insert(tk.END, "  Result: ", (DraculaColors.DEFAULT,))
            st.insert(tk.END, f"{result}\n", (DraculaColors.CURRENT,))
        else:
            st.insert(tk.END, "  Expected: ", (DraculaColors.DEFAULT,))
            st.insert(tk.END, f"{input_data}\n", (DraculaColors.CURRENT,))
            st.insert(tk.END, "  Actual: ", (DraculaColors.DEFAULT,))
            st.insert(tk.END, f"{result}\n", (DraculaColors.RED,))

    st.tag_config(DraculaColors.GREEN, foreground=DraculaColors.GREEN)
    st.tag_config(DraculaColors.RED, foreground=DraculaColors.RED)
    st.tag_config(DraculaColors.CURRENT, foreground=DraculaColors.CURRENT)
    st.config(state=tk.DISABLED)  # Make the text widget read-only

    def exit_and_callback():
        root.destroy()
        if on_close_callback:
            on_close_callback()

    exit_button = tk.Button(
        root,
        text="Exit",
        command=exit_and_callback,
        bg=DraculaColors.COMMENT,
        fg=DraculaColors.DEFAULT
    )
    exit_button.pack(pady=20)

    root.mainloop()


def test_selection_sort(main_function):
    test_results = []

    run_test("Test empty list", selection_sort, [], [], test_results)
    run_test("Test single element list", selection_sort, [42], [42],
             test_results)
    run_test("Test two element lists (1)", selection_sort, [42, 23], [23, 42],
             test_results)
    run_test("Test two element lists (2)", selection_sort, [23, 42], [23, 42],
             test_results)
    run_test("Test multiple elements", selection_sort,
             [64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90],
             test_results)
    run_test("Test negative numbers", selection_sort, [-5, -1, -89, 0, 3, 8],
             [-89, -5, -1, 0, 3, 8], test_results)
    run_test("Test repeated numbers", selection_sort, [5, 3, 5, 3, 5],
             [3, 3, 5, 5, 5], test_results)
    run_test("Test already sorted list", selection_sort, [1, 2, 3, 4, 5],
             [1, 2, 3, 4, 5], test_results)
    run_test("Test reverse sorted list", selection_sort, [5, 4, 3, 2, 1],
             [1, 2, 3, 4, 5], test_results)
    run_test("Test list with all identical elements", selection_sort,
             [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], test_results)
    run_test("Test list with large numbers", selection_sort,
             [1000000, 500000, 250000], [250000, 500000, 1000000],
             test_results)
    run_test("Test list with floating point numbers", selection_sort,
             [3.14, 2.71, 1.41], [1.41, 2.71, 3.14], test_results)

    display_results_in_window(test_results, on_close_callback=main_function)

    # Display the results using matplotlib
    fig, ax = plt.subplots(figsize=(10, len(test_results) * 0.5))
    ax.set_facecolor(DraculaColors.BACKGROUND)
    fig.patch.set_facecolor(DraculaColors.BACKGROUND)

    y_labels = [result[0] for result in test_results]
    y_pos = range(len(test_results))
    x_values = [1 if result[1] else 0 for result in test_results]
    colors = [
        DraculaColors.GREEN if result[1] else DraculaColors.RED
        for result in test_results
    ]

    ax.barh(y_pos, x_values, color=colors, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(y_labels, color=DraculaColors.DEFAULT)
    ax.set_xticks([])
    ax.set_title("Test Results", color=DraculaColors.DEFAULT)

    plt.show(block=True)

