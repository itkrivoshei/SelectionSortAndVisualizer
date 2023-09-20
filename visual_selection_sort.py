import time
import tkinter as tk
from tkinter import Button, Canvas


# Define the Dracula color palette for visualization
class DraculaColors:
    BACKGROUND = '#282a36'
    CURRENT = '#ff79c6'
    NEXT = '#50fa7b'
    DEFAULT = '#f8f8f2'
    BUTTON_BG = '#44475a'
    BUTTON_FG = '#f8f8f2'


# Global variable to control stopping the sorting
STOP_SORTING = False


def exit_callback(root, main_function):
    """
    Callback function to stop the sorting process and exit the window.
    """
    global STOP_SORTING
    STOP_SORTING = True
    root.destroy()
    main_function()  # Return to the main window


def visualize_numbers(canvas, root, numbers, current_index=None, next_index=None):
    """
    Visualize the numbers on a canvas during sorting.
    """
    if not root.winfo_exists():
        return
    canvas.delete("all")
    canvas.configure(bg=DraculaColors.BACKGROUND)

    bar_width = canvas.winfo_width() / len(numbers)
    max_height = canvas.winfo_height()
    scale = max_height / max(numbers)

    colors = [DraculaColors.DEFAULT] * len(numbers)
    if current_index is not None:
        colors[current_index] = DraculaColors.CURRENT
    if next_index is not None:
        colors[next_index] = DraculaColors.NEXT

    for i, num in enumerate(numbers):
        canvas.create_rectangle(
            i * bar_width,
            max_height - num * scale,
            (i + 1) * bar_width,
            max_height,
            fill=colors[i],
            outline=colors[i]
        )
    canvas.update()
    time.sleep(0.5)


def selection_sort_visualized(numbers, main_function):
    """
    Visualize the selection sort algorithm.
    """
    global STOP_SORTING
    STOP_SORTING = False

    root = tk.Tk()
    root.title("Selection Sort Visualization")
    root.geometry("800x600")
    root.attributes('-fullscreen', True)

    canvas = Canvas(root, bg=DraculaColors.BACKGROUND)
    canvas.pack(fill=tk.BOTH, expand=True)

    exit_button = Button(
        root,
        text="Exit",
        bg=DraculaColors.BUTTON_BG,
        fg=DraculaColors.BUTTON_FG,
        command=lambda: exit_callback(root, main_function)
    )
    exit_button.pack()

    for current_index in range(len(numbers)):
        if STOP_SORTING:
            break
        smallest_index = current_index
        for next_index in range(current_index + 1, len(numbers)):
            if STOP_SORTING:
                break
            visualize_numbers(canvas, root, numbers, current_index, next_index)
            if numbers[next_index] < numbers[smallest_index]:
                smallest_index = next_index
        if STOP_SORTING:
            break
        if smallest_index != current_index:
            numbers[current_index], numbers[smallest_index] = numbers[
                smallest_index], numbers[current_index]
            visualize_numbers(canvas, root, numbers, current_index, smallest_index)

    root.mainloop()

    return numbers
