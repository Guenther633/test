#print("Hallo Python")
# Kommentar um eine Zeile auszukommentieren oder Code zu erklären


def isfloatStr(parameter=""):
    try:
        number = float(parameter) # Versucht den String in eine Zahl umzuwandeln   
        return True
        
    except ValueError:
        print("Bitte eine gültige Zahl eingeben!")
        return False
    
def isoperator(parameter=""):
    if parameter in ['+', '-', '*', '/']:
        return True
    else:
        print("Bitte einen gültigen Operator eingeben (+, -, *, /)!")
        return False

def berechne(zahl1, zahl2, operator):
    if operator == '+':
        return zahl1 + zahl2
    elif operator == '-':
        return zahl1 - zahl2
    elif operator == '*':
        return zahl1 * zahl2
    elif operator == '/':
        if zahl2 != 0:
            return zahl1 / zahl2
        else:
            print("Fehler: Division durch Null ist nicht erlaubt.")
            return None
    else:
        print(f"Ungültiger Operator: {operator}")
        return None

print("Start des Programms")

while True:
    eingabe1 = input("Bitte Zahl 1 eingeben: ").replace(',', '.')
    if isfloatStr(parameter=eingabe1):
        zahl1 = float(eingabe1)
        break
    else:
        print("Ungültige Eingabe für Zahl 1. Bitte erneut versuchen.")

while True:
    eingabe2 = input("Bitte Zahl 2 eingeben: ").replace(',', '.')
    if isfloatStr(eingabe2):
        zahl2 = float(eingabe2)
        break
    else:
        print("Ungültige Eingabe für Zahl 2. Bitte erneut versuchen.")

while True:
    operator = input("Bitte Operator eingeben (+, -, *, /): ")
    if isoperator(operator):
        ergebnis = berechne(zahl1, zahl2, operator)
        break
    else:
        print("Ungültige Eingabe für Operator. Bitte erneut versuchen.")


if ergebnis is not None:
    print(f"Das Ergebnis von {zahl1} {operator} {zahl2} ist: {ergebnis}")

print("Ende des Programms")