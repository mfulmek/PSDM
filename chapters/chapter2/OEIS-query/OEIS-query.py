def OEIS_query(sequence, n=5):
    """Abfrage der OEIS-Datenbank"""
    #@ Die \EM{Online Ecyclopedia of Integer Sequences} ist eine
    #@ nützliche Quelle, um (noch) ``unbekannte'' Folgen ganzer
    #@ Zahlen zu identifizieren. Man kann entsprechende Anfragen
    #@ natürlich manuell in einem Web--Browser eingeben, aber
    #@ wir illustrieren hier einmal die Internet--Fähigkeiten von
    #@ Python.

    # Eine "lokale" Klasse, die sich um die Antwort aus dem Internet
    # kümmert:
    class ResponseManager:
        def __init__(self):
            self.contents = ""
        def callback(self, buf):
            # Das Internet liefert einen "Byte-String", den wir
            # in einen "normalen" String decodieren (UTF-8 ist
            # ein sehr gebräuchliches Format zum Codieren von
            # Texten):
            self.contents += buf.decode('utf-8')

    # Zusammenstellen der HTML-Anfrage
    querystr = "http://oeis.org/search?q="
    querystr += ",".join([str(x) for x in sequence])
    querystr += "&n=" + str(n) + "&fmt=text"

    # Anfrage absetzen, Antworten speichern
    t = ResponseManager()
    c = pycurl.Curl()
    c.setopt(c.URL, querystr)
    c.setopt(c.WRITEFUNCTION, t.callback)
    c.perform()
    c.close()

    # Antwort zurückgeben (In Form eines Strings)
    return t.contents

