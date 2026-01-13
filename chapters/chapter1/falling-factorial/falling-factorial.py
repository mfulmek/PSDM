def falling_factorial(n,k):
    """Berechne fallende Faktorielle:"""
    #@ Diese Funktion berechnet die fallenden Faktoriellen \EM{ohne Rekursion}:
    #@ In einem Ju\-py\-ter--No\-te\-book kann man durch die Kommandos
    #@ \begin{center}
    #@ \verb|%timeit factorial(10)| bzw.\ \verb|%timeit falling_factorial(10, 10)|
    #@ \end{center}
    #@ sehen, daß die rekursive Funktion deutlich
    #@ langsamer ist. (Am schnellsten ist allerdings die Funktion numpy.math.factorial
    #@ aus der Numerik--Bibliothek numpy).
    if k > n:
        return 0
    else:
        ret = 1
        for factor in range(n-k+1,n+1):
        	# "ret*=factor" ist kurz für "ret = ret*factor"
            ret*= factor
    return ret

