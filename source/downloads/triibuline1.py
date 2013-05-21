from pykkar import *


world1 = """
########
#      #
#      #
#  ^   #
#      #
#      #
########
"""

world2 = """
##########
#        #
#        #
#        #
# ^      #
##########
"""

create_world(world1) # NB! programm peab töötama ka world2-ga

# Võime eeldada, et robot alustab alati näoga põhjasuunas, aga täpset asukohta
# me ei tea.



# Esimene etapp: liigutame roboti loodenurka, näoga lõuna suunas
# liigu põhjaseinani
while not is_wall():
    step()

# pööra läänesuunda
right()
right()
right()

# liigu lääneseinani
while not is_wall():
    step()

# pööra lõunasuunda
right()
right()
right()



# Värvimise etapp:
# välimine tsükkel käib üle veergude (kaks veergu korraga, üks allaminnes,
# koos värvimisega ja teine üles tulles, ilma värvimiseta)
while True:

    # allaminek ja värvimine
    paint()
    while not is_wall():
        step()
        paint()

    # liigu järgmisele veerule (kui võimalik)
    right()
    right()
    right()

    if is_wall():
        # rohkem veerge pole
        break

    # kui jõudsime siia, siis on järelikult veel veerge
    step()
    # pööra nina põhjasuunda
    right()
    right()
    right()

    # liigu üles
    while not is_wall():
        step()

    # proovime liikuda järgmisele (värvitavale) veerule
    right()
    if is_wall():
        # pole rohkem veerge
        break

    step()
    # pöörame õigesse suunda
    right()
