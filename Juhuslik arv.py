#valib juhusliku arvu ja nimetab selle, kui arv on väiksem kui 5, vastasel juhul ütleb, et "suurem arv"
from random import *
a = (randint(1, 10))
print(a)
if a == 1:
    print("üks")
elif a == 2:
    print("kaks")
elif a == 3:
    print("kolm")
elif a == 4:
    print("neli")
elif a == 5:
    print("viis")
else:
    print("suurem arv")