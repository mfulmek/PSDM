def get_connecting_edges(list_of_components,list_of_edges):
    """Finde alle Kanten in der Menge list_of_edges, die
    zwei verschiedene Komponenten aus der Menge list_of_components
    verbinden:"""
    #@ Für eine Liste von Zusammenhangskomponenten suchen wir
    #@ alle Kanten aus einer Liste, die zwei Komponenten verbinden,
    #@ durch ``direktes Suchen'' und retournieren das Ergebnis
    #@ in Form einer Liste, die für jede Kante die verbundenen
    #@ Komponenten zeigt.
    result = []
    for na, a in enumerate(list_of_components[:-1]):
        for nb, b in enumerate(list_of_components[na+1:], start=na+1):
            for ne,(i,j) in enumerate(list_of_edges):
                if ((i in a) and (j in b) or (j in a) and (i in b)):
                    result+=[(ne,(na,nb))]
    return result

