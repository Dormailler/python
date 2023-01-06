import pickle

class Multiply(object):
    def __init__(self,multiplier):
        self.multiplier = multiplier
    
    def multiply(self,number):
        return number * self.multiplier

muliply = Multiply(5)
print(muliply.multiply(100))
f = open("multiply_object.pickle",'wb')
pickle.dump(muliply,f)
f.close()

del muliply

f = open("multiply_object.pickle",'rb')
multiply_pickle = pickle.load(f)
print(multiply_pickle.multiply(100))
f.close()
