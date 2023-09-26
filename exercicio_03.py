mes=int(input("qual é o mês que estamos? "))
mesnascimento=int(input("em que mês você nasceu? "))
idade=int(input("quantos anos você tem? "))

if mesnascimento>=mes:
    anonascimento=(2023-idade)-1
else:
    anonascimento=(2023-idade)

print(anonascimento)