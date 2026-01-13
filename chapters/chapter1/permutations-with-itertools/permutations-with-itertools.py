def permutations_with_itertools(the_list):
    """Verwende die Python-Bibliotheksfunktion itertools.permutations()
    zur Erzeugung aller Permutationen der Liste the_list. - Nicht wundern:
    Statt einer Liste  kann man auch einen String als Argument übergeben,
    denn Strings _funktionieren_ genauso wie Listen in puncto Indizierung
    und Slicing."""
    #@ In Python ist die Erzeugung aller Permutationen (wie so viele andere
    #@ nützliche Algorithmen und Routinen auch) bereits in einem Modul
    #@ (\verb|itertools|) ausprogrammiert, das man nur importieren muß:
    #@ Die Funktion \verb|itertools.permutations| ist ein sogenannter
    #@ \EM{Generator}, sie liefert als Ergebnis einen \EM{Iterator}, also
    #@ (salopp gesprochen) ``ein Konstrukt, über das man eine Schleife
    #@ laufen lassen kann''.
    for pi in itertools.permutations(the_list,len(the_list)):
        print(pi)

