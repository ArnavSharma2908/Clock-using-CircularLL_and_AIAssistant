import tkinter as tk

window = None
label = None

def display_message(message):
    """Displays or updates a message on the tkinter window."""
    global window, label

    if window is None:
        window = tk.Tk()
        window.title("Display Message")
        window.configure(bg="#1e1e1e")
        window.geometry("400x200")

        label = tk.Label(
            window,
            text=message,
            font=("Consolas", 24, "bold"),
            fg="#00ff00",
            bg="#1e1e1e"
        )
        label.pack(expand=True)
    else:
        label.config(text=message)

    window.update()

if __name__ == "__main__":
    display_message("Initial Message")