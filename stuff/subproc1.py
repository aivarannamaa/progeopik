import subprocess
import sys

testnäited = {
    0.0 : 32.0,
    -51 : -59.8,
    39  : 102.2
}

for celsius in testnäited:
    fahrenheit = testnäited[celsius]
    sisend = str(celsius) + "\n"

    vastus = subprocess.run([sys.executable, "lahendus.py"],
                            input=sisend, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    väljund = vastus.stdout

    if vastus.returncode != 0:
        print("VIGA! Sisendi", celsius, "korral ebaõnnestus programmi käivitamine.",
              "Veakood oli", vastus.returncode, "ja veavoo sisu oli järgmine\n",
              vastus.stderr)

    elif str(fahrenheit) not in väljund:
        print("VIGA! Sisendi", celsius, "korral ei leidnud väljundist oodatud vastust.")