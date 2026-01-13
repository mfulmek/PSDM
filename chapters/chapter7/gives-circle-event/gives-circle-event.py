def gives_circle_event(A, X, B):
    """Consider the three foci A, X, B of three consecutive arcs of
    a beachline: Is there a circle event affecting the "central" arc
    (with focus X)? If so, return the vertex and key corresponding
    to this event."""
    if np.inner(get_normalized_normal(X-A),B-X) >= 0:
        return None, None
    # Implicit else:
    bisector_ax = plane_line_bisector(A,X)
    bisector_bx = plane_line_bisector(X,B)
    vertex = get_intersection(bisector_ax, bisector_bx)[0]
    radius = get_norm(X-vertex)
    x,y = vertex
    key = y-radius
    # Return key (height where this event should be handled)
    # and center (vertex) _as a tuple_:
    return key, (x,y)

