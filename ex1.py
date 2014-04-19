import sys
for x in range(1, 10):
	if x == 5:
		break
	print(x)
	
def mafonction(x):
	return 2*x**3 + x -5

print(mafonction(int(sys.argv[1])))

def tabuler(borneInf, borneSup, nbPas):
	if borneInf < borneSup:
		for x in range(borneInf, borneSup, nbPas):
			print(x)
	else:
		print("borneInf > borneSup")

tabuler(10, 1, 2);

# import
from math import sqrt
# programme principal -----------------------------------------------
x = float(input("x ? "))
if x >= 0:
	y = sqrt(x)
	print("La racine de {:.2f} est {:.3f}".format(x, y))
else:
	print("On ne peut pas prendre la racine d'un reel negatf !")
print("\nAu revoir")