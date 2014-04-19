import sys # importation de la bibliothèque standard système

def main(argv=None):
    if argv == None:
        argv = sys.argv
	
    # traitement des arguments de la ligne de commande
    # et exécution du programme
       
    return 0

if __name__ == "__main__":
    main(55)
	
print(sys.argv)

# -*- coding:utf-8 -*-

from random import randint

d = randint(1, 6)
print(d)

if d == 1:
    print("gagné")
else:
    if d == 5:
        print("gagné")
    else:
        if d == 6:
            print("gagné")
        else:
            print("perdu")
			
texte = "Quid? qui se etiam nunc subsidiis patrimonii aut amicorum liberalitate sustentant, hos perire patiemur? An, si qui frui publico non potuit per hostem, hic tegitur ipsa lege censoria; quem is frui non sinit, qui est, etiamsi non appellatur, hostis, huic ferri auxilium non oportet? Retinete igitur in provincia diutius eum, qui de sociis cum hostibus, de civibus cum sociis faciat pactiones, qui hoc etiam se pluris esse quam collegam putet, quod ille vos tristia voltuque deceperit, ipse numquam se minus quam erat, nequam esse simularit. Piso autem alio quodam modo gloriatur se brevi tempore perfecisse, ne Gabinius unus omnium nequissimus existimaretur."
mot_long = ""  # Cette variable contiendra le mot cherché.
# Le recordman de longueur en quelque sorte.
# Pour l’instant on stocke le mot vide "" dedans.
mots = texte.split()              # On construit la liste des mots.
for mot in mots:                  # On parcourt cette liste (boucle for).
	if len(mot) > len(mot_long):  # Si le mot rencontré bat le record de longueur,
		mot_long = mot            # on le proclame recordman.
print(mot_long)                   # On affiche le résultat.