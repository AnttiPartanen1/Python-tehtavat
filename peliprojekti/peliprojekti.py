
# pelissä on reilusti time.sleep komentoa siksi importtasin ajan
# importtasin ossän ikä tarkistus vitsin sekä tilasto funktion takia.
#importtasin randomin kaatumisfunktion takia
import time
import os
import random

nimi = input("Mikä on nimesi?: ")
ika = int(input("Mikä on ikäsi?: "))

# Funktio joka kirjaa nimensä mukaisesti tekstitiedostoon tilastot.
def kirjaatulos(tulos):
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(tulos + "\n")


# Tilasto funktio oli koko pelin koodauksen haastavin osuus mielestäni.
# En täydellisesti ymmärrä itsekkään täsmälleen miten se toimii mutta nyt se kirjaa häviöt, voitot sekä luovutukset ylös.
# Funktio luo "tulokset" tekstitiedoston ja kirjaa sinne voitot, häviöt sekä luovutukset.
def naytatilasto():
    if not os.path.exists("tulokset.txt"):
        print("Et ole vielä pelannut yhtään peliä.")
        return
    with open("tulokset.txt", "r") as tiedosto:
        rivit = tiedosto.readlines()
    voitot = rivit.count("voitto\n")
    haviot = rivit.count("häviö\n")
    luovtukset = rivit.count("luovutukset\n")
    print("voitot: " + str(voitot) + ", häviöt: " + str(haviot))


if ika < 12:
    print("Olet liian nuori pelaamaan näin hurjaa peliä")
    exit()
elif ika == 67:
    print("Hurjaa peliä eivät pääse pelaamaan vitsiniekkarit.")
    os.system("shutdown /r /t 7") 
    # Jos pelaaja syöttää iän "67" pelaajan tietokone käynnistyy uudelleen 
    print("Hurjaa peliä eivät pääse pelaamaan vitsiniekkarit.")
else:
    print("Tervetuloa Hurjaan peliin " + nimi +".")

#importtasin ajan koska pelin tekstit tulee näin dynaamisemmin pienellä aika viiveellä 
# Pelin ideana toimii että olet pelaajana kotona ja näät lemmikkejä kinastelevan keskenään. Pelin tarkoitus on löytää jokaiselle-
# syömistä että eläimet ei syö toisiaan.
def peli():
    print("Hurja peli alkaa...")
    time.sleep(2)
    print("Olet kotona...")
    time.sleep(2)
    print("Näät kissasi jahtaa pientä hiirtä maassa...")
    time.sleep(5)
    print("Sinulle tulee paha mieli koska olet katsonut vierestä kun hiiri on kasvanut pienestä isoksi ja nyt hän juoksee henkensä edestä")
    time.sleep(5)
    print("Näät myös että kissaa jahtaa koirasi ja ymmärrät että kissa käytännössä myös juoksee henkensä edestä...")
    time.sleep(5)
    print("Päätät etsiä lemmikeillesi ruokaa ennen kuin ne syövät toisensa")
    tavarat = []
    koti(tavarat)

# Pelaajalla on mahdollisuus kaatua siirtyessä huoneesta huoneeseen. 

def kaatuminen():
    if random.randint(1, 100) <= 10:
        print("Juostessasi varpaasi jää maton alle ja kaadun yltäpäätä naamallesi lattiaan.")
        time.sleep(4)
        print("Silmissäsi sumenee ja vaivut tajuttomaksi...")
        time.sleep(4)
        print("Eläimet jahtaavat toisiaan kunnes lopulta ne syövät toisensa kun sinä makaat lattialla tajuttomana")
        print("*********************Hävisit hurjan pelin**********************************")
        kirjaatulos("häviö")
        exit()
    

#inventaarion tarkastus funktio
def nayta_tavarat(tavarat):
    if len(tavarat) == 0:
        print("Et kanna mitään mukanasi")
    else:
        print("Kannat tällä hetkellä mukanasi:")
        for tavara in tavarat:
            print("- " + tavara)

