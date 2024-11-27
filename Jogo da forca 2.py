import random 
import time

palavras = ['brasil', 'argentina']
palavra = random.choice(palavras)
jogador = []
vitoria = 0
vidas = 5

for i in range(len(palavra)):
	jogador.append('_')

print('-' * 67)
time.sleep(0.25)
print("|--------+    ")
time.sleep(0.25)
print("|       [ ]  ")
time.sleep(0.25)
print("|      / | \ ")
time.sleep(0.25)
print("|       / \  ")
time.sleep(0.25)
print("|              ")
print('-' * 67)
time.sleep(0.25)
while vidas > 0:
	print("\nDigite a letra\n")
	print(f"[0] sair\n[1] chutar\n")
	letra = input("--: ").lower()
	print("\n")
	if letra == "0":
		break
	if letra == "1":
		print("Qual é a palavra\n")
		chute = input("--: ").lower()
		print("\n")
		if chute == palavra:
			print("Parabéns, você acertou ")
			break
		else:
			print("Que pena, você errou :(")
			break
	while not letra.isalpha() or len(letra) > 1:
		time.sleep(0.3)
		print("A caracter é invalída\n")
		letra = input("--: ").lower()
		print("\n")
		time.sleep(0.3)
	acertos = len(palavra)
	for i in range(len(palavra)):
		gps = palavra.find(letra, i , (i+1))
		if gps != -1:
			jogador[gps] = letra
			vitoria += 1
		if gps == -1:
			acertos -= 1
	time.sleep(0.3)
	print(jogador)
	time.sleep(0.3)
	if vitoria == len(palavra):
		print("\nParabéns, você ganhou!!")
		break
	if acertos == 0:
		vidas -= 1
		print(f"\nA palavra não possui a letra {letra}\n")
		time.sleep(0.5)
		print(f"Sua vida caiu para {vidas}\n")
		if vidas == 4:
			time.sleep(0.25)
			print("|--------+    ")
			time.sleep(0.25)
			print("|       [ ]     ")
			time.sleep(0.25)
			print("|      / | \   ")
			time.sleep(0.25)
			print("|       /      ")
			time.sleep(0.25)
			print("|               ")	
		elif vidas == 3:
			time.sleep(0.25)
			print("|--------+    ")
			time.sleep(0.25)
			print("|       [ ]     ")
			time.sleep(0.25)
			print("|      / | \  ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.25)
			print("|               ")	
		elif vidas == 2:
			time.sleep(0.25)
			print("|--------+    ")
			time.sleep(0.25)
			print("|       [ ]    ")
			time.sleep(0.25)
			print("|      / |     ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.25)
			print("|               ")	
		elif vidas == 1:
			time.sleep(0.25)
			print("|--------+    ")
			time.sleep(0.25)
			print("|       [ ]     ")
			time.sleep(0.25)
			print("|        |      ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.25)
			print("|               ")	
		else:
			time.sleep(0.25)
			print("|--------+    ")
			time.sleep(0.25)
			print("|       [ ]     ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.25)
			print("|               ")
			time.sleep(0.3)
			print("\nQue pena, você perdeu")
			break