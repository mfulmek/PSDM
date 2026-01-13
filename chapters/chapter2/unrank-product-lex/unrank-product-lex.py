def unrank_product_lex(the_number, the_maxima):
    """Bestimme aus der gegebenen Nummer (mit 1 beginnend)
    das entsprechende Tupel in der lexikographischen
    Auflistung des cartesischen Produkts
    [the_maxima[0]] x [the_maxima[1]] x ...
    """
    # Wie in der rank-Funktion ist es besser, "mit dem Zählen bei
    # Null zu beginnen":
    the_number-= 1
    # (Äquivalent: "the_number = the_number - 1".)
    
    # Wir beginnen mit dem leeren Tupel:
    the_tuple = []
    for divisor in the_maxima[::-1]:
        # Division mit Rest: a % b für zwei ganze Zahlen
        # a, b liefert a modulo b.
        integer_remainder = the_number % divisor
        # Wir bleiben (noch) bei der Gewohnheit, das Zählen
        # bei Eins zu beginnen:
        the_tuple = [integer_remainder + 1]+the_tuple
        # Das könnte man auch in eine Zeile zusammenfassen:
        # the_tuple = [the_number % divisor + 1]+the_tuple
        
        # ACHTUNG, würde man hier
        #    "the_number / divisor"
        # schreiben, dann erhielte man eine Fließkommazahl
        # (Datentyp float), also i.a. KEINE ganze Zahl!!!
        the_number = the_number // divisor
    
    return the_tuple

