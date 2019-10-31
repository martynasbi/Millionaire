import random

def ar_zaisti(start):
    beginning = 0
    while True:
        if start == str(beginning):
            atsakymas = input("\nAr norite pradėti žaidimą: TAIP / NE\n").upper()
        else:
            atsakymas = input("\nAr norite kartoti žaidimą: TAIP / NE\n").upper()
        if "T" in atsakymas:
            pradeti_zaidima()
        elif "N" in atsakymas:
            print ("\nIki. Lauksime Jūsų sugrįžtant!")
            exit()
        else:
            continue

def taisykles():
    
    print("********************************************************************************************************************************************")
    print("Sveiki atvykę į žaidimą \"Kas laimės milijoną?\"!\n\nŽaidimo metu Jums bus pateikta 10 klausimų ir 4 atsakymų variantai.")
    print("\nĮveikę pirmus 4 klausimus, Jūs užsitikrinsite 25 000 Eur laimėjimą, o įveikę pirmus 7 klausimus, užsitikrinsite net 180 000 Eur laimėjimą!")
    print(f"\nIš viso Jūs turite 3 bandymus. Išnaudojus visus bandymus, žaidimas bus baigtas.")
    print("********************************************************************************************************************************************")

def pradeti_zaidima():
    
    bandymu_skaicius = 3
    laimeta_suma = 0
    laimeti_kartai = 0
    klausimo_numeris = 0
     
    klausimynas_easy = [ { "klausimas": "Kas atstovauja indų kino meną?",
                           "atsakymas": "Bolivudas",
                           "atsakymai": ["Bolivudas",
                                         "Holivudas",
                                         "Golivudas",
                                         "Indivudas" ] },
                         
                         { "klausimas": "Kokios šalies veikėjas buvo Leninas?",
                           "atsakymas": "Rusijos",
                           "atsakymai": ["Rusijos",
                                         "Ukrainos",
                                         "Čekijos",
                                         "Gruzijos" ]},
                         
                         { "klausimas": "Kaip vadinama istorijos disciplina padedanti nustatyti įvykių eiliškumą ir datas?",
                           "atsakymas": "Chronologija",
                           "atsakymai": ["Chronologija",
                                         "Enkaustika",
                                         "Bonistika",
                                         "Paleografija" ]},
                         
                         { "klausimas": "Kaip vadinamas didžiausio ir mažiausio dydžio skirtumas?",
                           "atsakymas": "Amplitudė",
                           "atsakymai": ["Amplitudė",
                                         "Atogrąža",
                                         "Speigratis",
                                         "Brizas" ]}]

    klausimynas_medium = [ { "klausimas": "Kuris iš šių rašytojų ekspresionistas?",
                             "atsakymas": "Boruta",
                             "atsakymai": ["Boruta",
                                           "Simonaitytė",
                                           "Cvirka",
                                           "Mieželaitis" ] },
                           
                           { "klausimas": "Kurio romano autorius yra Viktoras Hugo?",
                             "atsakymas": "Vargdieniai",
                             "atsakymai": ["Vargdieniai",
                                           "Kaimiečiai",
                                           "Kalniečiai",
                                           "Turtuoliai" ]},
                           
                           { "klausimas": "Kaip paleontologijoje vadinami \"velnio nagai\"?",
                             "atsakymas": "Belemnitai",
                             "atsakymai": ["Belemnitai",
                                           "Amonitai",
                                           "Trilobitai",
                                           "Stalagmitai" ]}]

    klausimynas_hard = [ { "klausimas": "\"Šimtas zuikių susirinko, Net žalia girelė linko\". Kas poemėlės autorius?",
                           "atsakymas": "Eduardas Mieželaitis",
                           "atsakymai": ["Eduardas Mieželaitis",
                                         "Martynas Vainilaitis",
                                         "Kostas Kubilinskas",
                                         "Vytė Nemunėlis" ] },
                         
                         { "klausimas": "Kurioje valstybėje sesoto kalba yra valstybinė?",
                           "atsakymas": "Lesote",
                           "atsakymai": ["Lesote",
                                         "Somalyje",
                                         "Sesote",
                                         "Libijoje" ]},
                         
                         { "klausimas": "Kuris iš šių metalų netirpsta net \"karališkajame vandenyje\"?",
                           "atsakymas": "Iridis",
                           "atsakymai": ["Iridis",
                                         "Sidabras",
                                         "Auksas",
                                         "Platina" ]}]
    
    for klausimas in klausimynas_easy.copy():
        klausimynas_easy, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai = uzduoti_klausima(
            klausimynas_easy, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai)
    for klausimas in klausimynas_medium.copy():
        klausimynas_medium, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai = uzduoti_klausima(
            klausimynas_medium, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai)
    for klausimas in klausimynas_hard.copy():
        klausimynas_hard, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai = uzduoti_klausima(
            klausimynas_hard, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai)

