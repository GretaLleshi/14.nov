domanda = str(input("Vuoi calcolare il perimetro di una figura? si/no "))
while domanda == "si":
    figura =str(input("Inserisci una tra le seguenti figure: [quadrato], [rettangolo], [cerchio]: "))
    if figura == "quadrato":
        lato = float(input("Inserisci il lato del quadrato: "))
        perimetro = 4 * lato
        print(f"Il perimetro è {perimetro}: ")
        domanda2 = str(input("Vuoi anche calcolare l'area? si/no "))
        if domanda2 == "si":
            area = lato * lato
            print(f"L'area è: ", area)
    elif figura == "rettangolo":
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = (2 * base) + (2 * altezza)
        print(f"Il perimetro è {perimetro}: ")
        domanda2 = str(input("Vuoi anche calcolare l'area? si/no "))
        if domanda2 == "si":
            area = base * altezza
            print(f"L'area è: ", area)
    else:
        raggio =float(input("Inserisci il raggio del cerchio: "))
        perimetro = 2 * 3.14 * raggio
        print(f"La circonferenza è {perimetro}: ")
        domanda2 = str(input("Vuoi anche calcolare l'area? si/no "))
        if domanda2 == "si":
            area = raggio * raggio * 3.14
            print(f"L'area è: ", area)
    
    nuova_figura = str(input("Vuoi inserire un'altra figura? si/no "))
    if nuova_figura == "no":
        print("Fine programma")
        break
