morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
    '8': '---..',  '9': '----.',

    ' ': '/'
}

reverse_morse_code = {value: key for key, value in morse_code.items()}


def encode(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    text = text.strip().upper()

    if not text:
        raise ValueError("Input cannot be empty.")

    encoded_characters = []

    for char in text:
        if char not in morse_code:
            raise ValueError(f"Unsupported character: {char}")
        encoded_characters.append(morse_code[char])

    return ' '.join(encoded_characters)


def decode(morse_text: str) -> str:
    if not isinstance(morse_text, str):
        raise TypeError("Input must be a string.")

    morse_text = morse_text.strip()

    if not morse_text:
        raise ValueError("Input cannot be empty.")

    decoded_characters = []
    symbols = morse_text.split()

    for symbol in symbols:
        if symbol not in reverse_morse_code:
            raise ValueError(f"Invalid Morse code symbol: {symbol}")
        decoded_characters.append(reverse_morse_code[symbol])

    return ''.join(decoded_characters)