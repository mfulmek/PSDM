def perm_mul(sigma, tau):
    """Berechne die Permutation sigma(tau), dargestellt als _Listen_
    (d.h.: in Einzeilen-Notation)"""
    #@ Wir codieren Permutationen einfach als (geordnete) Listen: Das ist
    #@ sicherlich die nächst\-lie\-gen\-de Codierung, allerdings muß man dabei
    #@ bedenken, daß die Indizierung von Listen in Python \EM{bei Null}
    #@ beginnt!
    # Permutationen sind als _Listen_ dargestellt; die Indizierung
    # von Listen beginnt bei 0 (nicht bei 1!):
    return [sigma[tau_i-1] for tau_i in tau]

