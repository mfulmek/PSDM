def estimate_average_length_integer_partitions(n,N):
    """Beispiel für Monte--Carlo--Simulation: Schätze durchschnittliche
    Länge der Zahlpartitionen von n durch Bestimmung der mittleren Länge
    von N zufällig gewählten Zahl--Partitionen."""
    sum_of_lengths = 0.0
    for i,pi in enumerate(random_integer_partitions(n)):
        sum_of_lengths += len(pi)
        if i == N-1:
            break
    
    print(f'Zahlpartitionen von {n} haben {sum_of_lengths/N} Teile')
    print(f'im Durchschnitt (geschätzt aus Random--Sample der Größe {N}).')

