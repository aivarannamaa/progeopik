def väärtusta_avaldis(avaldis):
    # tühikuid nõudsime selleks, et osadeks jaotamine oleks lihtsam
    märgid = avaldis.split()
    (tulemus, märgid) = loe_avaldis(märgid)
    if märgid != []:
        print("Mingi jama, allesjäänud märgid:", märgid)
    return tulemus

def loe_avaldis(märgid):
    # nagu avaldise grammatika ütleb, on avaldise lõpus alati term
    (parem_argument, märgid) = loe_term(märgid)

    # kui enne termi on operaator (+ või -), siis enne operaatorit peab olema avaldis
    if märgid != [] and märgid[-1] in ['+', '-']:
        operaator = märgid[-1]
        märgid = märgid[:-1]
        (vasak_argument, märgid) = loe_avaldis(märgid)
        if operaator == '+':
            return (vasak_argument + parem_argument, märgid)
        else:
            return (vasak_argument - parem_argument, märgid)

    # kui liitmist/lahutamist pole, siis järelikult on tegemist
    # avaldise lihtsa variandiga (e. lihtsalt termiga)
    else:
        return (parem_argument, märgid)

def loe_term(märgid):
    # selle funktsiooni ülesehitus on eelmisega analoogne
    (parem_argument, märgid) = loe_faktor(märgid)

    if märgid != [] and märgid[-1] in ['*', '/']:
        operaator = märgid[-1]
        märgid = märgid[:-1]
        (vasak_argument, märgid) = loe_term(märgid)
        if operaator == '*':
            return (vasak_argument * parem_argument, märgid)
        else:
            return (vasak_argument / parem_argument, märgid)
    else:
        return (parem_argument, märgid)

def loe_faktor(märgid):
    märk = märgid[-1]
    märgid = märgid[:-1]

    if märk == ')': # tegemist on sulgudes oleva avaldisega
        (tulemus, märgid) = loe_avaldis(märgid)
        # nüüd on eeldatavasti viimaseks sümboliks '(', "loeme" ka selle ära
        sulg = märgid[-1]
        märgid = märgid[:-1]
        if sulg != '(':
            print("Mingi jama!")
        return (tulemus, märgid)
    else:
        # tagastatud märk peab olema arv
        return (float(märk), märgid)

print(väärtusta_avaldis("3"))
print(väärtusta_avaldis("( 3 )"))
print(väärtusta_avaldis("3 * ( -4 / 3.5 + ( 3 - 2 ) ) - 6"))
print(väärtusta_avaldis("3 * 3"))
print(väärtusta_avaldis("( 3 + 3 * 4 )"))
print(väärtusta_avaldis("( 3 + 3 ) * 4"))
print(väärtusta_avaldis("1 + 1 + 1 + 1"))
print(väärtusta_avaldis("2 * 2 * 2 * 2"))
