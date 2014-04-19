print(" Exemple 1 ".center(40, '-'))
for lettre in "ciao":
	print(lettre)
print()
print(" Exemple 2 ".center(40, '-'), "\n")
for i in [7, 'm', 2.718]:
	print(i, end=" ")
print("\n\n{:-^40}".format(" idem avec format "))

print()

# import
from math import sin, pi
# programme principal -----------------------------------------------
for x in range(-3, 4): # -3 -2 -1 0 1 2 3
	try:
		print("{:.3f}".format(sin(x)/x), end=" ")
	except:
		print("{:.3f}".format(float(1)), end=" ")
print()

# fonctions
def cube(x):
	"""Calcule le cube de l'argument."""
	return x**3
def volumeSphere(r):
	"""Calcule le volume d'une sphere de rayon <r>."""
	return 4 * pi * cube(r) / 3
# programme principal -----------------------------------------------
rayon = float(input("Rayon : "));
print("\nVolume de la sphere de rayon {:.1f} : {:.3f}".format(rayon, volumeSphere(rayon)));

def somme(a, b, c):
	return a+b+c
# programme principal -----------------------------------------------
sequence = (2, 4, 6)
print(somme(*sequence))

t =5
def ff(a):
	a=1
ff(t)
print(t)