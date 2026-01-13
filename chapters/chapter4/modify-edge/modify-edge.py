def modify_edge(am, i, j, entry=1):
    """Trage eine Kante in einer Adjazenzmatrix ein: Die Matrix
    soll _symmetrisch_ sein."""
    try:
        am[i][j] = am[j][i] = entry
    except IndexError:
        print(f'Indices ({i},{j}) nicht in {am.shape}!')

