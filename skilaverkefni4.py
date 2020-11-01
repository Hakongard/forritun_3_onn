# Hákon Garðarsson
# Haust 2020


import random

class Trapisa:

    numer=1
    def __init__(self,a=0,b=0,c=0,d=0,h=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
        self.nafn = "HH"
        self.numer=Trapisa.numer
        Trapisa.numer+=1

    def get_nafn(self):
        return self.nafn

    def set_nafn(self,nafn=""):
        self.nafn=nafn

    def ummal_trap(self):
        return self.a+self.b+self.c+self.d

    def flatarmal_trap(self):
        pass

    def _trap(self):
        pass

    def __str__(self):
        return "Ég er númer "+str(self.numer)+" og heiti:"+self.nafn

trap1=Trapisa(1,2,3,4,5)
trap1.set_nafn("Pétur")
print(trap1.get_nafn())
print(trap1)

trap2=Trapisa(3,5,38,3,5)
trap2.set_nafn("Sveppi")
print(trap2)


"""
class Froskur:
    numer=1
    def __init__(self,kyn):
        self.kyn=kyn
        self.numer=Froskur.numer
        Froskur.numer+=1

    def __str__(self):
        return "Ég er froskur númer "+str(self.numer)+" og ég er "+str(self.kyn)

hann=Froskur("kk")
print(hann)
hun=Froskur("kvk")
print(hun)
froskar_kk=[]
froskar_kk.append(hann)
froskar_kvk=[]
froskar_kvk.append(hun)
dagur=0
kyn=""
while (len(froskar_kvk)+len(froskar_kk))<10000:
    for x in range(len(froskar_kvk)):
        tala=random.randint(0,1)
        if tala==1:
            kyn="kk"
            froskur = Froskur(kyn)
            froskar_kk.append(froskur)
        else:
            kyn="kvk"
            froskur= Froskur(kyn)
            froskar_kvk.append(froskur)
    dagur+=2
    print("Dagur númer:",dagur)
    print("Fjöldi kk froska nuna:",len(froskar_kk))
    print("Fjöldi kvk froska nuna:", len(froskar_kvk))
    



class Bill:
    def __init__(self,tegund="",argerd="",hradi="",bensin="",eydsla=""):
        self.tegund=tegund
        self.argerd=argerd
        self.hradi=hradi
        self.bensin=bensin
        self.eydsla=eydsla

    def stada(self,sek):
        metrar_komnir=self.hradi*sek
        return metrar_komnir

    def eftir_bensin(self,sek):
        eftir_bensin=(self.bensin-(self.eydsla*self.hradi*sek)/100)
        return eftir_bensin

    def __str__(self):
        return str(self.tegund)+" árgerð "+str(self.argerd)


hradi=random.randint(5,15)
bensin=random.randint(1,10)
eydsla=random.randint(2,8)
bill1=Bill("Honda",2013,hradi,bensin,eydsla)
print(bill1)
hradi=random.randint(5,15)
bensin=random.randint(1,10)
eydsla=random.randint(2,8)
bill2=Bill("KIA",2011,hradi,bensin,eydsla)
print(bill2)
hradi=random.randint(20,30)
bensin=random.randint(1,10)
eydsla=random.randint(2,8)
bill3=Bill("Rolls Royce",2006,hradi,bensin,eydsla)


sek=0
while (bill1.stada(sek)<1000 and bill1.eftir_bensin(sek)>=0) and (bill2.stada(sek)<1000 and bill2.eftir_bensin(sek)>=0):
    sek+=1
    print(bill1.tegund,"er kominn",bill1.stada(sek))
    print(bill2.tegund, "er kominn", bill2.stada(sek))
    print(bill1.tegund,"á eftir af bensíni",round(bill1.eftir_bensin(sek),2))
    print(bill2.tegund, "á eftir af bensíni", round(bill2.eftir_bensin(sek), 2))



class Ithrottarmadur:
    def __init__(self,nafn="",aldur=0,kyn="hk"):
        self.nafn=nafn
        self.aldur=aldur
        self.kyn=kyn
        self.gildi=2

    def kraftur_ithtottar(self):
        return self.gildi

    def __str__(self):
        if self.kyn.lower()=="kk":
            return self.nafn+" er "+str(self.aldur)+" ára gamall"+" og íþróttarkrafturinn er "+str(self.kraftur_ithtottar())
        else:
            return self.nafn+" er"+str(self.aldur)+" ára gömul"


class Hlaupari(Ithrottarmadur):
    def __init__(self,nafn,aldur,kyn,hradi):
        Ithrottarmadur.__init__(self,nafn,aldur,kyn)
        self.hradi=hradi


    def kraftur_ithtottar(self):
        return self.gildi*self.hradi


    def __str__(self):
        if self.kyn.lower() == "kk":
            return self.nafn+" er "+str(self.aldur)+" ára gamall og hraðinn er "+ str(self.hradi)+" og íþróttarkrafturinn er "+str(self.kraftur_ithtottar())
        else:
            return self.nafn + " er " + str(self.aldur) + " ára gömul og hraðinn er " + str(self.hradi)+" og íþróttarkrafturinn er "+str(self.kraftur_ithtottar())


class Kraftlyfting_madur(Ithrottarmadur):
    def __init__(self,nafn,aldur,kyn,styrkur):
        Ithrottarmadur.__init__(self,nafn,aldur,kyn)
        self.styrkur=styrkur

    def kraftur_ithtottar(self):
        return self.gildi*self.styrkur

    def __str__(self):
        if self.kyn.lower() == "kk":
            return self.nafn + " er " + str(self.aldur) + " ára gamall og styrkurinn er " + str(self.styrkur)+" og íþróttarkrafturinn er "+str(self.kraftur_ithtottar())
        else:
            return self.nafn + " er " + str(self.aldur) + " ára gömul og styrkurinn er " + str(self.styrkur)+" og íþróttarkrafturinn er "+str(self.kraftur_ithtottar())









ob1=Ithrottarmadur("Hákon",17,"kk")
print(ob1)
ob2=Hlaupari("Júlía",22,"kvk",6)
print(ob2)
ob3=Kraftlyfting_madur("Steinn",29,"kk",9)
print(ob3)
"""