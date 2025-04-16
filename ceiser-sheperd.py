# Todo: Lägg till svenska symboler
# Todo: Lägg till siffror
# Todo: Lägg till tvåsiffriga nycklar
# Todo: Lägg till interaktivt val av nyckel



def main():
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789"
    MODE = ""
    KEY = 0
    
    # Välj krypterings- eller dekrypteringsläge
    while True:
        val = input('Välj 1 för "Enkrypt" eller 2 för "Dekrypt" och tryck på enter för att fortsätta: ').lower()

        if val.startswith("1"):
            MODE = 'encrypt'
            break
        elif val.startswith("2"):
            MODE = 'decrypt'
            break
        else:
            print("Ogiltigt val. Försök igen.")

    # Ange nyckel
    while True:
        print("Ange din nyckel (Du kan ange valfritt heltal):")
        val = input("Din val of nyckel: ")

        if not val.isdigit():
            print("Ogiltigt val. Ange endast siffror.")
            continue

        KEY = int(val)
        break

    # Ange meddelande
    print("Ange meddelande:")
    meddelande = input("> ").upper()

    # Bearbeta meddelandet
    c_meddelande = ""
    for m in meddelande:
        if m in SYMBOLS:
            nummer = SYMBOLS.find(m)

            if MODE == "encrypt":
                nummer += KEY
            elif MODE == "decrypt":
                nummer -= KEY
                
# I have tried while loops to handle the bigger keys and i see it more clearer than using modulo.
# but i thought its good to have both of them in mind.    
         
            while nummer >= len(SYMBOLS):
                nummer -= len(SYMBOLS)
            while nummer < 0:
                nummer += len(SYMBOLS)

# I even tried with using modulo, which worked pretty fine and it can handle the bigger keys. 
# But lacks readibility and i had to understand the whole process of how it works.

            # nummer %= len(SYMBOLS)
            c_meddelande += SYMBOLS[nummer]
        else:
            c_meddelande += m

    # Skriv ut resultat
    print("\nOriginal:", meddelande)
    print("Resultat:", c_meddelande)

# Programstart
if __name__ == "__main__":
    print(
        
        "Välkommen till Caesar Cipher!\n\n"
        "# Detta program krypterar och dekrypterar meddelanden med Caesar Cipher.\n"
        "# Du kan välja mellan att kryptera eller dekryptera ett meddelande.\n"
        "# Du ska också välja en nyckel för att kryptera eller dekryptera meddelandet.\n"
        "# Nyckeln är ett heltal som anger hur många positioner varje tecken ska flyttas i symboluppsättningen.\n"
        "# Till exempel, om nyckeln är 3, kommer A att bli D, B blir E och C blir F. Vid dekryptering sker det motsatta.\n"
    )
    input("Tryck på enter för att fortsätta...\n")
    
while True:
    main()
    Restart = input("\nVill du köra om programmet? (JA/NEJ): ").upper()
    if Restart != "JA":
        print("Tack för att du använde Caesar Cipher! ")
        break
