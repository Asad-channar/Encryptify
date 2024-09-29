import tkinter as tk
from tkinter import messagebox
import cipher  # Import the cipher module

# Load or generate the key and decryption dictionary
key = cipher.load_key()
decryption_dict = cipher.create_decryption_dict(key)

# GUI Functions
def encrypt_message():
    plain_text = entry_plain.get("1.0", "end-1c")  # Get the input from the text box
    if plain_text:
        encryption = cipher.encryption_algorithm(plain_text, key)
        entry_cipher.delete("1.0", tk.END)
        entry_cipher.insert(tk.END, encryption)
    else:
        messagebox.showerror("Error", "Please enter a message to encrypt.")

def decrypt_message():
    cipher_text = entry_cipher.get("1.0", "end-1c")  # Get the input from the text box
    if cipher_text:
        decryption = cipher.decryption_algorithm(cipher_text, decryption_dict)
        entry_plain.delete("1.0", tk.END)
        entry_plain.insert(tk.END, decryption)
    else:
        messagebox.showerror("Error", "Please enter a message to decrypt.")

def clear_text():
    entry_plain.delete("1.0", tk.END)
    entry_cipher.delete("1.0", tk.END)

# GUI Setup
root = tk.Tk()
root.title("Encryptify")

# Set a permanent size for the window
root.geometry("600x400")  # Width x Height
root.resizable(False, False)  # Disable resizing

# Set background color
root.configure(bg="#D6C6B8")  # Light foggy brown background

# Configure grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Labels
label_plain = tk.Label(root, text="Plain Text:", font=("Arial", 15), bg="#D6C6B8", fg="#343A40")
label_plain.grid(row=0, column=0, padx=(5, 2), pady=(10, 0), sticky="w")  # Align to the left

label_cipher = tk.Label(root, text="Encrypted Text:", font=("Arial", 15), bg="#D6C6B8", fg="#343A40")
label_cipher.grid(row=1, column=0, padx=(5, 2), pady=(10, 0), sticky="w")  # Align to the left

# Text boxes
entry_plain = tk.Text(root, height=4, width=50, font=("Arial", 10), bg="#FFFFFF", fg="#212529")  # White background
entry_plain.grid(row=0, column=1, padx=5, pady=(10, 0), sticky="w")  # Align to the left

entry_cipher = tk.Text(root, height=4, width=50, font=("Arial", 10), bg="#FFFFFF", fg="#212529")  # White background
entry_cipher.grid(row=1, column=1, padx=5, pady=(10, 10), sticky="w")  # Align to the left

# Buttons Frame to hold buttons in a row and center them
button_frame = tk.Frame(root, bg="#D6C6B8")  # Same background as root
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Buttons with color scheme
button_encrypt = tk.Button(button_frame, text="Encrypt", command=encrypt_message, font=("Arial", 10), width=15, bg="#007BFF", fg="#FFFFFF")
button_encrypt.grid(row=0, column=0, padx=10)

button_decrypt = tk.Button(button_frame, text="Decrypt", command=decrypt_message, font=("Arial", 10), width=15, bg="#28A745", fg="#FFFFFF")
button_decrypt.grid(row=0, column=1, padx=10)

button_clear = tk.Button(button_frame, text="Clear", command=clear_text, font=("Arial", 10), width=15, bg="#DC3545", fg="#FFFFFF")
button_clear.grid(row=0, column=2, padx=10)

# Center the button frame
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)

# Run the application
root.mainloop()
