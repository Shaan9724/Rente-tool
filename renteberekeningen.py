startkapitaal = 1000
rente = 0.05
while True:
    try:
        aantal_jaren = int(input("Voor hoeveel jaar wil je de eindwaarde weten? "))
        startkapitaal = 1000
        rente = 0.05
        if aantal_jaren < 0:
            print("Voer een positief getal in.")
            continue
    except ValueError:
        print("Ongeldige invoer. Voer een geheel getal in.")
    print(f"je startkapitaal is: €{startkapitaal:.2f}")
    eindwaarde = startkapitaal * (1 + rente) ** aantal_jaren
    print(f"de rente is: {rente * 100:.1f}%")
    print(f"Na {aantal_jaren} jaar is de eindwaarde: €{eindwaarde:.2f}")
    print(f"De totale rente die je ontvangt als je {aantal_jaren} jaar spaart: €{eindwaarde - startkapitaal:.2f}")
    if aantal_jaren > 10:
     print(f"je eindwaarde is: €{eindwaarde:.2f}")
     print("Dat is een lange periode, jij gaat rijk worden!") 
    elif aantal_jaren < 10:
     print(f"je eindwaarde is: €{eindwaarde:.2f}")
     print("je moet nog ff doorsparen als je veel geld wil hebben")
    else:
     print(f"je eindwaarde is: €{eindwaarde:.2f}")
     print("10 jaar is een mooie periode om te sparen, maar hoe langer je spaart hoe meer geld je krijgt!")

    print("")
    print("Wil je nog een keer de eindwaarde berekenen? (ja/nee)")
    antwoord = input("ja/nee: ").lower()
    if antwoord == "ja":
        print("")
        continue
    else:
        print("Bedankt voor het gebruiken van de rente berekeningstool. Tot ziens!")
    print("")     