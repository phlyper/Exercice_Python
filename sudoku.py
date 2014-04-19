# -*- coding: utf-8 -*-
"""
@author: H.BOUIA (Sep 30 2013)
Solveur de SuDoKu light
"""

class np:
	def sort(self, l):
		return l
	def reshape(self, l, s):
		z = []
		i = 0
		for x in l:
			a = i//s[0]
			b = i%s[1]
			if b == 0:
				z.append([])
			z[a].append(x)
			i = i + 1
		return z

np = np()
# Calcul des voisins incompatibles pour chaque case n allant de 0 Ã  80
def vois():
    v=[[]]*81
    for n in range(81):
        v[n],i,j=[],n//9,n%9 # initialise v[n] et calcule indices ligne/colonne 
        ri,rj=i//3,j//3 # Indices de rÃ©gion
        v[n]+=[9*i+p for p in range(9) if p!=j] # voisins de ligne
        v[n]+=[9*p+j for p in range(9) if p!=i] # voisins de colonne
        v[n]+=[27*ri+3*rj+9*(p//3)+p%3 for p in range(9)] # voisins de rÃ©gion
        v[n].remove(n) # supprime n de la liste
        v[n]=np.sort(list(set(v[n]))) # Ã©limine les doublons et sort une liste triÃ©e
    return v # liste de listes des voisins incompatibles

# Solveur du SuDoKu
def solve(g):
    n=g.find(sep) # recherche du premier caractÃ¨re non numÃ©rique dans g
    if n<0: # si tous les caractÃ¨res sont numÃ©riques, on affiche la solution
        print("\n",np.reshape([(g[i]) for i in range(81)],(9,9)))
    else: # sinon : on remplace le caractÃ¨re par un chiffre candidat
             # c : ensemble des candidats potentiels
        c=set(liste)-set([g[v[n][i]] for i in range(20)])
        for elt in c: solve(g[:n]+elt+g[n+1:])

# sep='+' : sÃ©parateur ou (case vide)
liste,sep='123456789','+' # Liste des caractÃ¨res utilisÃ©s + sÃ©parateur
# Saisie de la grille du SoDoKu Ã  rÃ©soudre : chaine de 81 caractÃ¨res
#g=string.rjust(liste,81,sep) # PremiÃ¨re ligne de 1 Ã  9
g="++94+++8+++7+815+9++++29+3+295+++++38++1+2++47+++++256+5+27++++3+281+7+++7+++53++"
print(u'\nExemple de grille a  resoudre :')
print("\n",np.reshape([(g[i]) for i in range(81)],(9,9)))
v=vois() # Calcul des voisins incompatibles
solve(g) # RÃ©solution de la grille g