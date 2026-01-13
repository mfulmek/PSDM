# Arrays (d.h.: Vektoren und Matrizen) mit numpy:
# Einfache Definition einer 2x2-Matrix, wo alle Einträge 0.0 sind: 
meine_matrix = np.zeros(4, dtype = float).reshape((2,2))
# Verändern der Einträge dieser Matrix:
meine_matrix[0][0] = 1
meine_matrix[0][1] = 2
meine_matrix[1][0] = 3
meine_matrix[1][1] = 4
print(meine_matrix)
# Alternative Definition einer 2x2-Matrix, Einträge hier Datentyp int:
# Zuerst wird der Vektor (1,2,3,4) der Länge 4 erzeugt, der dann in
# eine 2x2-Matrix "umgewandelt" wird (mit reshape):
meine_matrix = np.arange(1,5, dtype = int).reshape((2,2))
print(meine_matrix)
# Die "Dimensionen" einer Matrix erhält man wie folgt:
zeilen, spalten = meine_matrix.shape
print(f'Unsere Matrix hat {zeilen} Zeilen und {spalten} Spalten.')
# Multiplikation einer Matrix mit einem Vektor:
mein_vektor = np.arange(2, dtype = int) # kein "reshape" erforderlich! 
print('Multiplikation Matrix*Vektor:')
print(f'{meine_matrix}*{mein_vektor} = {meine_matrix.dot(mein_vektor)}')
print('Multiplikation Matrix*Matrix:')
print(f'{meine_matrix}*{meine_matrix} = {meine_matrix.dot(meine_matrix)}')