def uzduoti_klausima(klausimynas, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai):
    
    laimimos_sumos = [1000, 3000, 6000, 15000, 30000, 50000, 75000, 130000, 250000, 440000]
    klausimo_numeriai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    atsakymu_raides = ["A", "B", "C", "D"]
    
    klausimas = (random.choice(klausimynas))
    klausimynas.remove(klausimas)
    pirmas_klausimas = klausimo_numeriai[klausimo_numeris]
    print(str(pirmas_klausimas) + ". " + klausimas["klausimas"])
    
    random_atsakymai = random.sample(klausimas["atsakymai"], len(klausimas["atsakymai"]))
    print("\nAtsakymų variantai:")

    for raide, atsakymas in zip(atsakymu_raides, random_atsakymai):
        print(f"{raide}. {atsakymas}")
    print()

    while True:
        
        while True:
            
            if bandymu_skaicius == 0:
                print("Jūs išnaudojote visus bandymus.\n")
                if laimeta_suma >= 180000:
                    laimeta_suma = 180000
                    print("************************************")
                    print(f"Jūs laimėjote {laimeta_suma} Eur. Sveikiname!")
                    print("************************************")
                    ar_zaisti(1)
                elif laimeta_suma >= 25000:
                    laimeta_suma = 25000
                    print("************************************")
                    print(f"Jūs laimėjote {laimeta_suma} Eur. Sveikiname!")
                    print("************************************")
                    ar_zaisti(1)
                else:
                    print("*****************************************")
                    print("Deja šį kartą Jūs nieko nelaimėjote.\n\nAčiū už dalyvavimą, bandykite kitą kartą!")
                    print("*****************************************")
                    ar_zaisti(1)
                    
            atsakymo_raide = input("Kai norėsite stabdyti žaidimą, pasirinkite: S.\nPasirinkite atsakymo variantą: A, B, C ar D.\n").upper()
            if atsakymo_raide in atsakymu_raides:
                
                atsakymas = random_atsakymai[ord(atsakymo_raide)-65]
                print("Jūs pasirinkote atsakymą:",atsakymas)
                break
                
            elif atsakymo_raide == "S":
                if laimeta_suma == 0:
                    print("*************************************************************************************************")
                    print(f"Jūs nusprendėte nebetęsti žaidimo. Deja šį kartą Jūs nieko nelaimėjote. Bandykite sekantį kartą.")
                    print("*************************************************************************************************")
                    ar_zaisti(1)
                else:
                    print("*********************************************************************************")
                    print(f"Jūs nusprendėte nebetęsti žaidimo. Jūs laimėjote {laimeta_suma} Eur. Sveikiname!")
                    print("*********************************************************************************")
                    ar_zaisti(1)
            else:
                print("Nėra tokio pasirinkimo.\n")
                
        if klausimas["atsakymas"] == atsakymas:
            print("\nJūsų atsakymas yra teisingas!")
            laimeta_suma += laimimos_sumos[laimeti_kartai]
            if laimeta_suma < 1000000:
                print("******************************************")
                print(f"Sveikiname, Jūs pasiekėte {laimeta_suma} Eur ribą!")
                print("******************************************\n")
                return klausimynas, laimeta_suma, bandymu_skaicius, laimeti_kartai+1, klausimo_numeris+1
            else:
                print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("$Sveikiname, Jūs laimėjote milijoną!$")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                ar_zaisti(1)
                 
        else:
            bandymu_skaicius -= 1
            if bandymu_skaicius > 1:
                print(f"\nDeja, Jūsų atsakymas yra neteisingas.\n-------------------------------------\nJums liko {bandymu_skaicius} bandymai.\n")
            elif bandymu_skaicius == 1:
                print("\nDeja, Jūsų atsakymas yra neteisingas.\n-------------------------------------\nJums liko paskutinis bandymas.\n")
            else:
                print(f"\nDeja, Jūsų atsakymas yra neteisingas.\n")
    return klausimynas, laimeta_suma, bandymu_skaicius, klausimo_numeris, laimeti_kartai

if __name__ == "__main__":
    taisykles()
    ar_zaisti(0)
    pradeti_zaidima()
