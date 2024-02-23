#Carolyn Vang
#Introduction to Data Mining
#Project 1
#2/22/2024
class Tables:
    #Constructor has permutation matrix, input matrix, signaturematrix, and dimensions
    def __init__(self):
        self.permMatrix = []
        self.inputMatrix = []
        self.sigMatrix = []
        self.dimensions=1000

    #Get dimensions from constructor
    def get_dim(self):
        return self.dimensions

    # Get inputMatrix from constructor
    def get_inputMatrix(self):
        return self.inputMatrix
    # Get sigMatrix from constructor
    def get_sigMatrix(self):
        return self.sigMatrix
    # Get permMatrix from constructor
    def get_permMatrix(self):
        return self.permMatrix

    # Given hash functions
    # H1(x): (x+1) mod 1000
    # H2(x): (x+2) mod 1000
    # H3(x): (x+3) mod 1000
    #Permutation method converts indexes according to the given hash functions.
    #Permutations are made into lists according to the given hash functions
    #Permutation Matrix appends permutation lists to matrix
    def permutation(self):
        vect1 = [0] * self.get_dim()
        vect2 = [0] * self.get_dim()
        vect3 = [0] * self.get_dim()
        for index in range(0, self.get_dim()-1):
            vect1[index] = (index + 1) % 1000
            vect2[index] = (index + 2) % 1000
            vect3[index] = (index + 3) % 1000
        self.permMatrix.append(vect1)
        self.permMatrix.append(vect2)
        self.permMatrix.append(vect3)

    #Creates the input matrix given by vertices
    def createInputMat(self, vector):
        self.inputMatrix.append(vector.vect)

    #foundValue method checks to see if the given value(wantedValue) is in the given permutation list
    #Returns a boolean value
    def foundValue(self,wantedValue,permList):
        if wantedValue in permList:
            return True
        else:
            return False

    #Method create_sigList performs minhashing.
    #Parameter is list from the permMatrix
    # Spare_Row gives a list filled with 0 values.
    #Looks for values from 0 to  number of dimensions (1000)
    #If true, the index of the wanted Value in the Permutation list is used.
    #Each vector list from inputMatrix uses index to check if the value is 1
    #Returns list of values
    def create_sigList(self, permList):
        spare_row=[0,0,0]
        for wantedValue in range(0,self.get_dim()):
            if self.foundValue(wantedValue,permList):
                found_index=permList.index(wantedValue)
                #iterate through vectors in inputMatrix
                for vector in self.get_inputMatrix():
                    if vector[found_index] == 1 and spare_row[self.inputMatrix.index(vector)]==0:
                        spare_row[self.inputMatrix.index(vector)]=wantedValue
        return spare_row

    #Creates signature matrix
    #Appends lists of values given by create_sigList() method
    def create_sigmatrix(self):
        for row in range(0,3):
            self.sigMatrix.append(self.create_sigList(self.permMatrix[row]))

    def printSignature(self):
        for document in range(0,len(self.get_sigMatrix())):
            print(f"Document C{document} signature: ")
            printed_List = []
            for sigNum in self.get_sigMatrix():
                printed_List.append(sigNum[document])
            print(printed_List)


