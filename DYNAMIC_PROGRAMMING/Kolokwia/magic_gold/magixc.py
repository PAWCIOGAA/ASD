from egz2btesty import runtests

def magic(C):
    n = len(C)
    tab = [-1]*n
    tab[0] = 0
    for i in range(n):
        obecna_komnata = i
        posiadane_juz_zloto = tab[i]
        zloto_w_komnacie = C[i][0]
        for j in range(1,4):
            nowa_komnata = C[i][j][1]
            koszt_wejscia_do_nowej_komnaty = C[i][j][0]

            if nowa_komnata > obecna_komnata and tab[i] != -1 and zloto_w_komnacie -koszt_wejscia_do_nowej_komnaty <= 10:

                tab[nowa_komnata] = max(tab[nowa_komnata],posiadane_juz_zloto + min(10,(zloto_w_komnacie -koszt_wejscia_do_nowej_komnaty)))

    return tab[-1]




runtests( magic, all_tests = True )