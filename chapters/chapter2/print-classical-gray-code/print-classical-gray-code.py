def print_classical_gray_code(the_width):
    """Print a (classical) Gray code of width the_width"""
    for dum in classical_gray_code(2**the_width):
        char_func = set_to_characteristic_function(dum,the_width)
        # Der Datentyp string hat eine "member function" join,
        # die eine Liste von strings "aneinanderhängt", mit dem
        # "aufrufenden Objekt" (hier der leere String "") als
        # "Verbindungs-String". Z.B. liefert
        #    "*".join(['a','b','c'])
        # den String
        #    "a*b*c".
        binary_string = "".join([str(i) for i in char_func])
        print(binary_string)

