def OEIS_parse(response):
    """Sehr einfacher 'Parser', der die Antwort der
    OEIS Datenbank verarbeitet"""
    #@ Die Antwort von OEIS besteht aus einem langen String, der
    #@ sehr einfach aufgebaut ist und aus dem man die Bedeutung
    #@ der Informationen rasch extrahieren kann.
    # Dictionary für unsere formatierte Ausgabe
    formatted_responses = dict()
    for line in response.split("\n"):
        # Die Zeilen, die wir verarbeiten wollen, beginnen alle mit "%"
        # und einem Buchstaben, der die Bedeutung der restlichen Zeile
        # bestimmt (siehe dictionary OEIS_PARSER); Achtung: Es kann auch
        # leere Zeilen geben!
        if not line or line[0] != '%':
            continue
        # Wir schauen uns den zweiten Buchstaben an:
        second_character = line[1]
        # Anstatt vorher zu schauen, ob dieser zweite
        # Buchstabe im dictionary OEIS_PARSER vorkommt,
        # probieren wir das einfach ...
        try:
            record = OEIS_PARSER[second_character]
            data = line[3:]
        # ... und "fangen" die Fehlermeldung ab, wenn's schiefgeht:
        except KeyError:
            continue
        if record == 'OEIS Index':
            # Wir basteln ein neues dictionary für die gefundene
            # Zahlenfolge, die mit data bezeichnet ist:
            OEIS_INDEX = data
            formatted_responses[OEIS_INDEX] = dict(
                zip(
                    OEIS_VALUES,
                    ['']*len(OEIS_VALUES)
                )
            )
            formatted_responses[OEIS_INDEX][record]+= OEIS_INDEX
        else:
            # Die ersten 8 Buchstaben sind der aktuelle OEIS_INDEX und
            # ein Space; die lassen wir weg:
            formatted_responses[OEIS_INDEX][record]+=(data[8:]+'\n')
            
    return formatted_responses

