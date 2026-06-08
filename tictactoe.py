def zeige_feld(feld):
    print(feld[0] + " | " + feld[1] + " | " + feld[2])
    print("---------")
    print(feld[3] + " | " + feld[4] + " | " + feld[5])
    print("---------")
    print(feld[6] + " | " + feld[7] + " | " + feld[8])
    print("\n")

def zeige_nummern():
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\n")

def hat_gewonnen(feld, spieler):
    gewinn_kombinationen = [
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # Reihen
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # Spalten
        {0, 4, 8}, {2, 4, 6}              # Diagonalen
    ]
    
    spieler_felder = set()
    for i, feld_inhalt in enumerate(feld):
        if feld_inhalt == spieler:
            spieler_felder.add(i)
    for kombination in gewinn_kombinationen:
        if kombination.issubset(spieler_felder):
            return True
    return False

def spiel():
    feld = [" "] * 9  # Leeres Brett: 9 Felder
    aktueller_spieler = "X"
    zuege = 0
    
    print("Willkommen bei Tic-Tac-Toe!")
    zeige_nummern()
    
    while zuege < 9:
        zeige_feld(feld)
        print(f"Spieler {aktueller_spieler}, wähle ein Feld (1-9): ")
        
        try:
            zug = int(input()) - 1  # Eingabe 1-9, Index 0-8
            if zug < 0 or zug > 8 or feld[zug] != " ":
                print("Ungültiger Zug! Feld ist belegt oder außerhalb des Bereichs.")
                continue
        except ValueError:
            print("Bitte eine Zahl zwischen 1 und 9 eingeben.")
            continue
        
        feld[zug] = aktueller_spieler
        zuege += 1
        
        if hat_gewonnen(feld, aktueller_spieler):
            zeige_feld(feld)
            print(f"Spieler {aktueller_spieler} hat gewonnen!")
            return
        
        # Spieler wechseln
        aktueller_spieler = "O" if aktueller_spieler == "X" else "X"
    
    zeige_feld(feld)
    print("Unentschieden!")

# Spiel starten
if __name__ == "__main__":
    spiel()
    