def Przedzial(x, y,i):
    # x to tuple: (length, start, end)
    # y to tuple: (start, end)
    m, a1, b1 = x
    a2, b2 = y
    if a1 == -float('inf') and i !=1:
        return (-float('inf'), 0, 0)
    # Sprawdzenie czy przedziały się przecinają
    if a2 > b1 or a1 > b2:
        return (-float('inf'), 0, 0)  # Przypadek braku przecięcia

    # Obliczanie przecięcia przedziałów
    length = min(b1, b2) - max(a1, a2) + 1  # Dodajemy +1, bo przedziały są inkluzywne
    return (length, max(a1, a2), min(b1, b2))

def Kintersect(A, k):
    n = len(A)

    # DP[i][j] stores the maximum intersection length for the first i intervals and j selected intervals
    DP = [[(0, float('-inf'), float('inf'))] * (k + 1) for _ in range(n + 1)]
    parents = [[[] for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(k + 1, i + 1)):
            for l in range(i):
                # Oblicz wynik dla nowego przedziału
                result, a, b = Przedzial(DP[l][j - 1], A[i - 1],i)

                # Aktualizacja DP, jeśli nowy wynik jest lepszy
                if result > DP[i][j][0]:
                    DP[i][j] = (result, a, b)
                    parents[i][j] = parents[l][j - 1] + [i - 1]  # Przechowanie indeksu

            # Przeniesienie najlepszego wyniku bez uwzględnienia aktualnego przedziału
            if DP[i][j][0] < DP[i - 1][j][0]:
                DP[i][j] = DP[i - 1][j]
                parents[i][j] = parents[i - 1][j]

    return parents[n][k]  # Zwracamy listę indeksów

# Przykład użycia:
A = [(0, 4), (1, 10), (6, 7), (2, 8)]
k = 3
wynik = Kintersect(A, k)
print(wynik)  # Oczekiwany wynik: np. [0, 1, 3]
