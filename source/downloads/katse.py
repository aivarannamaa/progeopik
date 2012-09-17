while True:
    tekst = input("Sisesta arv ja vajuta ENTER (lõpetamiseks vajuta ainult ENTER): ")

    if tekst == "":
        print("OK, lõpetan")
        break
    else: # ei olnud ei arv ega tühisõne
        arv = float(tekst)
        print("Selle arvu ruut on", arv * arv)