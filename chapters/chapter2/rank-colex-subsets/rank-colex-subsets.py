def rank_colex_subsets(subset, k=None):
    r"""Der Parameter k ist hier an sich überflüssig - es muß ja "implizit"
    k = len(subset) gelten -, wir geben ihn hier aber dazu, damit wir
    unseren "generischen rank/unrank-Test" verwenden können.
    Das Ranking basiert auf der Beobachtung:
    rank([v_1,\dots,v_k]) = #(k-Teilmengen von {1,...,v_k-1})
    PLUS rank([v_1,\dots,v_{k-1}])"""
    # Die eingebaute Funktion binom (aus Modul scipy.special) liefert
    # float-Werte; die Summe dieser Werte ist daher auch vom Typ float:
    # Wir wandeln sie also in Datentyp int um.
    return int(sum([binom(v_k-1,k+1) for k,v_k in enumerate(subset)]))

