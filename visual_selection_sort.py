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

    # Delete only the bars (tagged as "bar")
    canvas.delete("bar")

    bar_width = canvas.winfo_width() / len(numbers)
    max_height = canvas.winfo_height() - 50  # Adjusted for increased top padding
    scale = max_height / max(numbers)

    colors = [DraculaColors.DEFAULT] * len(numbers)
    if current_index is not None:
        colors[current_index] = DraculaColors.CURRENT
    if next_index is not None:
        colors[next_index] = DraculaColors.NEXT

    for i, num in enumerate(numbers):
        canvas.create_rectangle(
            i * bar_width,
            50 + (max_height - num * scale),  # Increased top padding
            (i + 1) * bar_width,
            50 + max_height,  # Increased top padding
            fill=colors[i],
            outline=colors[i],
            tags="bar"  # Tag the bars for easy deletion
        )
        # Display the number above the bar
        canvas.create_text(
            i * bar_width + bar_width / 2,
            40 + (max_height - num * scale),  # Adjusted for increased top padding
            text=str(num),
            fill=DraculaColors.BUTTON_FG,
            tags="bar"
        )
    canvas.update()
    time.sleep(0.5)


def draw_legend(canvas):
    """Draw the color legend on the canvas."""
    legend_y = 10  # Adjust this value to position the legend vertically
    color_legend = [
        (DraculaColors.CURRENT, "Current"),
        (DraculaColors.NEXT, "Next"),
        (DraculaColors.DEFAULT, "Default")
    ]
    for i, (color, label) in enumerate(color_legend):
        canvas.create_rectangle(
            10 + i * 150, legend_y, 80 + i * 150, legend_y + 20,
            fill=color, outline=color
        )
        canvas.create_text(
            95 + i * 150, legend_y + 10, text=label,
            fill=DraculaColors.BUTTON_FG, anchor="w"
        )


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
    draw_legend(canvas)

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
