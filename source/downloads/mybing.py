from bingtrans import translate
        
eesti_keeles = input("Palun sisesta eestikeelne sõna (või lause): ")
ing_vaste = translate(eesti_keeles, 'et', 'en')
print("Inglise keelne vaste: " + ing_vaste)
