#The Vigenère cipher is a method of encrypting messages by using a series of different Caesar ciphers based on the letters of a particular keyword. The Vigenère cipher is more powerful than a single Caesar cipher and is much harder to crack.
#Enjoy!

def vigenere_cipher(text, key, mode):
    result = ""
    key_index = 0
    for char in text:
        if char.islower():  # Check if the character is a lowercase letter
            if mode == 'encrypt':
                # Shift the character by the corresponding key value (wrapping around if needed)
                shifted = chr((ord(char) - ord('a') + ord(key[key_index]) - ord('a') + 1) % 26 + ord('a'))
            elif mode == 'decrypt':
                # Reverse the encryption process to decrypt the character
                shifted = chr((ord(char) - ord('a') - ord(key[key_index]) + ord('a') - 1) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)  # Move to the next letter in the key
        else:
            # If the character is not a lowercase letter, leave it unchanged
            shifted = char
        result += shifted
    return result

# Loop until the user decides to exit
while True:
    choice = input("Enter '1' to encrypt text, '2' to decrypt text, or '0' to exit: ")
    if choice == '0':
        break  # Exit the loop if the user enters '0'

    if choice == '1':
        key = input("Enter a key (a word): ").lower()  # Accept key as a word
        while True:
            user_input = input("Enter a text to encrypt (enter '0' to return to menu): ").lower()  # Convert input to lowercase
            if user_input == '0':
                break  # Exit the inner loop if the user enters '0'
            
            # Call the function and print the encrypted result
            result = vigenere_cipher(user_input, key, 'encrypt')
            print("Encrypted Result:", result)
    elif choice == '2':
        key = input("Enter a key (a word): ").lower()  # Accept key as a word
        while True:
            user_input = input("Enter a text to decrypt (enter '0' to return to menu): ").lower()  # Convert input to lowercase
            if user_input == '0':
                break  # Exit the inner loop if the user enters '0'
            
            # Call the function and print the decrypted result
            result = vigenere_cipher(user_input, key, 'decrypt')
            print("Decrypted Result:", result)


