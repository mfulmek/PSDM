def parabolic_intersections(p1, p2, h):
    """Return the x-coordinates of the (two, in general) intersections
    of parabolas with focus/directrix (p1,y=h) and (p2,y=h):"""
    a,b = p1
    c,d = p2
    if b < h or d < h:
        print(f'Invalid input: {p1}, {p2} are not both above line y = {h}.')
        return None
    
    if d == h:
        # In this case, the parabola is degenerate: A vertical ray starting
        # upwards in (c,d).
        return [c]*2

    if b == h:
        # In this case, the parabola is degenerate: A vertical ray starting
        # upwards in (a,b).
        return [a]*2

    if b == d:
        # In this case, there is only _one_ point of intersection:
        return [(a+c)/2]*2
    
    # Implicit else: We expect _two_ points of intersection!
    discriminant = ((a-c)**2 + (b-d)**2)/((b-h)*(d-h))
    sqareroot_with_factor = (d-h)*np.sqrt(discriminant)
    c1, c2 = c - sqareroot_with_factor, c + sqareroot_with_factor
    
    # Return the x-coordinates of the (two) points of intersection:
    return sorted([((a*(h-d) + (b-h)*cc)/(b-d)) for cc in [c2, c1]])

