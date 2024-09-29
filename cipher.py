import random
import string
import time
import json
import os

# Constants
KEY_FILE = 'cipher_key.json'

# Generate the character set
chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

def generate_key():
    """Generates a shuffled key based on the chars list."""
    key = chars.copy()
    random.shuffle(key)
    return key

def save_key(key):
    """Saves the key to a JSON file for persistence."""
    with open(KEY_FILE, 'w') as file:
        json.dump(key, file)

def load_key():
    """Loads the key from a JSON file. Generates a new one if file doesn't exist."""
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as file:
            key = json.load(file)
            return key
    else:
        key = generate_key()
        save_key(key)
        return key

def create_decryption_dict(key):
    """Creates a dictionary for decryption to optimize lookups."""
    return {k: v for k, v in zip(key, chars)}

def encryption_algorithm(plain_text, key):
    """Encrypts the plain_text using the provided key."""
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Preserve non-mapped characters
    return cipher_text

def decryption_algorithm(cipher_text, decryption_dict):
    """Decrypts the cipher_text using the decryption dictionary."""
    plain_text = ""
    for letter in cipher_text:
        if letter in decryption_dict:
            plain_text += decryption_dict[letter]
        else:
            plain_text += letter  # Preserve non-mapped characters
    return plain_text

def display_menu():
    """Displays the encryption/decryption menu."""
    print("\n===== Simple Substitution Cipher =====")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    print("--------------------------------------")

def main():
    # Load or generate the key
    key = load_key()
    decryption_dict = create_decryption_dict(key)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            plain_text = input("Enter the message to encrypt: ")
            encryption = encryption_algorithm(plain_text, key)
            
            print("\nCiphering...")
            time.sleep(2)  # Shortened delay for better UX
            print("\n-------------------------------")
            print(f"Encrypted text: {encryption}")
            print("-------------------------------\n")
        
        elif choice == '2':
            cipher_text = input("Enter the encrypted message: ")
            decryption = decryption_algorithm(cipher_text, decryption_dict)
            
            print("\nDeciphering...")
            time.sleep(2)  # Shortened delay for better UX
            print("\n-------------------------------")
            print(f"Decrypted text: {decryption}")
            print("-------------------------------\n")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.\n")

if __name__ == '__main__':
    main()
