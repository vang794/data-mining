#Carolyn Vang
#Introduction to Data Mining
#Project 1
#2/22/2024

#Citation: createTuples method logic from https://www.youtube.com/watch?v=e_SBq3s20M8&t=841s
#A k-Shingle object.
#K and the document(doc) are initialized.
class Shingle:
    def __init__(self, k, doc):
        self.set = []
        self.k = k
        self.doc = doc

    # In a for loop, create k-shingles from document.
    #If container length is 0, append value
    #If container length is not 0, check true or false if there are duplicates.
    #If false, append to self.container
    #Return set
    def createTuples(self):
        for i in range(0, len(self.doc) - (self.k-1)):
            if (len(self.set) == 0):
                self.set.append(self.doc[i:i + self.k])
            else:
                if not (self.isFound(self.doc[i:i + self.k])):
                    self.set.append(self.doc[i:i + self.k])
        return self.set

    #Parameter is value. Value is the second numeric value compared to self.value
    #Returns true if values are the same and returns false if not
    def isFound(self,value):
        val1 = value
        for item in self.set:
            val2 = item
        if val1==val2:
            return True
        else:
            return False
