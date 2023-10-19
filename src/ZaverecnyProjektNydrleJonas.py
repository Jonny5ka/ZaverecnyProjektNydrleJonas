        #Třída Pojistenec představuje informace jednoho pojištěnce, který uchovává atributy jmeno, prijmeni, vek, telefon.
class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

        """
        Metoda __str__ vymezuje textový popis objektu Pojistenec, který se zobrazí při výpisu.
        Na základě f-řetězců umožňuje vložení hodnot do textu pomocí hodnot atributů
        objektu self.jmeno, self.prijmeni, self.vek a self.telefon.
        """
    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek} let, Telefoní číslo: {self.telefon}"

        """
        Třída EvidencePojistencu slouží k evidenci všech pojištěnců. Ukládá je do seznamu s názvem pojistenci.
        Každý člen tohoto seznamu bude instancí třídy Pojistenec, který představuje jednoho pojištěnce.
        """
class EvidencePojistencu:
    def __init__(self):
        self.pojistenci = []

        """
        Metoda pridej_pojistence přidává nového pojištěnce do evidence pojištěnců.
        Pojistenec - Tato instance představuje konkrétního pojištěnce a je volána
        hodnotami argumentů jmeno, prijmeni, vek, telefon.
        Nově založeného Pojištěnce pojistenec přidáváme do seznamu pojistenci. Seznam pojistenci slouží
        k evidenci všech pojištěnců, tím pádem tato metoda přidává nového pojištěnce do této evidence.
        """
    def pridej_pojistence(self, jmeno, prijmeni, vek, telefon):
        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.pojistenci.append(pojistenec)

        """
        Třída UzivatelskeRozhrani bude moci používat a manipulovat s evidencí pojištěnců. Tímto způsobem vytváříme spojení mezi třídou
        UzivatelskeRozhrani a třídou EvidencePojistencu, což umožňuje uživatelskému rozhraní přistupovat k evidenci
        pojištěnců a provádět s ní různé operace, jako je přidávání nových pojištěnců nebo vyhledávání existujících pojištěnců.
        """
class UzivatelskeRozhrani:
    def __init__(self):
        self.evidence = EvidencePojistencu()
        #Metoda vytvor_pojisteneho umožňuje přidat informace o novém pojištěnci a přidat ho do evidence.
    def vytvor_pojisteneho(self):
        jmeno = input("Zadejte jméno: ")
        if not jmeno:
            print("Chyba: Nebylo zadáno jméno. Data nebyla uložena.")
            return

        prijmeni = input("Zadejte příjmení: ")
        if not prijmeni:
            print("Chyba: Nebylo zadáno příjmení. Data nebyla uložena.")
            return

        vek = input("Zadejte věk: ")
        telefon = input("Zadejte telefonní číslo: ")
        self.evidence.pridej_pojistence(jmeno, prijmeni, vek, telefon)
        print("Data byla uložena. Pokračujte ve výběru...")

if __name__ == "__main__": #Následující části kódu budou prováděny pouze při spuštění tohoto skriptu jako samostatný program.
    rozhrani = UzivatelskeRozhrani()
    volba = None #Uchovává danou volbu zadavatele.

    while volba != "4": #Vyvolává smyčku, která zobrazuje menu s akcemi, dokud není zvolena volba "4 - Konec".
        print("----------------------------")
        print("Evidence Pojištěných")
        print("----------------------------")
        print("1 - Přidat nového pojištěnce")
        print("2 - Vypsat všechny pojištěnce")
        print("3 - Vyhledat pojištěného podle jména a příjmení")
        print("4 - Konec")
        volba = input() #Načte volbu od zadavatele.

        if volba == "1": #Umožní zadat nového pojištěnce do seznamu. Volá se metoda vytvor_pojisteneho z třídy UzivatelskeRozhrani.
            rozhrani.vytvor_pojisteneho()
        elif volba == "2": #Vypíše všechny zadané pojištěnce ze seznamu. Pokud není evidován ani jeden pojištěnec, tak se zobrazí zpráva o nenalezení pojištěnce.
            if not rozhrani.evidence.pojistenci:
                print("V evidenci se nenachází žádný pojištěný.")
            else:
                for pojisteny in rozhrani.evidence.pojistenci:
                    print(pojisteny)
        elif volba == "3": #Zadá se jméno a příjmení pro vyhledání již přidaného pojištěnce ze seznamu.
            jmeno = input("Zadejte jméno pojištěného: ")
            prijmeni = input("Zadejte příjmení: ")
            for pojisteny in rozhrani.evidence.pojistenci:
                if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                    print(pojisteny)
                    break
            else: #Pokud pojištěnec není nalezen nebo je špatně zadán, tak se zobrazí "Pojištěný se jménem XY nebyl nalezen."
                print(f"Pojištěný se jménem {jmeno} {prijmeni}nebyl nalezen.")
        elif volba not in {"1", "2", "3", "4"}: #V případě zadání jiného čísla z výběru 1, 2, 3, 4 program vypíše větu "Neplatná volba. Zvolte jedno z čísel 1, 2, 3, 4."
            print("Neplatná volba. Zvolte jedno z čísel 1, 2, 3, 4.")