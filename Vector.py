#Carolyn Vang
#Introduction to Data Mining
#Project 1
#2/22/2024

#Binvector is the binary vector created from the shingles
#The length of the vector is 1000
class Binvector:
    def __init__(self):
        self.vect=[0] * 1000
    #population method is given a set of shingles
    #Method takes the values from the set and uses the values as indexes.
    #Method sets the value "1" to self.vect list by the given indexes.
    #If the value does not exist, then the corresponding index value is not set to 1.
    def population(self,shingle):
        for item in shingle:
            index = item
            self.vect[index] = 1
    #Jaccard sim methods

    #Intersect method takes the object's vector and intersects with given vector
    #count all (1,1) pairs between vector and other vector
    #Returns amount of pairs
    def intersect(self,vect2):
        count=0
        #interate by column index
        for row in range(0,999):
            if self.vect[row]==1 and vect2.vect[row]==1:
                count+=1
        return count

    #Union method takes the object's vector and unifies with given vector
    #count all (0,1),(1,0),(1,1) pairs
    #Returns amount of pairs
    def union(self,vect2):
        count=0
        #interate by column index
        for row in range(0,999):
            if self.vect[row]==1 or vect2.vect[row]==1:
                count+=1
        return count
    #sim method takes the object's vector and second vector.
    #Uses intersect and union methods
    #Calculates the Jaccard Simularity value
    #Returns numeric value
    #Citation for logic and code: https://www.geeksforgeeks.org/how-to-calculate-jaccard-similarity-in-python/
    def sim(self,vect2):
        num=self.intersect(vect2)
        den=self.union(vect2)
        jaccsim=num/den
        return jaccsim
