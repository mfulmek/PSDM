def unrank_johnson_trotter(num,n):
    """Berechne die Permutation von {1,2,...,n} mit Nummer n in der
    Auflistung mit dem Johnson-Trotter-Algorithmus."""
    # num muß zwischen 0 und n!-1 liegen:
    if num < 0 or num >= factorial(n):
        print("Sehr lustig ....")
        return []

    # Initialisiere Rückgabewert pi
    pi = [0]*n
    # Startwert für Rückgabewert "Liste b"
    # list_b = [0]*n
    # Hilfsgrößen P, R, C
    P = num
    for j in range(n,0,-1):
        R = P % j
        P = P // j
        # list_b[j-1] = R
        if P % 2 == 1:
            k = 0
            direction = 1
        else:
            k = n+1
            direction = -1
        
        C = 0
        while True:
            k = k + direction
            if pi[k-1] == 0:
                C+= 1
            if C > R:
                break
        pi[k-1] = j
        
    return pi # , list_b

