def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

print(CYAN + BOLD + "="*40)
print(YELLOW + BOLD + "         Caesar Cipher Tool         ")
print(CYAN + BOLD + "="*40 + RESET)

print(GREEN + "1. Encrypt a message")
print(MAGENTA + "2. Decrypt a message")

choice = input(CYAN + BOLD + "Enter your choice (1 or 2): " + RESET)

if choice in ['1', '2']:
    message = input(WHITE + "Enter your message: " + RESET)
    try:
        shift = int(input(WHITE + "Enter shift value (e.g., 3): " + RESET))
    except ValueError:
        print(RED + "Shift must be an integer.")
        exit()

    if choice == '1':
        encrypted = caesar_cipher(message, shift)
        print(GREEN + BOLD + "\nEncrypted Message:")
        print(CYAN + encrypted)
    else:
        decrypted = caesar_cipher(message, shift, decrypt=True)
        print(MAGENTA + BOLD + "\nDecrypted Message:")
        print(CYAN + decrypted)
else:
    print(RED + "Invalid choice. Please select 1 or 2.")
