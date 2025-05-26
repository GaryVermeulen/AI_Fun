# poTest.py
# pickle/object test
#
import pickle

class MyClass:
    def __init__(
        self,
        a = '',
        b = '',
        c = []
        ):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"MyClass(a={self.a}, b={self.b}), c={self.c}"

    def printAll(self):
        print("a: ", self.a)
        print("b: ", self.b)
        print("c: ", self.c)

# Create an instance of MyClass
obj1 = MyClass(1, 2)
obj1.printAll()
print("---")

# Pickle the object to a file
with open('data.pickle', 'wb') as file:
    pickle.dump(obj1, file)

# Create a new instance of MyClass (the existing object)
obj2 = MyClass(3, 4)
obj2.printAll()
print(f"Before loading: {obj2}")

print("---")

# Load the pickled data
with open('data.pickle', 'rb') as file:
    loaded_obj = pickle.load(file)

# Update the existing object's attributes
obj2.__dict__.update(loaded_obj.__dict__)

obj2.printAll()
print(f"After loading: {obj2}")
