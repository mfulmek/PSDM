def binomial(n,k):
    """Berechne den Binomialkoeffizienten"""
    # Achtung: Ganzzahlige Division mit "//", "/" würde float liefern!!!
    return falling_factorial(n,k)//falling_factorial(k,k)

