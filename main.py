import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

from test_selection_sort import test_selection_sort
from visual_selection_sort import selection_sort_visualized


# Dracula color palette
class DraculaColors:
    BACKGROUND = '#282a36'
    CURRENT = '#ff79c6'
    NEXT = '#50fa7b'
    DEFAULT = '#f8f8f2'
    COMMENT = '#6272a4'


# Global list to store button objects and prevent them from being garbage collected
buttons = []


def test_button_callback(_):
    """Using underscore to indicate we're ignoring the argument."""
    # Disable fullscreen mode
    manager = plt.get_current_fig_manager()
    if hasattr(manager, "window"):
        manager.window.attributes('-fullscreen', False)

    test_selection_sort(main)

    # Re-enable fullscreen mode
    if hasattr(manager, "window"):
        manager.window.attributes('-fullscreen', True)

    plt.close('all')
    main()


def visualize_button_callback(_):
    """Using underscore to indicate we're ignoring the argument."""
    # Disable fullscreen mode
    manager = plt.get_current_fig_manager()
    if hasattr(manager, "window"):
        manager.window.attributes('-fullscreen', False)

    numbers = [64, 34, 25, 12, 22, 11, 90]
    selection_sort_visualized(numbers, main)

    # Re-enable fullscreen mode
    if hasattr(manager, "window"):
        manager.window.attributes('-fullscreen', True)

    plt.close('all')
    main()


def main():
    global buttons
    buttons.clear()  # Clear the list at the start of the function

    fig, ax = plt.subplots(figsize=(15, 10))
    fig.subplots_adjust(bottom=0.2)
    fig.patch.set_facecolor(DraculaColors.BACKGROUND)  # Set the background color

    ax.axis('off')  # Turn off the axis

    button_color = DraculaColors.COMMENT
    hover_color = DraculaColors.NEXT

    test_button = Button(
        ax=plt.axes((0.1, 0.6, 0.8, 0.1), facecolor=button_color),
        label="Test Selection Sort",
        color=DraculaColors.DEFAULT,
        hovercolor=hover_color
    )
    buttons.append(test_button)  # Add the button to the global list
    test_button.on_clicked(test_button_callback)

    visualize_button = Button(
        ax=plt.axes((0.1, 0.45, 0.8, 0.1), facecolor=button_color),
        label="Visualize Selection Sort",
        color=DraculaColors.DEFAULT,
        hovercolor=hover_color
    )
    buttons.append(visualize_button)  # Add the button to the global list
    visualize_button.on_clicked(visualize_button_callback)

    # Make the window fullscreen
    manager = plt.get_current_fig_manager()
    if hasattr(manager, "window"):
        manager.window.attributes('-fullscreen', True)

    plt.show()


if __name__ == "__main__":
    main()
