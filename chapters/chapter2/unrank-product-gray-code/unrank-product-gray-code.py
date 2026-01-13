def unrank_product_gray_code(the_number, the_maxima):
    """Das Unranking für den Gray-Code eines cartesischen Produkts:
    Liefere für gegebenes Zahl the_number das entsprechende Tupel in
    der Aufzählung, die durch product_gray_code erzeugt wird."""
    dim = len(the_maxima)
    the_tuple = np.zeros(dim, dtype=int)
    for i in range(dim-1,-1,-1):
        the_tuple[i] = the_number % the_maxima[i]
        the_number//= the_maxima[i]
        if the_number % 2:
            the_tuple[i] = the_maxima[i] - the_tuple[i] - 1
    return the_tuple

