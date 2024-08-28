from egzP1atesty import runtests 
from math import inf
def titanic( W, M, D ):
    #tutaj proszę wpisać własną implementację
    n = len(W)
    Word_in_morse = ''

    for i in range(n):
        Word_in_morse += M[ord(W[i]) - 65][1]

    m = len(Word_in_morse)
    # Tablica dynamiczna - DP[i] przechowuje minimalną liczbę liter, która koduje Word_in_morse[0:i+1]
    DP = [inf] * (m + 1)
    DP[0] = 0  # Początkowa wartość, brak liter na początku

    # Przeszukiwanie dynamiczne
    for i in range(1, m + 1):
        for j in range(max(0, i - 4),i):
            # Sprawdź, czy podciąg Word_in_morse[j:i] jest w słowniku Morse'a
            morse_fragment = Word_in_morse[j:i]
            for k in range(len(D)):
                if M[D[k]][1] == morse_fragment:
                    DP[i] = min(DP[i], DP[j] + 1)
                    break

    return DP[m] if DP[m] != inf else -1  # Jeśli nie da się zakodować, zwróć -1

runtests ( titanic, recursion=False )