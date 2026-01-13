def test_product_lex(the_maxima):
    """Eine einfacher (aber gründlicher;-) Test,
    ob das Ranking/Unranking richtig funktioniert"""
    # Python hat zwar eine eingebaute Funktion sum(), die die
    # Elemente einer Liste _aufsummiert_, aber keine analoge
    # Funktion prod() (jedenfalls nicht in Python-Versionen < 3.8),
    # die die Elemente einer Liste _aufmultipliziert_: Wir können
    # uns aber mit der ensprechenden numpy-Funktion behelfen.
    cardinality = np.prod(np.array(the_maxima, dtype=int))
    # Schleife über alle Zahlen von 1 bis zur Kardinalität des
    # cartesischen Produkts:
    for i in range(1, cardinality+1):
        # Es müßte "rank o unrank = identität" gelten - wenn nicht,
        # geben wir eine Fehlermeldung aus:
        if i != rank_product_lex(
            unrank_product_lex(
                i,
                the_maxima
            ),
            the_maxima
        ):
            # Eine der (mehreren!!) Arten, einen STRING (also eine
            # Kette von Buchstaben) _formatiert_ auszugeben: Was in
            # geschwungenen Klammern steht, wird durch die entsprechende
            # _string representation_ ersetzt.
            print(f'Fehler im kart. Produkt {the_maxima} bei Nummer {i}!')
            return False
    
    print(f'Alles bestens: (rank o unrank) = identity gilt für {the_maxima}!')
    return True

