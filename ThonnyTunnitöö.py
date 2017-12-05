#programm kysib su nime, siis annab arvutustehte ja ytleb, kas sa vastasid õigesti, kysib kas tahad ka uut tehet ja kui ytled ei, lõpetab ära
print("What is your name?")
myName = input()
print("Hello, " + myName)
from random import *
a = (randint(1, 10))
b = (randint(1, 10))
c = input("How much is " + str(a) + "*" + str(b) + "? ")
if int(c) == (a*b):
    print("Correct! I bet you can't get it right twice in a row motherfucker!")
else:
    print("Nope, you made a mistake! Just like the one ur momma made when she had you!")
d = input("Do you want to do another one?")
while d == "yes":
    a = (randint(1, 10))
    b = (randint(1, 10))
    c = input("How much is " + str(a) + "*" + str(b) + "? ")
    if int(c) == (a*b):
        print("Correct! I bet you can't get it right twice in a row motherfucker!")
    else:
        print("Nope, you made a mistake! Just like the one ur momma made when she had you!")
    d = input("Do you want to do another one?")
else:
    print("Goodbye motherfucker, u bad at math anyway!")