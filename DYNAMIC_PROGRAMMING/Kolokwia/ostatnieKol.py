def orchard(T, m):
    n = len(T)
    INF = float('inf')

    # Tworzymy tablicę DP o wymiarach (n+1) x m, wypełnioną nieskończonościami
    dp = [[INF] * m for _ in range(n + 1)]

    # Inicjalizacja: dla 0 drzew reszta 0 wymaga 0 wyciętych drzew
    dp[0][0] = 0

    # Iterujemy po każdym drzewie
    for i in range(n):
        for j in range(m):
            if dp[i][j] != INF:  # Jeśli stan dp[i][j] jest osiągalny
                # 1. Nie wycinamy drzewa - dodajemy jabłka z i-tego drzewa do sumy
                new_mod = (j + T[i]) % m
                dp[i + 1][new_mod] = min(dp[i + 1][new_mod], dp[i][j])

                # 2. Wycinamy drzewo - ignorujemy jabłka z i-tego drzewa, ale zwiększamy licznik wyciętych drzew
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)

    # Wynik znajduje się w dp[n][0] - minimalna liczba drzew do wycięcia, aby suma była podzielna przez m
    return dp[n][0] if dp[n][
                           0] != INF else n  # Jeśli nie znaleziono rozwiązania, zwracamy n (maksymalna liczba drzew do wycięcia)


# Przykład
T = [2, 2, 7, 5, 1, 14, 7]
m = 7
print(orchard(T, m))
