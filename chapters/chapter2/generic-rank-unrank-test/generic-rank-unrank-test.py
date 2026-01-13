def generic_rank_unrank_test(
    description,
    rank_func,
    unrank_func,
    cardinality
):
    """Ein einfacher (aber gründlicher;-) _generischer_ Test,
    ob das Ranking/Unranking richtig funktioniert: description ist
    eine Variable, die den Ranking/Unranking-Funktionen rank_func
    und unrank_funk übergeben wird, und cardinality ist die Anzahl
    der erzeugten Objekte."""
    # Schleife über alle Zahlen, die als Rang eines description-Objekts
    # auftreten (sollen):
    for i in range(cardinality):
        # Es müßte "rank o unrank = identität" gelten - wenn nicht, geben
        # wir eine Fehlermeldung aus:
        if i != rank_func(unrank_func(i,description),description):
            print(f'Oops: Fehler für {description} bei Nummer {i}!')
            return False
    
    print(f'Ok: (rank o unrank) = identity gilt für {description}!')
    return True

