import pickle

print("starting...")

def pickleIt(name, o):
    pickle.dump(o, open(name + ".pickle", "wb"))

def unpickleIt(name):
    return (pickle.load(open(name + ".pickle", "rb")))

def showPerson(p):
    print ("Display name: " + p.DisplayName)
                

# pickle a string
a = "mike was here"
pickle.dump(a, open("first.pickle", "wb"))
returnedString = pickle.load(open("first.pickle", "rb"))
print("returned: " + returnedString )


class Person:
    Age=-1
    DisplayName=""

mike = Person()
mike.Age =40
mike.DisplayName = "Rapa, Mike"

pickleIt("mike", mike)
newPerson = unpickleIt("mike")
showPerson(newPerson)

print("mike: " + mike.DisplayName)

print("Ending")
