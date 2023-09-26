contador=1
novamente="S"
while novamente=="S":
    numero=float(input("digite um número "))
    while numero==0:
        contador+=1
        print("número inválido ")
        numero = float(input("digite novamente "))

    if numero>0:
        print("positivo")
    else:
        print("negativo")
    print(f"você tentou {contador} vezes")
    novamente=input("deseja fazer de novo? S ou N ")
else:
    print("tchau")
