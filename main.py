def main():
    print("Data Security Project Running")

if __name__ == "__main__":
    main()
from algorithms.rail_fence import encrypt as rf_encrypt, decrypt as rf_decrypt
from algorithms.morse import encrypt as morse_encrypt, decrypt as morse_decrypt
from algorithms.homophonic import encrypt as h_encrypt, decrypt as h_decrypt


def main():
    while True:
        print("\n--- DATA SECURITY TEST ---")
        print("1. Rail Fence")
        print("2. Morse Code")
        print("3. Homophonic")
        print("4. Exit")

        choice = input("Choose algorithm: ")

        if choice == "1":
            text = input("Enter text: ")
            key = int(input("Enter key: "))

            cipher = rf_encrypt(text, key)
            print("Encrypted:", cipher)

            print("Decrypted:", rf_decrypt(cipher, key))

        elif choice == "2":
            text = input("Enter text: ")

            cipher = morse_encrypt(text)
            print("Encrypted:", cipher)

            print("Decrypted:", morse_decrypt(cipher))

        elif choice == "3":
            text = input("Enter text: ")

            cipher = h_encrypt(text)
            print("Encrypted:", cipher)

            print("Decrypted:", h_decrypt(cipher))

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()