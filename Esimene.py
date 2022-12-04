#Ülesanne 1
#Kirjuta programm, mis sind tervitab.
print("Ulesanne 1")
print("Hello World!")


#Ülesanne 2

#Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?

#+Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?

#+Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print("Ulesanne 2")
a=input('vastus on')

a=3+8/(4-2)*4

print("vastus", a)


#Ülesanne 2.1

#Ruudu sees asub ring. Ringi raadius on 3.

#Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.


from dataclasses import dataclass

import dataclasses

from math import *

print("Ulesanne 2.1")

input("ruudu sees asub ring")

S=pi*9

print("ringi pindala", S)

print()

C=2*pi*3

print("ringi umbermoot", C)

print()

S=4*9

print("ruud pindala", S)

print()

P=8*3

print("ruud umbermoot", P)


#Ülesanne 2.2

#Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu:

#kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist,

#et Maa raadius ekvaatori kohal on 6378 km.

print("Ulesanne 2.2")

a=10000/2.5

print("uhe kilometrile mahub nii palju muntide", a)


b=4000*6378

print("kogu ekvaatori mahub", b)

#Ülesanne 3
#Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
#kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll
#kill-koll

#Kas kasutasid muutujaid? Millistel juhtudel oleks muutujate kasutamine kindlasti otstarbekas?

print("Ulesanne 3")
a='kill-koll,'
b='killadi-koll,'
c='killkoll,'
print(a,a,b,a,a,b,a,a,c,a)

#Ülesanne 4
#Koosta programm, mis väljastaks järgmised laulusõnad:

#Rong see sõitis tsuhh tsuhh tsuhh,
#piilupart oli rongijuht.
#Rattad tegid rat tat taa,
#rat tat taa ja tat tat taa.
#Aga seal rongi peal,
#kas sa tead, kes olid seal?

#Kuidas lahendasid ülesande? Kas seda saaks teha kuidagi paremini? Kui lihtne oleks sellest programmist teha uus, kui
#soovitakse hoopis järgmist laulu?

#Rong see sõitis tuut tuut tuut,
#piilupart oli rongijuht.
#Rattad tegid kill koll koll,
#kill koll koll ja kill koll kill.


#....Sisend, väljund, tingimus....

print("Ulesanne 4")

print("Rong see sõitis tsuhh tsuhh tsuhh,")
print("piilupart oli rongijuht.")
print("Rattad tegid rat tat taa,")
print("rat tat taa ja tat tat taa.")
print("Aga seal rongi peal,")
print("kas sa tead, kes olid seal?")

print("Rong see sõitis tuut tuut tuut,")
print("piilupart oli rongijuht.")
print("Rattad tegid kill koll koll,")
print("kill koll koll ja kill koll kill.")



#Ülesanne 5

#Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku

#ümbermõõdu ja pindala.

from math import *

print("Ulesanne 5")


a=float(input('sisesta ristuliku pikkus='))

b=float(input('sisesta ristkuliku laius='))

P=2*(a+b)

print("ristkuliku umbermoot", P)

print()

a=float(input('sisesta kulje='))

b=float(input('sisesta kulje='))

S=a*b

print("ristkuliku pindala", S)