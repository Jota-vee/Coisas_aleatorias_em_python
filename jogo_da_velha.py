import random

casa = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
lance = 0

a1 = "_"
a2 = "_"
a3 = "_"
b1 = "_"
b2 = "_"
b3 = "_"
c1 = " "
c2 = " "
c3 = " "

def tabuleiro():
	
	print("\n")
	print("    1   2   3  ")
	print(f"a  _{a1}_|_{a2}_|_{a3}_")
	print(f"b  _{b1}_|_{b2}_|_{b3}_")
	print(f"c   {c1} | {c2} | {c3} ")
	print("\n")
	
def robo():
	global lance_robo
	
	if lance == 1 and lance_jogador == "b2":
		lance_1 = ["a1","a3","c1","c3"]
		lance_robo = random.choice(lance_1)
	elif a1 == peça_robo and a2 == peça_robo and a3 == "_":
		lance_robo = "a3"
	elif a1 == "_" and a2 == peça_robo and a3 == peça_robo:
		lance_robo = "a1"
	elif a1 == peça_robo and a2 == "_" and a3 == peça_robo:
		lance_robo = "a2"
	elif b1 == peça_robo and b2 == peça_robo and b3 == "_":
		lance_robo = "b3"
	elif b1 == "_" and b2 == peça_robo and b3 == peça_robo:
		lance_robo = "b1"
	elif b1 == peça_robo and b2 == "_" and b3 == peça_robo:
		lance_robo = "b2"
	elif c1 == peça_robo and c2 == peça_robo and c3 == " ":
		lance_robo = "c3"
	elif c1 == " " and c2 == peça_robo and c3 == peça_robo:
		lance_robo = "c1"
	elif c1 == peça_robo and c2 == " " and c3 == peça_robo:
		lance_robo = "c2"
	elif a1 == peça_robo and b1 == peça_robo and c1 == " ":
		lance_robo = "c1"
	elif a1 == "_" and b1 == peça_robo and c1 == peça_robo:
		lance_robo = "a1"
	elif a1 == peça_robo and b1 == "_" and c1 == peça_robo:
		lance_robo = "b1"
	elif a2 == peça_robo and b2 == peça_robo and c2 == " ":
		lance_robo = "c2"
	elif a2 == "_" and b2 == peça_robo and c2 == peça_robo:
		lance_robo = "a2"
	elif a2 == peça_robo and b2 == "_" and c2 == peça_robo:
		lance_robo = "b2"
	elif a3 == peça_robo and b3 == peça_robo and c3 == " ":
		lance_robo = "c3"
	elif a3 == "_" and b3 == peça_robo and c3 == peça_robo:
		lance_robo = "a3"
	elif a3 == peça_robo and b3 == "_" and c3 == peça_robo:
		lance_robo = "b3"
	elif a1 == peça_robo and b2 == peça_robo and c3 == " ":
		lance_robo = "c3"
	elif a1 == "_" and b2 == peça_robo and c3 == peça_robo:
		lance_robo = "a1"
	elif a1 == peça_robo and b2 == "_" and c3 == peça_robo:
		lance_robo = "b2"	
	elif c1 == peça_robo and b2 == peça_robo and a3 == "_":
		lance_robo = "a3"
	elif c1 == " " and b2 == peça_robo and a3 == peça_robo:
		lance_robo = "c1"
	elif c1 == peça_robo and b2 == "_" and a3 == peça_robo:
		lance_robo = "b2"
	elif a1 == peça_jogador and a2 == peça_jogador and a3 == "_":
		lance_robo = "a3"
	elif a1 == "_" and a2 == peça_jogador and a3 == peça_jogador:
		lance_robo = "a1"
	elif a1 == peça_jogador and a2 == "_" and a3 == peça_jogador:
		lance_robo = "a2"
	elif b1 == peça_jogador and b2 == peça_jogador and b3 == "_":
		lance_robo = "b3"
	elif b1 == "_" and b2 == peça_jogador and b3 == peça_jogador:
		lance_robo = "b1"
	elif b1 == peça_jogador and b2 == "_" and b3 == peça_jogador:
		lance_robo = "b2"
	elif c1 == peça_jogador and c2 == peça_jogador and c3 == " ":
		lance_robo = "c3"
	elif c1 == " " and a2 == peça_jogador and a3 == peça_jogador:
		lance_robo = "c1"
	elif c1 == peça_jogador and c2 == " " and a3 == peça_jogador:
		lance_robo = "c2"
	elif a1 == peça_jogador and b1 == peça_jogador and c1 == " ":
		lance_robo = "c1"
	elif a1 == "_" and b1 == peça_jogador and c1 == peça_jogador:
		lance_robo = "a1"
	elif a1 == peça_jogador and b1 == "_" and c1 == peça_jogador:
		lance_robo = "b1"
	elif a2 == peça_jogador and b2 == peça_jogador and c2 == " ":
		lance_robo = "c2"
	elif a2 == "_" and b2 == peça_jogador and c2 == peça_jogador:
		lance_robo = "a2"
	elif a2 == peça_jogador and b2 == "_" and c2 == peça_jogador:
		lance_robo = "b2"
	elif a3 == peça_jogador and b3 == peça_jogador and c3 == " ":
		lance_robo = "c3"
	elif a3 == "_" and b3 == peça_jogador and c3 == peça_jogador:
		lance_robo = "a3"
	elif a3 == peça_jogador and b3 == "_" and c3 == peça_jogador:
		lance_robo = "b3"
	elif a1 == peça_jogador and b2 == peça_jogador and c3 == " ":
		lance_robo = "c3"
	elif a1 == "_" and b2 == peça_jogador and c3 == peça_jogador:
		lance_robo = "a1"
	elif a1 == peça_jogador and b2 == "_" and c3 == peça_jogador:
		lance_robo = "b2"	
	elif c1 == peça_jogador and b2 == peça_jogador and a3 == "_":
		lance_robo = "a3"
	elif c1 == " " and b2 == peça_jogador and a3 == peça_jogador:
		lance_robo = "c1"
	elif c1 == peça_jogador and b2 == "_" and a3 == peça_jogador:
		lance_robo = "b2"
	else:
		lance_robo = random.choice(casa)
		

