num1=int(input("digite um número: "))
num2=int(input("digite um número: "))
num3=int(input("digite um número: "))

if(num1>num2):
       if num1>num3:
         print(f"{num1} é maior")
       else:
           print(f"{num3} é maior")
    elif num2>num1:
        if num2>num3:
            print(f"{num2} é maior")
        else:
            print(f"{num3} é maior")

