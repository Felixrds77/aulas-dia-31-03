nome = input("coloque seu nome: ")
idade = int(input("coloque sua idade: "))
salario = float(input("coloque seu salario: "))
print(f"seu  nome é: {nome}, sua idade é: {idade} e o seu salario é: {salario:.2f}  ")
percentual = float(input("informe o percentual do almento: "))
aumentosalario =salario*(percentual/100)
valor = salario + aumentosalario
print(f"seu novo salario é : {valor:.2f}, seu aumento foi de {aumentosalario:.2f} ")

