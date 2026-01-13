def find_spanning_tree(am):
    """Finde einen spannenden Baum: Umsetzung des Algorithmus."""
    n = am.shape[0]
    edges = get_edges(am)
    
    S = []
    T = adjacency_matrix_from_edge_set(n, S)
    
    loc = get_components(T)
    while len(loc) > 1:
        connectors = get_connecting_edges(loc, edges)
        if connectors:
            i,j = edges[connectors[0][0]]
            modify_edge(T,i,j)
            S+= [(i,j)]
        else:
            print('Graph ist nicht zusammenhängend!')
            return
        loc = get_components(T)
    return S,T

