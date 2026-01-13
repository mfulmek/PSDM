def unrank_colex_subsets(num, k):
    """Bestimme die Teilmenge num in der colex-Aufzählung
    aller k-elementigen Teilmengen: Das Lustige ist, daß wir
    hier nicht angeben müssen, von welcher Obermenge wir
    die Teilmengen betrachten!"""
    subset = [0]*k
    for i in range(k,0,-1):
        # Nummer num=0 ist sofort klar: Die Positionen
        # 0 bis i-1 werden mit 1,2,...,i belegt!
        if num == 0:
            subset[:i] = [j for j in range(1,i+1)]
            return subset
        # Implicit else: Suche die größte Zahl p sodaß binom(p,i) <= num.
        p = i
        # Die eingebaute Funktion binom (aus Modul scipy.special) liefert
        # float-Werte; wir wandeln das in integer um:
        binko = int(binom(p,i))
        while True:
            p+=1
            # binom(p+1,i) = binom(p,i)*(p+1)//(p-i); hier wieder
            # _ganzzahlige_ Division, also "//" statt "/" !
            newbinko = (binko*p)//(p-i)
            if newbinko > num:
                 # ... update num ...
                num-= binko
                # ... Element i (index i-1 in Python!) ist p
                subset[i-1] = p
                break
            else:
                binko = newbinko

    return subset

