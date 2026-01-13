def convex_hull_slow(lop, epsilon=10 ** (-8)):
    """Bestimme die Eckpunkte des Polygons, das die konvexe Hülle der
    Punktliste lop darstellt (geordnet im mathematisch positiven
    Umlaufsinn). Um numerische Ungenauigkeiten abzufangen, setze epsilon
    auf einen kleinen Wert > 0."""
    #@ Wir bestimmen die konvexe Hülle einer (endlichen) Menge von
    #@ Punkten als jenes konvexe \EM{Polygon}, in dessen abgeschlossenen
    #@ Inneren alle Punkte liegen, durch einen einfachen geometrischen
    #@ Algorithmus.
    arrows = dict()
    for i,p_i in enumerate(lop):
        for j,p_j in enumerate(lop[i+1:], start=i+1):
            # Trägergerade der Punkte p_i, p_j
            t_g = PlaneLine(p_i,p_j)
            
            # Zähle die Punkte von lop, die "schwach links" bzw.
            # "schwach rechts" von der Trägergeraden liegen:
            count_left = count_right = 0
            for k,q in enumerate(lop):
                # Setze Punkt q in die Geradengleichung ein:
                eval_q = t_g.eval_equation(q)
                if eval_q > epsilon:
                    # Punkt liegt links:
                    count_left+=1
                elif eval_q < -epsilon:
                    # Punkt liegt rechts:
                    count_right+=1
                else:
                    # Punkt liegt auf der Geraden - aber liegt er auch
                    # zwischen p_i und p_j
                    proj = np.inner(t_g.v_v, q - p_i)
                    if -epsilon<=proj and proj<=get_norm(p_j-p_i)+epsilon:
                        count_left+=1
                        count_right+=1

            # Wenn alle Punkte auf einer Seite der Trägergeraden
            # oder auf der Verbindungsstrecke von p_i, p_j liegen,
            # dann ist die Kante p_i, p_j Teil des konvexen Hüll-Polygons:
            if count_right == len(lop):
                arrows[j] = i
            if count_left == len(lop):
                arrows[i] = j

    # Bringe die Eckpunkte in die richtige Reihenfolge:
    start = list(arrows.keys())[0]
    corners = [start]
    for i in range(len(arrows)-1):
        new = arrows[start]
        corners+= [new]
        start = new
    
    return corners

