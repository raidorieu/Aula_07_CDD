novamente="S"
while novamente=="S"or novamente=="s":
    nota1 = float(input("Qual foi a primeira nota? "))
    while nota1 > 10 or nota1 < 0:
        nota1 = float(input("a nota 1 está invalida, digite novamente: "))

    nota2 = float(input("Qual foi a segunda nota? "))
    while nota2 > 10 or nota2 < 0:
        nota2 = float(input("a nota 2 está invalida, digite novamente: "))

    media = (nota1 + nota2) / 2

    print(f"a média do aluno é {media}")
    if media >= 7:
        print("aluno aprovado")
    elif media >= 4:
        print("aluno na recuperação")
    else:
        print("aluno reprovado")
    novamente=input("deseja fazer novamente? responda com 'S' ou 'N' ")

else:
    print("tchau")