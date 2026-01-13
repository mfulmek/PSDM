# ACHTUNG:
dummy = ['a', 'b', 'c']
# Der folgende Befehl erzeugt einfach eine weitere _Bezeichnung_
# (englisch: reference) für dieselbe Liste "dummy": 
handle = dummy
# Daher entfernt der folgende Befehl das Element 'b' aus
# der ursprünglichen Liste "dummy":
handle.remove('b')
# Die print-Funktion gibt ihre Argumente (hier: handle und dummy)
# einfach aus:
print(handle, dummy)

# Wenn tatsächlich eine _neue Kopie_ von Liste "dummy"
# erzeugt werden soll, muß man so vorgehen:
dummy = ['a', 'b', 'c']
handle = deepcopy(dummy)
# Der Name (reference) "handle" bezeichnet nun eine _neue Kopie_,
# der folgende Befehl läßt die ursprüngliche Liste also unverändert:
handle.remove('b')
print(handle, dummy)
