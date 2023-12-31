import tkinter as tk
from tkinter import ttk
import pyautogui
import pygetwindow

# The app was developed by Tom Girshovksi.
class CenterWindowGUI:
    def __init__(self, master):
        self.master = master
        master.title("Center Window")

        # Create the frame
        self.frame = ttk.Frame(master, padding=20)
        self.frame.pack()

        # Configure columns to have equal weight
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

        # Create the label
        self.label = ttk.Label(self.frame, text="Choose a window to center:")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create the listbox to display the windows
        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.update_windows()

        # Center Button
        self.center_button = ttk.Button(self.frame, text="Center Window", command=self.center_window)
        self.center_button.grid(row=2, column=0, pady=10)

        # Scale Function Button
        self.scale_button = ttk.Button(self.frame, text="Scale Window", command=self.scale_window)
        self.scale_button.grid(row=2, column=1, pady=10)  

        # Update List Button
        self.update_button = ttk.Button(self.frame, text="Update List", command=self.update_windows)
        self.update_button.grid(row=2, column=2, pady=10)

    def center_window(self):
        # Get the index of the selected item in the list box
        index = self.listbox.curselection()[0]
        # Get the selected window
        window = self.windows[index]
        # Get the size of the screen
        screen_width, screen_height = pyautogui.size()
        # Get the size of the window
        window_width, window_height = window.size
        # Calculate the new position to center the window
        new_left = (screen_width - window_width) // 2
        new_top = (screen_height - window_height) // 2
        # Move the window to the new position
        window.moveTo(new_left, new_top)

    def update_windows(self):
        # Clear the list box
        self.listbox.delete(0, tk.END)
        # Get a list of all windows that are currently open
        self.windows = pyautogui.getAllWindows()
        # Add the window titles to the list box
        for window in self.windows:
            self.listbox.insert(tk.END, window.title)

    def scale_window(self):
        # Get the index of the selected item in the list box
        index = self.listbox.curselection()[0]
        # Get the selected window
        window = self.windows[index]
        # Get the size of the screen
        screen_width, screen_height = pyautogui.size()
        # Get the size of the window
        window_width, window_height = window.size

        if window_width == screen_width and window_height == screen_height:
            # If the window is already full screen, center it instead
            self.center_window()
        else:
            # Resize the window to full screen
            window.resizeTo(screen_width // 2 + 500, screen_height // 2 +300)
        


# Create the root window
root = tk.Tk()
root.resizable(False, False)
# Set the style of the GUI
style = ttk.Style(root)
gui = CenterWindowGUI(root)

root.mainloop()
