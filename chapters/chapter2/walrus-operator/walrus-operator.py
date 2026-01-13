# Die folgende (auskommentierte) Zeile wäre ein Syntax-Fehler ...
# print(f'Der Ausdruck ergibt "(a = 2) > 7)" ergibt den Wert {(a = 2) > 7}')
# ... denn die _Zuweisung_ "a=2" ergibt keinen Wert (d.h., im Python-Code
# "(a=2) > 7" steht links von ">" einfach _nichts_).
# Der "Walross-Operator ":=" funktioniert "wie eine Zuweisung", ergibt aber
# einen Wert (nämlich das, was rechts von ":=" steht):
print(f'Der Ausdruck ergibt "(a:= 2) > 7)" ergibt den Wert {(a:= 2) > 7}')
print(f'Denn die Zuweisung "a:= 2" mit Walross-Operator ":=" ...')
print(f'... ERGIBT den Wert {(a:= 2)}')
