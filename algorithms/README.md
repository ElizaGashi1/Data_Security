# Data Security – Classical Cryptographic Algorithms

Implementim modular i algoritmeve klasike kriptografike në Python:
**Rail Fence Cipher**, **Morse Code**, dhe **Homophonic Substitution Cipher** —
me një ndërfaqe të unifikuar enkriptim/dekriptim.

---

## Struktura e projektit

```
Data_Security/
├── algorithms/
│   ├── __init__.py
│   ├── rail_fence.py          ← Anëtar 3
│   ├── morse_code.py
│   └── homophonic.py
├── tests/
│   ├── test_rail_fence.py     ← Anëtar 3
│   ├── test_morse_code.py
│   └── test_homophonic.py
├── .gitignore
└── README.md
```

---

## Si të instalohet dhe ekzekutohet

### Kërkesat

- Python **3.10+** (testohet me 3.12)
- `pytest` për testim

### Instalimi

```bash
# 1. Klonimi i repository
git clone https://github.com/ElizaGashi1/Data_Security.git
cd Data_Security

# 2. (Opsionale) Krijo virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Instalo varësitë
pip install pytest
```

### Ekzekutimi i algoritmeve

```bash
# Rail Fence Cipher – demo i plotë
python algorithms/rail_fence.py

# Morse Code – demo
python algorithms/morse_code.py

# Homophonic Cipher – demo
python algorithms/homophonic.py
```

### Ekzekutimi i testeve

```bash
# Të gjitha testet
python -m pytest tests/ -v

# Vetëm Rail Fence
python -m pytest tests/test_rail_fence.py -v

# Me raport coverage (kërkon pytest-cov)
pip install pytest-cov
python -m pytest tests/ --cov=algorithms --cov-report=term-missing
```

---

## Algoritmet e implementuara

---

### 1. Rail Fence Cipher *(Anëtar 3)*

#### Përshkrimi

**Rail Fence Cipher** (ose *Zig-Zag Cipher*) është një **shifër transpozicioni** klasike. Ndryshe nga shifrat me substitucim, Rail Fence i **rirendit** karakteret e plaintextit pa i ndryshuar ato — vetëm pozicioni i tyre ndryshon.

Karakteret shkruhen në model zig-zag nëpër `N` rreshta (rails), pastaj lexohen rresht pas rreshti për të formuar ciphertekstin.

**Çelësi:** Numri i rails `N` (duhet të jetë ≥ 2).

**Siguria:** E dobët — hapësira e vogël e çelësit lejon brute force. Përdorim kryesisht edukativ.

#### Si funksionon — shembull vizual

Plainteksti `HELLO` me 2 rails:

```
Rail 0:  H . L . O
Rail 1:  . E . L .

Ciphertext: H L O + E L = HLOEL
```

Plainteksti `WEAREDISCOVEREDFLEEATONCE` me 3 rails:

```
Rail 0:  W . . . E . . . C . . . R . . . L . . . T . . . E
Rail 1:  . E . A . R . D . S . O . E . E . F . E . A . O . C
Rail 2:  . . D . . . I . . . V . . . . . D . . . . . N . . .

Ciphertext: WECRLTE + EARDSOEEFEEAOC + DIVDN = WECRLTEERDSOEEFEAOCAIVDEN
```

#### Shembuj ekzekutimi

```
$ python algorithms/rail_fence.py

=======================================================
  Rail Fence Cipher – Demonstration
=======================================================

Rails     : 3
Plaintext : 'WEAREDISCOVEREDFLEEATONCE'
Encrypted : 'WECRLTEERDSOEEFEAOCAIVDEN'
Decrypted : 'WEAREDISCOVEREDFLEEATONCE'  ✓

Rails     : 2
Plaintext : 'HELLO'
Encrypted : 'HLOEL'
Decrypted : 'HELLO'  ✓

Rails     : 4
Plaintext : 'CRYPTOGRAPHY'
Encrypted : 'CGRORYYTAHPP'
Decrypted : 'CRYPTOGRAPHY'  ✓

Rails     : 3
Plaintext : 'A'
Encrypted : 'A'
Decrypted : 'A'  ✓

Rails     : 2
Plaintext : ''
Encrypted : ''
Decrypted : ''  ✓

Rails     : 10
Plaintext : 'ABCDE'
Encrypted : 'ABCDE'
Decrypted : 'ABCDE'  ✓
```

#### Përdorimi programatik

```python
from algorithms.rail_fence import RailFenceCipher, rail_fence_encrypt, rail_fence_decrypt

# Me klasë
cipher = RailFenceCipher(rails=3)
ciphertext = cipher.encrypt("HELLO WORLD")
plaintext  = cipher.decrypt(ciphertext)

# Me funksione
enc = rail_fence_encrypt("HELLO", rails=2)   # → 'HLOEL'
dec = rail_fence_decrypt("HLOEL", rails=2)   # → 'HELLO'
```

#### Rastet kufitare (Edge Cases)

