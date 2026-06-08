import random

woerter = [
    "KATZE", "HUND", "MAUS", "ELEFANT", "TIGER", "LAMA", "SCHAF", "PFERD", "ESEL",
    "BUCH", "TISCH", "STUHL", "LAMPE", "FENSTER", "SCHERE", "BLEISTIFT", "RUCKSACK",
    "HAUS", "WOHNUNG", "GARAGE", "KELLER", "BALKON", "GARTEN", "SCHLUESSEL",
    "KINDERGARTEN", "SCHULE", "KLASSENZIMMER", "LEHRER", "SCHUELER", "TAFEL",
    "WASSERFLASCHE", "PAUSENHOF", "TURNHALLE",
    
    "COMPUTER", "MAUSZEIGER", "BILDSCHIRM", "TASTATUR", "LAUTSPRECHER",
    "PROGRAMMIEREN", "ALGORITHMUS", "DATENBANK", "NETZWERK", "INTERNET",

    "SCHOKOLADE", "BONBON", "APFELKUCHEN", "ERDBEERE", "BANANE", "WASSERMELONE",
    "POMMES", "PIZZA", "SPAGHETTI", "GURKENSALAT",

    "AUTO", "FAHRRAD", "ROLLER", "BUS", "LASTWAGEN", "SCHIFF", "FLUGZEUG", "ZUG",

    "BERG", "FLUSS", "SEE", "WALD", "HOEHLE", "INSEL", "MEER", "STRAND",
    "REGEN", "SCHNEE", "GEWITTER", "SONNENSCHEIN", "NACHT", "TAGESLICHT",

    "ABENTEUER", "GEHEIMNIS", "SCHATZKARTE", "GESCHICHTE", "BUCHSTABE",
    "SPRACHE", "FREUNDSCHAFT", "GROSSZUEGIGKEIT", "HOEFE",
    
    "FUSSBALL", "BASKETBALL", "TISCHTENNIS", "SCHWIMMEN", "KLETTERN",
    "REITEN", "TURNEN", "SPRINGSEIL", "LAUFSTRECKE",

    "MUSIK", "GEIGE", "KLAVIER", "SCHLAGZEUG", "TROMPETE", "GITARRE", "LIEDTEXT",

    "ARZT", "KRANKENSCHWESTER", "KRANKENHAUS", "MEDIZIN", "SPRITZE",
    "THERMOMETER", "PFLASTER",

    "FERIEN", "GEBURTSTAG", "SOMMER", "WINTER", "FRUEHLING", "HERBST",
    "WEIHNACHTEN", "OSTERN", "SILVESTER",

    "ROBOTER", "SATELLIT", "RAKETE", "ASTRONAUT", "MONDLANDUNG",

    "KAMERAD", "FAMILIE", "GESCHWISTER", "COUSIN", "TANTE", "ONKEL",
    "GROSSMUTTER", "GROSSVATER",

    "HAMMER", "NAGEL", "SCHRAUBE", "WERKZEUG", "ZANGE", "SCHRAUBENZIEHER",
    "SAEGE", "BOHRMASCHINE",

    "WASCHMASCHINE", "KUEHLSCHRANK", "BACKOFEN", "GLOEHBIRNE",
    
    "THEATER", "SCHAUSPIELER", "KINO", "FILM", "TANZ", "KONZERT"
]

zufallwort = random.choice(woerter)

print("Willkommen bei Hangman!")
print("Das zufällige Wort hat", len(zufallwort), "Buchstaben.")

temp = []

for i in range(len(zufallwort)):
  temp.append("_")

# Variable initialisieren
versuche = 8
benutzte_buchstaben = []

# Hauptspielschleife
while versuche > 0 and "_" in temp:
  print("\nAktueller Stand: ", " ".join(temp))
  print("Verbleibende Versuche:", versuche)
  print("Benutzte Buchstaben:", " ".join(benutzte_buchstaben))
  
  # Spieler gibt einen Buchstaben ein
  buchstabe = input("Rate einen Buchstaben: ").upper()
  # Prüfen, ob es ein gültiger Buchstabe ist
  if buchstabe == "" or len(buchstabe) != 1 or not buchstabe.isalpha():
      print("Bitte gib nur einen Buchstaben ein du Idiot.")
      continue
  
  if buchstabe in benutzte_buchstaben:
      print("Diesen Buchstaben hast du bereits benutzt du Trottel.")
      continue

  # Prüfen, ob der Buchstabe im Wort ist
  if buchstabe  in zufallwort:
    print("Richtig! Der Buchstabe ", buchstabe, " ist im Wort.")
 
    # Aktualisieren des temporären Wortes
    for index, char in enumerate(zufallwort):
      if char == buchstabe:
        temp[index] = buchstabe

  # Der Buchstabe ist nicht im Wort, neuer versuch
  else:
    print("Falsch! Der Buchstabe ", buchstabe, " ist nicht im Wort.")
    versuche -= 1  # Versuch abziehen bei richtigem Buchstaben
   

  # Buchstabe zu den benutzten Buchstaben hinzufügen
  if buchstabe not in benutzte_buchstaben:
    benutzte_buchstaben.append(buchstabe)

# Spielende
if "_" not in temp:
  print(f"\nGlückwunsch! Du hast das Wort '{zufallwort}' erraten!")
  
else:
  print(f"\nLeider hast du keine Versuche mehr. Das Wort war '{zufallwort}'.") 