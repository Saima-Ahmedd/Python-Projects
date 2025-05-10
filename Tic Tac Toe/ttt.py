import tkinter as tk
from tkinter import messagebox

# Function to check if a player has won
def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
                  [0, 4, 8], [2, 4, 6]]:            # diagonals
        if (buttons[combo[0]]['text'] != "" and
            buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text']):
            for i in combo:
                buttons[i].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

# Function for when a button is clicked
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

# Switch turns between X and O
def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

# Main setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game state
buttons = []
current_player = "X"
winner = False

# Display whose turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Create 9 buttons (3x3 grid)
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the app
root.mainloop()
