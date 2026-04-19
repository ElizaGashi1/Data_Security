DATA SECURITY – KRIPTIMI I TË DHËNAVE

Ky projekt implementon tre algoritme të ndryshme të kriptografisë:

Morse Code Cipher
Homophonic Substitution Cipher
Rail Fence Cipher

Qëllimi i projektit është të demonstrojë mënyra të ndryshme të enkriptimit dhe dekriptimit të tekstit.

Përdorimi i programit

Pas ekzekutimit shfaqet menuja:

1. Morse Code
2. Homophonic Cipher
3. Rail Fence Cipher
4. Exit
Zgjedh algoritmin me numër (1–3)
Pastaj fut tekstin për enkriptim/dekriptim


PËRSHKRIMI I ALGORITMEVE

🔷 1. Morse Code Cipher

Morse Code është një metodë e thjeshtë kriptimi ku çdo shkronjë zëvendësohet me kombinim pikash dhe vijash.

Përdoret për komunikim të hershëm (radio, sinjale)
Është algoritëm zëvendësimi (substitution cipher)

 Karakteristikë:

Një shkronjë → një kod Morse
Lehtë për t’u kuptuar, por jo i sigurt

🔷 2. Homophonic Substitution Cipher

Ky algoritëm është version më i avancuar i zëvendësimit.

Çdo shkronjë mund të zëvendësohet me shumë simbole të ndryshme
E bën më të vështirë analizën frekuenciale

Karakteristikë:

Më i sigurt se Morse
Përdor “key” për dekriptim në disa raste
Shpesh jep output të ndryshëm për të njëjtin tekst

🔷 3. Rail Fence Cipher

Ky është algoritëm transpozicioni.

Teksti shkruhet në formë zig-zag mbi disa “shina” (rails)
Pastaj lexohet rresht për rresht për të krijuar tekstin e enkriptuar

Karakteristikë:

Nuk ndryshon shkronjat, vetëm renditjen
Siguria varet nga numri i rails


SHEMBUJ EKZEKUTIMI:
1.Morse code
Input: Hello
Output: .... . .-.. .-.. ---

2.Homophonic Cipher
Input: Hello
Output: G7 X3 L9 L2 O5

3.Rail Fence Cipher
Input: Hello World
Output: HOLELWRDLO

Përfundim

Ky projekt demonstron tre teknika të ndryshme të kodimit dhe kriptimit të tekstit, duke ilustruar dallimin midis zëvendësimit dhe transpozimit, si dhe kodimit simbolik.
