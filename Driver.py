#Carolyn Vang
#Introduction to Data Mining
#Project 1
#2/22/2024


from Shingle import Shingle
from Vector import Binvector
from Minhashing import Tables

C1 = "78493157175489549376148695781578475926543918574367195748574950004752380475183459847592567467854245734860981305640100987301574865100973401839"
C2 = "93761486957815778493157175489548475926543957481857436719574953804751800047523459824573447592567467854860981305100973401856401009873015748639"
C3 = "43967243885947619758467578364710365741564736580713650134785678460164756405674567841378954623719785810765846125647561304956765996108574857876"

a = Shingle(3, C1)
a.createTuples()
b = Shingle(3, C2)
b.createTuples()
c = Shingle(3, C3)
c.createTuples()

vectC1 = Binvector()
vectC2 = Binvector()
vectC3 = Binvector()

vectC1.population(a.set)
vectC2.population(b.set)
vectC3.population(c.set)


#1) Calculate JaccSim
vectC1.sim(vectC2)
vectC2.sim(vectC3)
vectC1.sim(vectC3)

print(f"Jaccard Simularity for C1 & C2: {vectC1.sim(vectC2)} ")
print(f"Jaccard Simularity for C2 & C3: {vectC2.sim(vectC3)} ")
print(f"Jaccard Simularity for C1 & C3: {vectC1.sim(vectC3)} ")
#2) Calculate signatures

#create minhashing tables
minHash = Tables()
minHash.permutation()
minHash.createInputMat(vectC1)
minHash.createInputMat(vectC2)
minHash.createInputMat(vectC3)

minHash.create_sigmatrix()
#print the signatures for C1,C2,C3
minHash.printSignature()