# En kommentoi sen enempää talon huoneita pääpiireittäin ne ovat melko saman tapaiset.
def keittio(tavarat):
    print("Juokset keittiöön")
    time.sleep(1)
    print("kipi kipi")
    time.sleep(0.5)
    print("kipi kipi")
    time.sleep(0.5)
    print("kipi kipi")
    if kaatuminen():
        return True
    time.sleep(0.5)
    print("kipi kipi")
    print("Olet nyt keittiössä.")
    if "juusto" not in tavarat:            #Alempana on ensimmäinen tavaran hankinta valinta jossa pelaaja voi valita ottaako mukaansa tarjotun esineen.
        print ("näät pöydällä reikäisen juuston! otetaanko se mukaan?")
        juustovalinta = input("Nappaatko juuston mukaan vai jätätkö sen pöydälle istumaan? 1. kyllä 2. Ei")
        if juustovalinta == "1":
            tavarat.append("juusto")
            print("Nappasit juuston mukaan")
        if juustovalinta == "2":
            print("jätit juuston pöydälle...")

    if "veitsi" not in tavarat:
        print("Näät myös terävän veitsen kimaltavan pöydällä")
        veitsivalinta = input("nappaatko veitsen mukaan vai jätätkö sen pöydälle? 1. Kyllä 2. Ei")
        if veitsivalinta == "1":
            tavarat.append("veitsi")
            print("jätit veitsen pöydälle...")
    else:
        print("Keittiössä ei ole enää mitään muuta kuin resonoivaa ääntä pitävä jääkaappi...")
        time.sleep(6)

def olohuone(tavarat):
    print("Juokset olohuoneeseen")
    time.sleep(1)
    print("kipi kipi")
    time.sleep(1.5)
    print("kipi kipi")
    if kaatuminen():
            return True
    
    time.sleep(1.5)
    print("kipi kipi")
    time.sleep(1.5)
    print("kipi kipi")
    print("Olet nyt olohuoneessa.")
    print("katselet ympärillesi etsien esineitä jotka voisi olla hyödyllisiä...")
    time.sleep(3)
    if "radio" not in tavarat:
        print ("Mummon vanha radio istuu piirongin päällä... pitäisikö se napata mukaan?")
        radiovalinta = input("Nappaatko radion mukaan vai jätätkö sen piirongille istumaan? 1. kyllä 2. Ei")
        if radiovalinta == "1":
            tavarat.append("radio")
            print("Nappasit radion mukaan")
        if radiovalinta == "2":
            print("jätit radion piirongille...")

    if "luu" not in tavarat:
        print("Kurkkaat maton alle ja löydät naapurin Vesan luurangon??? ihmetyksissäsi mietit, nappaatko vesasta luun palasen mukaan?")
        luuvalinta = input("nappaatko luun mukaan vai jätätkö sen pölyttymään maton alle? 1. Kyllä 2. Ei")
        if luuvalinta == "1":
            tavarat.append("luu")
            print("Nappasit suuren luun mukaasi.")
        if radiovalinta == "2":
                    print("jätit vesan rauhaan ja peittelit luut matolla...")
    else:
        print("Olohuoneessa ei enää ole muuta kuin tikittävä kaappikello ja edes takas ryntäilevät eläimet...")


def ullakko(tavarat):
    print("Juokset ullakon luukulle")
    time.sleep(1)
    print("kipi kipi")
    if kaatuminen():
            return True
    time.sleep(1.5)
    print("kipi kipi")
    time.sleep(1)
    print("ullakko on hirvittävän kaukana päätät hengähtää hetken...")
    time.sleep(0.5)
    print("hengität syvään ja päätät jatkaa matkaa...")
    time.sleep(4.5)
    print("kipi kipi")
    time.sleep(1.5)
    print("kipi kipi")
    print("Olet nyt ullakon luukulla.")
    time.sleep(1.5)
    print("kurkkaat ullakon luukusta ja toteat että siellä ei ole oikeastaan mitään hyödyllistä sinulle.")
    print("mietiskelet miksi edes tuhlasit aikaasi katsoaksesi mitä ullakolla on")
    time.sleep(8)


def makuuhuone(tavarat):
    print("Juokset makuuhuoneeseen")
    time.sleep(1)
    print("kipi kipi")
    time.sleep(1.5)
    print("kipi kipi")
    if kaatuminen():
            return True
    time.sleep(1.5)
    print("kipi kipi")
    time.sleep(1.5)
    print("kipi kipi")
    time.sleep(1.5)                            
    #Pelin ensimmäinen häviö mahdollisuus menemällä nukkumaan.
    print("Olet nyt makuuhuoneessa.")
    print("katselet ympärillesi ja mietit onko makuuhuoneessa mitään hyödyllistä sinulle...")
    time.sleep(3)
    print ("Huomaat että sinua väsyttää, ja makkarin sänky suorastaan huutaa nimäeäsi:" + nimi + " tule nukkumaan...")
    print("Mietit, pitäisikö luovuttaa asian suhteen ja mennä vain nukkumaan...")
    nukkumaanmeno = input("Menetkö nukkumaan? 1. kyllä 2. Ei")
    if nukkumaanmeno == "1":
        print("Menit nukkumaan. Tämä oli virhe koska kissa söi hiiren ja koira söi kissan.")
        print("*********************Hävisit hurjan pelin**********************************")
        time.sleep(10)
        kirjaatulos("häviö")
        exit()
    if nukkumaanmeno == "2":
        print("Totesit että rakastat lemmikkejäsi enemmän kuin mitään muuta ja jätät nukkumaanmenon myöhemmälle.")

    if "sardiinipurkki" not in tavarat:
            print("Avaat yöpöydän laatikon ja löydät hätävara yöpala sardiinipurkin.")
            sardiinivalinta = input("Jätätkö yöpalan rauhaan vai nappaatko sen mukaan? 1. Kyllä 2. Ei")
            if sardiinivalinta == "1":
                tavarat.append("sardiinipurkki")
                print("Jätit sardiinit haisemaan yöpödän laatikkoon...")
    else:
        print("Keittiössä ei ole enää mitään muuta kuin resonoivaa ääntä pitävä jääkaappi...")


