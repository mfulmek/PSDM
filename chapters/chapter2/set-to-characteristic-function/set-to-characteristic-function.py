def set_to_characteristic_function(the_set, the_width):
    """Convert the_set (supposed to be a subset of
    [the_width] = {1,2,...,the_width}) to its characteristic
    function"""
    char_func = [0]*the_width
    for x in the_set:
        # Nicht vergessen: Indexierung beginnt bei 0.
        char_func[x-1] = 1
    return char_func

