time1 = input("digite o nome de um time1: ")
time2 = input("digite o nome de um time2: ")
golstime1 = int(input("digite a quantidade de gols do time1: "))
golstime2 = int(input("digite a quantidade de gols do time1: "))
if golstime1>golstime2: print(f"{time1} ganhou de {golstime1} a {golstime2} do {time2} ")
elif golstime1==golstime2: print(f"o jogo foi empate no placar de {golstime1} a {golstime2}")
else: print(f"{time2} ganhou de {golstime2} a {golstime1} do {time1} ")