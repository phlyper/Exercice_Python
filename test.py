"""
import math

for k,v,s in {'aad':'111','bbe':'222'}:
    print("%s : %s : %s",k,v,s)
    print("+++++++++++++")
    if k == 'b':
        print('jeniale')
"""
from datetime import date
from time import gmtime, strftime
import time
import re
import sys

def main():
    print('Hello there', len(sys.argv))
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

class Point2D:
	name = ""
	x = 0
	y = 0
	def __init__(self, name, x, y=10):
		self.name = name
		self.x = x
		self.y = y
	
	def __str__(self):
		return "{0}({1},{2})".format(self.name, self.x, self.y)
		
class Point3D(Point2D):
	z = 0
	def __init__(self, name, x, y=10, z=5):
		Point2D.__init__(self, name, x, y)
		self.z = z
		
	def __str__(self):
		#self.toString()
		return "{0},{1})".format(Point2D.__str__(self).replace(")", ""), self.z)

class Droit:
	def __init__(self, p1, p2 = Point3D("p11", x=5)):
		self.p1 = p1
		self.p2 = p2
		self.separ("b")
	
	def milieu(self):
		p = Point3D("Centre", 0)
		p.x = (self.p1.x + self.p2.x)/2
		p.y = (self.p1.y + self.p2.y)/2
		return p
	def separ(self, q="q"):
		print('separ', "{0}, {1}".format(self.p1, self.p2), q)
	def mesure(v):
		print('v',v)

p2 = Point2D("A",x=0)
print(p2)
p3 = Point3D("B",x=8,z=3)
print(p3)
p4 = Point2D("C",x=1)
print(p4)

d = Droit(p2)
Droit.mesure("aaa")
pd = d.milieu()
print(pd)


today = date.today()
print("today :", today.strftime("%m-%d-%y %H:%M:%S %Z. %d %b %Y is a %A on the %d day of %B."))

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

now = time.time()
today == date.fromtimestamp(now)
print("today :", today, ", now :", now)


pattern = re.compile(".*KB[0-9]{6,8}.*")
try:
	with open('../../AOPEN.txt', 'r') as f:
		for line in f.readlines():
			if pattern.match(line):
				print(line.strip())
		# print(int(line.strip()))
except IOError as e:
	print("erreur de fichier ::", e)
except ValueError as e:
	print("erreur de conversion ::", e)
except:
	print("erreur inconnue !")