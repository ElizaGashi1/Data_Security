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
            plaintext_chars.append(
                rails_data[rail_idx][rail_pointers[rail_idx]]
            )
            rail_pointers[rail_idx] += 1

        return "".join(plaintext_chars)


# ===================== COMPATIBILITY LAYER =====================

def encrypt(text: str, key: int = 3) -> str:
    """
    Compatible me main.py (uniform interface)
    """
    return RailFenceCipher(key).encrypt(text)


def decrypt(text: str, key: int = 3) -> str:
    """
    Compatible me main.py (uniform interface)
    """
    return RailFenceCipher(key).decrypt(text)