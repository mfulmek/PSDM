# Illustration einer Schleife (for-loop) mit dem range-Befehl.
# Berechne 1*3*5*7*9
ergebnis = 1
print('Das Produkt 1', end='')
# "end=''" bedeutet: Kein "newline" (Zeilenumbruch) am Ende des Strings
for zahl in range(3,10,2):
    ergebnis *= zahl
    # Gleichbedeutend mit: ergebnis = ergebnis*zahl
    print(f'*{zahl}', end='')
    # Eine von vielen Möglichkeiten für einen "formatierten String"
# Die for-Schleife ist hier zu Ende:
print(f' ist gleich {ergebnis}.')
# Ohne end='' gibt print den String mit einem "newline" am Ende aus.
