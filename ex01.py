print("Opções")
print("1 - Par ou Ímpar")
print("2 - Verifique o número")
print("3 - Mostre o dobro")
opcao = int(input("Escolha uma opção: "))
match opcao:
   case 1:
        print("1 - Par ou Ímpar")
        n = int(input("Escolha um número: "))
        if n % 2 == 0:
           print(f"{n} é par")
        else:
           print(f"{n} é ímpar")
   case 2:
        print("2 - Verifique o número")
        numero1=int(input("Escolha o 1º número: "))
        numero2=int(input("Escolha o 2º número: "))
        if numero1 > numero2:
           print(f"{numero1} é maior que {numero2}")  
        elif numero1 < numero2:
           print(f"{numero1} é menor que {numero2}")  
        else:        
           print(f"{numero1} é igual a {numero2}") 
   case 3:
        print("3 - Mostre o dobro")
        numero4 = int(input("Escolha o número: "))
        print(f"O dobro desse número é {2*numero4}")
   case _:
        print("Opção Inválida")