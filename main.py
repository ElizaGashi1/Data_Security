# ================= IMPORTS =================

# Morse (mbështet encrypt/decrypt OSE encode/decode)
from algorithms.MorseCode import morse as morse_module

# Homophonic
import algorithms.Homophonic_sub_cipher as homophonic_module


# ================= HELPER FUNCTIONS =================

def get_encrypt(module):
    if hasattr(module, "encrypt"):
        return module.encrypt
    elif hasattr(module, "encode"):
        return module.encode
    else:
        raise Exception(f"{module.__name__} has no encrypt/encode function")


def get_decrypt(module):
    if hasattr(module, "decrypt"):
        return module.decrypt
    elif hasattr(module, "decode"):
        return module.decode
    else:
        raise Exception(f"{module.__name__} has no decrypt/decode function")


# ================= FLOWS =================

def morse_flow():
    encrypt = get_encrypt(morse_module)
    decrypt = get_decrypt(morse_module)

    text = input("Enter text: ")

    cipher = encrypt(text)
    print("Encrypted:", cipher)

    print("Decrypted:", decrypt(cipher))


def homophonic_flow():
    encrypt = get_encrypt(homophonic_module)
    decrypt = get_decrypt(homophonic_module)

    text = input("Enter text: ")

    try:
        cipher = encrypt(text)
        print("Encrypted:", cipher)

        print("Decrypted:", decrypt(cipher))
    except TypeError:
        # nëse kërkon key
        key = input("Enter key: ")
        cipher = encrypt(text, key)
        print("Encrypted:", cipher)

        print("Decrypted:", decrypt(cipher, key))


# ================= MAIN =================

def main():
    while True:
        print("\n--- DATA SECURITY TEST ---")
        print("1. Morse Code")
        print("2. Homophonic")
        print("3. Exit")

        choice = input("Choose algorithm: ")

        if choice == "1":
            morse_flow()

        elif choice == "2":
            homophonic_flow()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
    