# Pelin "loppu" eli kohta missä voit syöttää eläimille hankitut tavarat


def ruokinta(tavarat):
    puuttuu = []
    if "sardiinipurkki" not in tavarat:
        puuttuu.append("kissalle") 
    if "luu" not in tavarat:
        puuttuu.append("koiralle")
    if "juusto" not in tavarat:
        puuttuu.append("hiirelle")

    if puuttuu:
        print("Sinulla ei ole vielä kaikille rakkaille eläimillesi ruokaa..." + ", ".join(puuttuu))
        return False
    
#"Join" yhdistää listan sanat yhdeksi tekstiksi.

    print("Annat koiralle luun palan ja hän lopettaa kissan jahtaamisen...")
    time.sleep(6)
    print("Juokset seuraavaksi kissan kiinni ja annat yöpala sardiinisi hänelle evääksi...")
    time.sleep(6)
    print("viimeisenä hiiri katselee sinua hengästyneenä. Päätät antaa hänelle juustonpalan joka sinulta löytyy vielä")
    time.sleep(6)
    print("Nyt kaikki eläimet mutustavat onnellisena omia eväitään... pystyt vihdoin hengähtämään itsekkin...")
    time.sleep(6)
    print("***************************************************************************")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                               VOITIT PELIN!                               ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("                                                                           ")
    print("***************************************************************************")
    time.sleep(10)
    kirjaatulos("voitto")
    return True

# Voiton lopussa tulos järjestelmä kirjaa voiton ylös.
    
    

    
def koti(tavarat):
    while True:
        print("...............................................")
        print("Valitse huone minne menet kodikkaassa kodissasi")
        print("        tai katsahda mitä kannat mukanasi      ")
        print("...............................................")
        print("                1.Keittiö                      ")
        print("                2.Makuuhuone                   ")
        print("                3.Olohuone                     ")
        print("                4.Ullakko                      ")
        print("                5.Katso mitä kannat mukana     ")
        print("                6.Ruoki eläimet                ")
        print("                7.Luovuta                      ")
        print("...............................................")

        #peliä voisi käytännössä jatkaa mielettömiin määriin lisäämällä huoneita

        valinta = input ("valitse minne mennä (numero)")

        if valinta == "1":
            keittio(tavarat)
        elif valinta == "2":
            makuuhuone(tavarat)
        elif valinta == "3":
            olohuone(tavarat)
        elif valinta == "4":
            ullakko(tavarat)
        elif valinta == "5":
            nayta_tavarat(tavarat)
            time.sleep(7)
        elif valinta == "6":
            ruokinta(tavarat)
            break
        elif valinta == "7":
            print("Ymmärrän, hurja peli kävi liian hurjaksi...")
            kirjaatulos("luovutus")
            break
        #Tein myös luovuttamisen mahdolliseksi.
        else:
            print("kirjoita numero, pelkkä numero (1-6)")



while True:
    print("..........................................")
    print("               PÄÄVALIKKO                 ")
    print("..........................................")
    print("              1.Aloita peli               ")
    print("              2.Ohjeet                    ")
    print("              3.Lopeta peli               ")
    print("              4.Tulokset                  ")
    print("..........................................")

    menuvalinta = input("Valitse vaihtoehto (numero): ")

    if menuvalinta == "1":
        peli()

    elif menuvalinta == "2":
        print("Peliä pelataan pääosin kirjoittamalla eri numeroita. Ei se sen vaikeemmaks mee.")
    elif menuvalinta == "3":
        print("Hurja peli päättyi nopeasti...")
        break
    elif menuvalinta == "4":
        naytatilasto()
        time.sleep(10)
        #Vaikka tietyt pelissä esiintyvät samankaltaiset tilastot, voitto sekä häviö ruudut voisi toteuttaa inputilla koen sen paremmaksi että peli itse
        #sulkee kyseiset näytöt ajastimella. se on myös 10 kertaa helpompi tapa koodaa kyseinen asia.
    else:
        print("Kirjoita vain numero älä aloita peli ymsyms ")



