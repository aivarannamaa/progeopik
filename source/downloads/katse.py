y = float(input("Sisestage arv, mille ruutjuurt tahate leida: "))

x0 = 1
while True :
    eelmine_x0 = x0

    x0 = (x0 + y / x0 ) / 2.0

    print("Lähend on " + str(x0))

    # Lõpeta arvutamine, kui lähend enam eriti ei muutu
    if abs(x0-eelmine_x0) < 0.0000001:
        break

print("Ruutjuur on ligikaudu: " + str(x0))