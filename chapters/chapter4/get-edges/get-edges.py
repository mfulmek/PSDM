def get_edges(am):
    """Rekonstruiere die Kantenmenge eines Graphen aus seiner
    (quadratischen und symmetrischen!) Adjazenzmatrix;
    retourniere diese in einer Liste."""
    # Anzahl der Knoten:
    n = am.shape[0]
    # Liste der bereits identifizierten Kanten:
    edges = []
    for i in range(n-1):
        for j in range(i+1,n):
            if am[i][j]:
                edges+= [(i,j)]
    return edges

