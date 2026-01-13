def invert_pi(pi):
    """Sei pi = [pi_1, ..., pi_n] eine Permutation der ersten n
    natürlichen Zahlen, codiert in Einzeilen-Notation (Achtung: Das
    "Indizieren" in einer Liste beginnt bei 0): Berechne pi^(-1) (in
    derselben Einzeilen-Notation)."""
    #@ Die Inverse zu einer Permutation $\pi$ ist einfach die Umkehrabbildung:
    #@ In unserer Python--Umsetzung müssen wir wieder zu bedenken, daß die Indizierung
    #@ von Listen \EM{bei Null} beginnt!
    # Umkehrfunktion ist einfach:
    for i,pi_i in enumerate(pi, start = 1):
        # Indizierung beginnt bei Null - nicht vergessen!
        inverse[pi_i-1] = i
    return inverse

