from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    print("[+] New encryption key generated.")
    print("[+] Key saved to:", KEY_FILE)


def load_key():
    if not os.path.exists(KEY_FILE):
        print("[!] Encryption key not found.")
        print("[!] Generate a key first.")
        return None

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_message():
    key = load_key()

    if key is None:
        return

    message = input("Enter message to encrypt: ")

    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())

    print("\n[+] Encrypted message:")
    print(encrypted_message.decode())


def decrypt_message():
    key = load_key()

    if key is None:
        return

    encrypted_message = input("Enter encrypted message: ")

    try:
        cipher = Fernet(key)
        decrypted_message = cipher.decrypt(
            encrypted_message.encode()
        )

        print("\n[+] Decrypted message:")
        print(decrypted_message.decode())

    except Exception:
        print("[!] Decryption failed.")
        print("[!] Check the encrypted message and encryption key.")


def main():
    while True:
        print("\n===================================")
        print("   Encryption / Decryption Tool")
        print("===================================")
        print("1. Generate Encryption Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            encrypt_message()

        elif choice == "3":
            decrypt_message()

        elif choice == "4":
            print("[+] Exiting...")
            break

        else:
            print("[!] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
