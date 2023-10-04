# Functie om een vraag te stellen en het antwoord te controleren
def stel_vraag(vraag, juist_antwoord):
    antwoord = input(vraag)
    if antwoord.lower() == juist_antwoord.lower():
        print('goed!')
        return True
    else:
        print('fout!')
        return False

# Functie om de quiz uit te voeren
def speel_quiz():
    punten = 0
    aantal_vragen = 10

    print('\n\n\nWelkom bij de quiz')

    antwoord = input('Ben je klaar om de Quiz te spelen? (ja/nee): ')

    if antwoord.lower() == 'ja':
        print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2023 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')

        if stel_vraag('Vraag 1: Wat is 15 * 10? ', '150'):
            punten += 1

        if stel_vraag('Vraag 2: Welke is een INT?\nA: 9\nB: 9,5\n', 'a'):
            punten += 1

        if stel_vraag('Vraag 3: wat is de uitkomst voor:\nfor x in "banana":\nprint(x)?\n', 'banana'):
            punten += 1

        if stel_vraag('vraag: Wie is de grondlegger van Python?\n', 'Guido van Rossum'):
            punten += 1

        if stel_vraag('vraag: Hoe zet je een opmerking op een regel neer?\n', '#'):
            punten += 1

        if stel_vraag('vraag: Wat is een voorbeeld van een ingebouwde Python-functie om de lengte van een lijst (array) te berekenen?\n', 'len()'):
            punten += 1

        if stel_vraag('vraag: Wat is de hoofdstad van Frankrijk?\n', 'Parijs'):
            punten += 1

        if stel_vraag('vraag: Wat is de hoofdstad van Duitsland?\n', 'Berlijn'):
            punten += 1

        if stel_vraag('vraag: Wat is de hoofdstad van Portugal?\n', 'Lissabon'):
            punten += 1

        if stel_vraag('vraag: Wat is de hoofdstad van Estland?\n', 'Tallinn'):
            punten += 1

        print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
        cijfer = round(float(10/aantal_vragen*punten), 1)
        print('Je cijfer voor dit project komt daarmee op een voorlopige '+str(cijfer)+'.')
        if punten >= 6:
            print('Goed bezig!')
        else:
            print('Hmmm, kan beter... nog even oefenen chef.\n\n')

    elif antwoord.lower() == 'nee':
        print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
    else:
        print('Dit antwoord ken ik niet!')

# Start de quiz
speel_quiz()


