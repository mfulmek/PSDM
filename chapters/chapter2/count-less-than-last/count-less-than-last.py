def count_less_than_last(pi):
    """Hilfsfunktion: Wieviele Element der Liste sind echt kleiner als ihr
    letztes Element"""
    return sum([1 if pi_i < pi[-1] else 0 for pi_i in pi[:-1]])

