def kd_tree(cloud):
    # cloud.shape[1] = Anzahl der Spalten, also gleich
    # Anzahl der Punkte: Wir betrachten hier die (unechte)
    # Teilmenge _aller_ Punkte.
    subset = np.ones(cloud.shape[1], dtype=bool)
    # Die Wurzel des so konstruierten Teilbaums wird
    # die Wurzel eines BinaryTree, den wir als Resultat
    # zurückgeben.
    return BinaryTree(kd_subtree(cloud, subset))

