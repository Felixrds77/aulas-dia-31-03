nome = input("coloque seu nome: ")
idade = int(input("coloque sua idade: "))
salario = float(input("coloque seu salario: "))
print(f"seu  nome é: {nome}, sua idade é: {idade} e o seu salario é: {salario:.2f}  ")
percentual = float(input("informe o percentual do almento: "))
salario +=(salario*percentual)/100
print(f"seu novo salario é : {salario}")

