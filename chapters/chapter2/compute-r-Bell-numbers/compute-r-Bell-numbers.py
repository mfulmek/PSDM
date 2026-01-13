def compute_r_Bell_numbers(nnn):
    """Berechne die r--Bell Zahlen, die bei der Bestimmung
    des Rangs einer Funktion von beschränktem Wachstum in
    lexikographischer Ordnung auftreten"""
    #@ Die Matrix, die wir hier berechnen, hat in der OEIS-Datenbank
    #@ Index A095148.
    # Vorbereitung der Matrix als numpy-array von ganzen Zahlen
    result = np.zeros(nnn**2, dtype=int).reshape((nnn,nnn))
    # Die letzte und vorletzte Zeile ergeben sich aus der
    # Anfangsbedingung der Rekurion
    result[-1] = 1
    result[-2][:-1] = np.arange(2,nnn+1)
    # Die übrigen Einträge bestimmen wir aus der Rekursionsgleichung
    for row in range(nnn-3,-1,-1):
        for col in range(row+1):
            new_b = (col+1)*result[row+1][col] + result[row+1][col+1]
            result[row][col] = new_b

    return result

