def rank_product_gray_code(the_tuple, the_maxima):
    """Das Ranking für den Gray-Code eines cartesischen Produkts:
    Liefere für gegebenes Tupel the_tupel die "Nummer" in der
    Aufzählung, die durch product_gray_code erzeugt wird.
    """
    rank = 0
    dim = len(the_tuple)
    for i in range(dim):
        if rank % 2:
            remainder = the_maxima[i] - the_tuple[i] - 1
        else:
            remainder = the_tuple[i]
        rank = rank*the_maxima[i] + remainder
    return rank

