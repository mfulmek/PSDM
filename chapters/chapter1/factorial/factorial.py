def factorial(n):
    """Berechne n! _rekursiv_"""
    #@ Diese Funktion ruft \EM{rekursiv} sich selbst auf: Das ist jedenfalls möglich;
    #@ diese Programmierung ist zwar sehr gut verständlich, aber ganz und gar nicht
    #@ optimal in bezug auf Rechenzeit und Speicherverbrauch.
    if n == 0 or n == 1:
        return 1
    else:
        # Hier ruft sich die Funktion "rekursiv selbst auf":
        return n*factorial(n-1)

