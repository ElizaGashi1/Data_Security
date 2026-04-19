import random

CIPHER_TABLE = {
    'E': list(range(0,  12)),   # 12 simbole (~12% frekuence ne fajlor te perdorur)
    'T': list(range(12, 20)),   # 8 simbole
    'A': list(range(20, 28)),   # 8 ...
    'O': list(range(28, 36)),   # 8 .. 
    'I': list(range(36, 43)),   # 7 .
    'N': list(range(43, 50)),   # 7
    'S': list(range(50, 56)),   # 6
    'H': list(range(56, 62)),   # 6
    'R': list(range(62, 68)),   # 6
    'D': list(range(68, 72)),   # 4
    'L': list(range(72, 76)),   # 4
    'C': list(range(76, 79)),   # 3
    'U': list(range(79, 82)),   # 3
    'M': list(range(82, 84)),   # 2
    'W': list(range(84, 86)),   # 2
    'F': list(range(86, 88)),   # 2
    'G': list(range(88, 90)),   # 2
    'Y': list(range(90, 92)),   # 2
    'P': list(range(92, 94)),   # 2
    'B': [94],                  # 1
    'V': [95],
    'K': [96],
    'J': [97],
    'X': [98],
    'Q': [99],
    'Z': [100],
    ' ': [101],
}

# Reverse lookup: code → letter:
REVERSE_TABLE = {}
for letter, codes in CIPHER_TABLE.items():
    for code in codes:
        REVERSE_TABLE[code] = letter

#Enkriptimi // Dekriptimi:
def encrypt(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input-i duhet te jete string.")
    text = text.strip().upper()
    if not text:
        raise ValueError("Input-i nuk duhet te jete i zbrazet.")

    result = []
    for char in text:
        if char not in CIPHER_TABLE:
            raise ValueError(f"Unsupported character: '{char}'")
        chosen_code = random.choice(CIPHER_TABLE[char])
        result.append(str(chosen_code).zfill(3)) 

    return ' '.join(result)


def decrypt(cipher_text: str) -> str:
    if not isinstance(cipher_text, str):
        raise TypeError("Input must be a string.")
    cipher_text = cipher_text.strip()
    if not cipher_text:
        raise ValueError("Input cannot be empty.")

    result = []
    tokens = cipher_text.split()
    for token in tokens:
        if not token.isdigit():
            raise ValueError(f"Invalid token: '{token}'")
        code = int(token)
        if code not in REVERSE_TABLE:
            raise ValueError(f"Unknown code: {code}")
        result.append(REVERSE_TABLE[code])

    return ''.join(result)


#Inputi i Userit:
print("=" * 45)
print("   Homophonic Substitution Cipher")
print("=" * 45)

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Demo (encrypt te njejten fjale 3 here)")
    print("4. Exit")
    choice = input("\nZgjidh (1/2/3/4): ").strip()

    if choice == "1":
        text = input("Teksti: ")
        try:
            result = encrypt(text)
            print(f"Encrypted: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

    elif choice == "2":
        cipher = input("Cipher (numrat e ndare me hapesire): ")
        try:
            result = decrypt(cipher)
            print(f"Decrypted: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

    elif choice == "3":
        word = input("Fjala per demo: ")
        try:
            print(f"\nE njejte fjale '{word.upper()}', 3 rezultate te ndryshme:")
            for i in range(3):
                enc = encrypt(word)
                print(f"  {i+1}: {enc}")
            print()
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

    elif choice == "4":
        print("Duke dalur...")
        break

    else:
        print("Zgjidhje e pavlefshme.\n")