print("Jogo da velha")
tabuleiro()
print("escolha sua peça\n")
print("[1] X")
print("[2] O\n")
escolha = input("--: ")
print("\n")

while escolha != "1" and escolha != "2":
	print("elemento inexistente, por favor escolha novamente\n")
	print("[1] X")
	print("[2] O\n")
	escolha = input("--: ")
	print("\n")

if escolha == "1":
	peça_jogador = "X"
	peça_robo = "O"
else:
	peça_jogador = "O"
	peça_robo = "X"

while len(casa) > 0:
	lance += 1
	print("movimentos disponiveis\n")
	print(casa)
	print("\nqual seu movimento\n")
	lance_jogador = input("--: ").lower()
	while lance_jogador not in casa:
		print("\nmovimento invalido, por favor escolha novamente\n")
		print(casa)
		print("\n")
		lance_jogador = input("--: ").lower()
	
	
	if lance_jogador == "a1":
		a1 = peça_jogador
	elif lance_jogador == "a2":
		a2 = peça_jogador
	elif lance_jogador == "a3":
		a3 = peça_jogador
	elif lance_jogador == "b1":
		b1 = peça_jogador
	elif lance_jogador == "b2":
		b2 = peça_jogador
	elif lance_jogador == "b3":
		b3 = peça_jogador
	elif lance_jogador == "c1":
		c1 = peça_jogador
	elif lance_jogador == "c2":
		c2 = peça_jogador
	else:
		c3 = peça_jogador
		
	if a1 == peça_jogador and a2 == peça_jogador and a3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif b1 == peça_jogador and b2 == peça_jogador and b3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif c1 == peça_jogador and c2 == peça_jogador and c3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif a1 == peça_jogador and b1 == peça_jogador and c1 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif a2 == peça_jogador and b2 == peça_jogador and c2 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif a3 == peça_jogador and b3 == peça_jogador and c3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif a1 == peça_jogador and b2 == peça_jogador and c3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
	elif c1 == peça_jogador and b2 == peça_jogador and a3 == peça_jogador:
		tabuleiro()
		print("\nVocê ganhou!!")
		break
		
	casa.remove(lance_jogador)
	
	if len(casa) == 0:
		tabuleiro()
		print("\nempate")
		break
		
		
	robo()

		
		
	if lance_robo == "a1":
		a1 = peça_robo
	elif lance_robo == "a2":
		a2 = peça_robo
	elif lance_robo == "a3":
		a3 = peça_robo
	elif lance_robo == "b1":
		b1 = peça_robo
	elif lance_robo == "b2":
		b2 = peça_robo
	elif lance_robo == "b3":
		b3 = peça_robo
	elif lance_robo == "c1":
		c1 = peça_robo
	elif lance_robo == "c2":
		c2 = peça_robo
	else:
		c3 = peça_robo
		
	if a1 == peça_robo and a2 == peça_robo and a3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif b1 == peça_robo and b2 == peça_robo and b3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif c1 == peça_robo and c2 == peça_robo and c3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif a1 == peça_robo and b1 == peça_robo and c1 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif a2 == peça_robo and b2 == peça_robo and c2 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif a3 == peça_robo and b3 == peça_robo and c3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif a1 == peça_robo and b2 == peça_robo and c3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
	elif c1 == peça_robo and b2 == peça_robo and a3 == peça_robo:
		tabuleiro()
		print("\nVocê perdeu :(")
		break
		
	casa.remove(lance_robo)
	tabuleiro()