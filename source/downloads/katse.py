from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab
# roboti "maailma"
# Trellid tähistavad seinu, nooleke tähistab robotit
# (noole suund tähistab roboti suunda)
create_world("""
########
#     >#
#      #
#      #
#      #
#      #
########
""")

samme_jäänud = 3
while samme_jäänud > 0:
    if is_wall(): # ei lase robotil vastu seina põrgata
        break
    else:
        step() # robot liigub ühe ruudu võrra edasi
        samme_jäänud -= 1

# pöörame ringi
right()
right()
