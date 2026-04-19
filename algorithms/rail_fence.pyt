class RailFenceCipher:

    def __init__(self, rails: int):
        if rails < 2:
            raise ValueError("Numri i shiritave duhet te jete te pakten 2.")
        self.rails = rails

    def _build_pattern(self, length: int) -> list[int]:
        pattern = []
        rail = 0
        direction = 1

        for _ in range(length):
            pattern.append(rail)
            if rail == 0:
                direction = 1
            elif rail == self.rails - 1:
                direction = -1
            rail += direction

        return pattern

    def encrypt(self, plaintext: str) -> str:
        if not plaintext:
            return ""

        pattern = self._build_pattern(len(plaintext))
        rails_data = [[] for _ in range(self.rails)]
        for char, rail_idx in zip(plaintext, pattern):
            rails_data[rail_idx].append(char)

        return "".join("".join(row) for row in rails_data)

    def decrypt(self, ciphertext: str) -> str:
        if not ciphertext:
            return ""

        n = len(ciphertext)
        pattern = self._build_pattern(n)

        rail_lengths = [0] * self.rails
        for rail_idx in pattern:
            rail_lengths[rail_idx] += 1

        rails_data = []
        pos = 0
        for length in rail_lengths:
            rails_data.append(list(ciphertext[pos: pos + length]))
            pos += length

        rail_pointers = [0] * self.rails
        plaintext_chars = []
        for rail_idx in pattern:
            plaintext_chars.append(rails_data[rail_idx][rail_pointers[rail_idx]])
            rail_pointers[rail_idx] += 1

        return "".join(plaintext_chars)

    def __repr__(self) -> str:
        return f"RailFenceCipher(rails={self.rails})"


def rail_fence_encrypt(plaintext: str, rails: int) -> str:
    return RailFenceCipher(rails).encrypt(plaintext)


def rail_fence_decrypt(ciphertext: str, rails: int) -> str:
    return RailFenceCipher(rails).decrypt(ciphertext)


def _get_rails() -> int:
    while True:
        try:
            rails = int(input("Numri i shiritave: ").strip())
            if rails < 2:
                print("Gabim: duhet te jete te pakten 2.")
            else:
                return rails
        except ValueError:
            print("Gabim: shkruaj nje numer te plote.")


def main():
    while True:
        print("\n1. Enkriptim")
        print("2. Dekriptim")
        print("3. Dil")

        choice = input("\nZgjidh: ").strip()

        if choice == "1":
            teksti = input("Shkruaj tekstin: ")
            if not teksti:
                print("Gabim: teksti eshte bosh.")
                continue
            rails = _get_rails()
            rezultati = RailFenceCipher(rails).encrypt(teksti)
            print(f"Rezultati: {rezultati}")

        elif choice == "2":
            teksti = input("Shkruaj tekstin e enkriptuar: ")
            if not teksti:
                print("Gabim: teksti eshte bosh.")
                continue
            rails = _get_rails()
            rezultati = RailFenceCipher(rails).decrypt(teksti)
            print(f"Rezultati: {rezultati}")

        elif choice == "3":
            print("Mirupafshim!")
            break

        else:
            print("Gabim: zgjidhni 1, 2 ose 3.")


if __name__ == "__main__":
    main()