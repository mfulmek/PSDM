def adjacency_matrix_from_edge_set(n, edges):
    """Erzeuge die Adjazenzmatrix eines Graphen mit n Knoten
    und vorgegebener Kantenmenge"""
    am = np.zeros(n**2, dtype=int).reshape((n,n))
    for i,j in edges:
        modify_edge(am, i, j)
    return am

