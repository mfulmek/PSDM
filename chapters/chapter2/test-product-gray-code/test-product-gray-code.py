def test_product_gray_code(the_maxima):
    # Erster Test: Haben zwei aufeinanderfolgende Tupel tatsächlich
    # Abstand 1 (in der 1-Norm)
    for i,t in enumerate(product_gray_code(the_maxima)):
        if i==0:
            v = np.copy(t)
        else:
            # Da alle Koordinaten von t-v GANZZAHLIG sind, ist die
            # 1-Norm von (t-v) genau dann gleich 1, wenn das für die
            # "normale" euklidische Norm gilt:
            if np.linalg.norm(t-v) != 1:
                print(f'Mist: 1-Norm von ({t} - {v}) ungleich 1!')
                return False
            # NICHT "v=t": Dann würde nämlich Variablen v und t auf
            # DASSELBE numpy-array verweisen!
            v[:] = t
    # Zweiter Test: Liefert der Gray-Code dieselben Tupel wie der
    # lexikographische Algorithmus
    return sorted([t for t in product_lex(the_maxima)]) == \
sorted([list(t+1) for t in product_gray_code(the_maxima)])

