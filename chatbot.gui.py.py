import tkinter as tk
from tkinter import scrolledtext

# Function to send user message and bot response
def send_message():
    user_input = entry.get()
    if user_input != "":
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        entry.delete(0, tk.END)

        bot_response = generate_response(user_input)  # Removed "Bot:"
        chat_display.insert(tk.END, bot_response + "\n")
        chat_display.config(state=tk.DISABLED)
        chat_display.yview(tk.END)

# Function to generate bot response
def generate_response(user_input):
    return f"Hello, you said: {user_input}"

# Set up the main window
root = tk.Tk()
root.title("Chatbot")

# Create a scrolled text box for the chat history
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=("Arial", 12))
chat_display.pack(pady=10)
chat_display.config(state=tk.NORMAL)

# Insert initial bot message (without "Bot:")
chat_display.insert(tk.END, "Hello, I am Mantashah!\n")
chat_display.config(state=tk.DISABLED)

# Create an entry box for user input
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=10)

# Create a button to send the message
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