| Situata | Sjellja |
|---------|---------|
| Tekst bosh `""` | Kthen `""` |
| Karakter i vetëm | Kthen të njëjtin karakter |
| `rails >= len(text)` | Round-trip funksionon, cipher ≈ plaintext |
| `rails < 2` | Gjeneroi `ValueError` |
| Karaktere speciale / unicode / hapësira | Trajtohen normalisht |

---

### 2. Morse Code *(Anëtar — )*

#### Përshkrimi

**Morse Code** është një metodë enkodimi që përfaqëson karakteret (germa dhe shifra) si sekuenca pikash (`.`) dhe vizave (`-`). U zhvillua në shekullin XIX për telekomunikim dhe mbetet standardi ndërkombëtar për komunikim emergjent.

Çdo karakter ka kodin e tij unik. Fjalët ndahen me hapësira të veçanta (`/`), ndërsa karakteret ndahen me hapësira të thjeshta.

**Çelësi:** Tabela fiks ndërkombëtare — nuk ka çelës sekret.
**Siguria:** Zero — është enkodim, jo kriptografi. Çdokush me tabelën mund ta dekodojë.

#### Shembuj ekzekutimi

```
$ python algorithms/morse_code.py

Input  : 'HELLO WORLD'
Encoded: '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
Decoded: 'HELLO WORLD'  ✓

Input  : 'SOS'
Encoded: '... --- ...'
Decoded: 'SOS'  ✓
```

---

### 3. Homophonic Substitution Cipher *(Anëtar — )*

#### Përshkrimi

**Homophonic Substitution Cipher** është një shifër substitucioni ku çdo karakter i plaintextit mund të mapohet te **shumë simbole** të ndryshme të ciphertekstit (homofone). Karakteret me frekuencë të lartë (si `E`, `T`, `A`) marrin më shumë homofone, duke e bërë analizën e frekuencës shumë më të vështirë.

**Çelësi:** Tabela e mapimit (plaintext karakter → listë homofone).
**Siguria:** Shumë më e fortë se substitucioni i thjeshtë — reziston analizës së frekuencës. Megjithatë, sulmohet ende me metoda statistikore moderne.

#### Shembuj ekzekutimi

```
$ python algorithms/homophonic.py

Plaintext : 'HELLO'
Encrypted : '47 91 23 23 05'   (homofone të rastit)
Encrypted : '12 56 67 67 88'   (ekzekutim tjetër — ndryshon!)
Decrypted : 'HELLO'  ✓
```

---

## Rezultatet e testeve

```
$ python -m pytest tests/ -v

tests/test_rail_fence.py::TestEncryption::test_classic_3_rails          PASSED
tests/test_rail_fence.py::TestEncryption::test_2_rails_hello             PASSED
tests/test_rail_fence.py::TestEncryption::test_2_rails_abcde_clean       PASSED
tests/test_rail_fence.py::TestEncryption::test_4_rails                   PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip[HELLO-2]        PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip[HELLO-3]        PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip[CRYPTOGRAPHY-4] PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip_with_spaces     PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip_symbols         PASSED
tests/test_rail_fence.py::TestRoundTrip::test_round_trip_unicode         PASSED
tests/test_rail_fence.py::TestEdgeCases::test_empty_string_encrypt       PASSED
tests/test_rail_fence.py::TestEdgeCases::test_single_character_encrypt   PASSED
tests/test_rail_fence.py::TestEdgeCases::test_rails_greater_than_length  PASSED
tests/test_rail_fence.py::TestEdgeCases::test_rails_exactly_2            PASSED
tests/test_rail_fence.py::TestEdgeCases::test_large_rails                PASSED
tests/test_rail_fence.py::TestInvalidInput::test_rails_less_than_2_raises PASSED
tests/test_rail_fence.py::TestInvalidInput::test_rails_zero_raises       PASSED
tests/test_rail_fence.py::TestInvalidInput::test_rails_negative_raises   PASSED
tests/test_rail_fence.py::TestConvenienceFunctions::test_encrypt_function PASSED
tests/test_rail_fence.py::TestConvenienceFunctions::test_round_trip_functions PASSED
tests/test_rail_fence.py::TestDeterminism::test_encrypt_is_deterministic PASSED
tests/test_rail_fence.py::TestRepr::test_repr                            PASSED
... (43 total)

================ 43 passed in 0.15s ================
```

---

## Autori

| Anëtar | Algoritmi | Skedarët |
|--------|-----------|----------|
| Anëtar 1 | Morse Code | `algorithms/morse_code.py`, `tests/test_morse_code.py` |
| Anëtar 2 | Homophonic Cipher | `algorithms/homophonic.py`, `tests/test_homophonic.py` |
| Anëtar 3 | Rail Fence Cipher | `algorithms/rail_fence.py`, `tests/test_rail_fence.py` |

---

## Licenca

Projekt akademik — Siguria e të Dhënave, 2024/2025.
