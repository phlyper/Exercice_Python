# programme principal -----------------------------------------------
p_seuil, v_seuil = 2.3, 7.41
print("Seuil pression :", p_seuil, "\tSeuil volume ;", v_seuil, "\n")
pression = float(input("Pression courante = "))
volume = float(input("Volume courant = "))
if (pression > p_seuil) and (volume > v_seuil):
	print("\t pression ET volume eleves. Stoppez !")
elif pression > p_seuil:
	print("\t Il faut augmenter le volume")
elif volume > v_seuil:
	print("\t Vous pouvez diminuer le volume")
else:
	print("\t Tout va bien !")

print("--------------------------------------")

n = int(input("Entrez un entier [1 .. 10] : "))
while not(1 <= n <= 10):
	n = int(input("Entrez un entier [1 .. 10], S.V.P. : "))
print("\nValeur saisie :", n)