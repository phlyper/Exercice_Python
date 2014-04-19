def compterMots(texte):
	dict = {}
	listeMots = texte.split()

	for mot in listeMots:
		if mot in dict:
			dict[mot] = dict[mot] + 1
		else:
			dict[mot] = 1
	return dict
# programme principal -----------------------------------------------
res = compterMots("Ala Met Asn Glu Met Cys Asn Glu Hou Ala Met Gli Asn Asn")
for c in res.keys():
	print(c, "-->", res[c])
	
	
# import
from math import sqrt
# fonction
def trinome(a, b, c):
	delta = b**2 - 4*a*c
	if delta > 0.0:
		racine_delta = sqrt(delta)
		return (2, (-b-racine_delta)/(2*a), (-b+racine_delta)/(2*a))
	elif delta < 0.0:
		return (0,)
	else:
		return (1, (-b/(2*a)))
if __name__ == "__main__":
	print(trinome(1.0, -3.0, 2.0))
	print(trinome(1.0, -2.0, 1.0))
	print(trinome(1.0, 1.0, 1.0))