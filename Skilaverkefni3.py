# Hákon Garðarsson
# Haust 2020


class Nemi:
    def __init__(self,kennitala,nafn,kyn,postnumer,nafnSkola,email):
        self.kennitala=kennitala
        self.nafn=nafn
        self.kyn=kyn
        self.postnumer=postnumer
        self.nafnSkola=nafnSkola
        self.email=email



class GrunnskolaNemi(Nemi):
    def __init__(self,kennitala,nafn,kyn,postnumer,nafnSkola,email,forrmadur):
        Nemi.__init__(self,kennitala,nafn,kyn,postnumer,nafnSkola,email)
        self.forrmadur=forrmadur

    def __str__(self):
        return str(self.kennitala)+" "+str(self.nafn)+" "+str(self.kyn)+" "+str(self.postnumer)+" "+str(self.nafnSkola)+" "+str(self.email)+" "+str(self.forrmadur)


class FrammhaldskolaNemi(Nemi):
    def __init__(self,kennitala,nafn,kyn,postnumer,nafnSkola,email,brautarheiti,fjoldiafangabusetu,styrkur=False):
        Nemi.__init__(self,kennitala,nafn,kyn,postnumer,nafnSkola,email)
        self.brautarheiti=brautarheiti
        self.fjoldiafangabusetu=fjoldiafangabusetu
        self.styrkur=styrkur

    def __str__(self):
        return str(self.kennitala)+" "+str(self.nafn)+" "+str(self.kyn)+" "+str(self.postnumer)+" "+str(self.nafnSkola)+" "+str(self.email)+" "+str(self.brautarheiti)+" "+str(self.fjoldiafangabusetu)

class HaskolaNemi(Nemi):
    def __init__(self, kennitala, nafn, kyn, postnumer, nafnSkola, email,stignams,namslan=False,namskuld=0):
        Nemi.__init__(self,kennitala, nafn, kyn, postnumer, nafnSkola, email)
        self.stignams=stignams
        self.namslan=namslan
        self.namsskuld=namskuld


def birta(listi):
    for x in listi:
        print(x)


def finna_kyn(listi):
    kk_teljari=0
    kvk_teljari=0
    for x in listi:
        if x.kyn=="kk":
            kk_teljari+=1
        elif x.kyn =="kvk":
            kvk_teljari+=1
    return "------------ Fjöldi stráka er: "+str(kk_teljari)+" fjöldi stelpna er: "+str(kvk_teljari)+" -------------"



def finna_nem_med_skola(listi,skola):
    listi_med_nem=[]
    for x in listi:
        if str(x.nafnSkola)==str(skola):
             listi_med_nem.append(x.__str__())
    return listi_med_nem


def fjoldi_afanga(listi):
    listi1=[]
    for x in listi:
        if int(x.fjoldiafangabusetu)<=4:
            listi1.append(x.nafn)
    return listi1





grunnskolalisti=[GrunnskolaNemi("1111113322", "Jón Jónson", "kk", 112, "Rimaskóli", "jon@gmail.com", "Jón Pállson"),
                 GrunnskolaNemi("2203071140", "Páll Friðson", "kk", 112, "Rimaskóli", "pall@gmail.com", "Friður Friðson"),
                 GrunnskolaNemi("2911095093", "Ragnar Leifson", "kk", 101, "Asnaskóli", "ragnar@gmail.com", "Leifur Rögnvaldsson"),
                 GrunnskolaNemi("0707072310", "Júlía Rögnvaldsdóttir", "kvk", 102, "Melarskóli", "julia@gmail.com", "Rögnvaldur Leifsson"),
                 GrunnskolaNemi("0606064591", "Ágúst Júlúsarson", "kk", 103, "Bústaðarskóli", "agust@gmail.com", "Júlús Ceasar")]


framhalskólalisti=[ FrammhaldskolaNemi("1111113322", "Jón Jónson", "kk", 112, "Tækniskóli", "jon@gmail.com", "Tölvubraut","8",False),
                    FrammhaldskolaNemi("1111113322", "Jón Jónson", "kk", 112, "MS", "jon@gmail.com", "Tölvubraut","8",False),
                    FrammhaldskolaNemi("1111113322", "Jón Jónson", "kk", 112, "Tækniskóli", "jon@gmail.com", "Tölvubraut","8",False),
                    FrammhaldskolaNemi("1111023322", "Páll Mansson", "kk", 112, "MR", "jon@gmail.com", "Tölvubraut","3",False),
                    FrammhaldskolaNemi("2207013322", "Guðrún Helgadóttir", "kvk", 112, "Versló", "gudrun@gmail.com", "Nátúrufræði","3",False)]



"""
flag1=True
while flag1:
    print("1. Grunnskólanemendur")
    print("2. Framhalskólanemdur")
    print("3. Háskólanemendur")
    print("4. Hætta")
    try:
        val=int(input("Veldu 1-4"))
        if val<1 or val>4:
            raise ValueError ("\n -------------Verður að velja 1-4--------------")
    except ValueError as x:
        print(x)

    if val==1:
        flag2 = True
        while flag2:
            print("1. Birta lista")
            print("2. Fjöldi kk eða kvk")
            print("3. Finna nemendur í skóla")
            print("4. Hætta")
            try:
                val = int(input("Veldu 1-4"))
                if val < 1 or val > 4:
                    raise ValueError("\n -------------Verður að velja 1-4--------------")
            except ValueError as x:
                print(x)

            if val == 1:
                birta(grunnskolalisti)

            elif val == 2:
                print(finna_kyn(grunnskolalisti))


            elif val == 3:
                skoli = input("Sláðu inn skóla")
                print(finna_nem_med_skola(grunnskolalisti, skoli))

            elif val == 4:
                flag2 = False

    elif val==2:
        print(2)

    elif val==3:
        print(3)

    elif val==4:
        print(4)
"""

flag3 = True
while flag3:
    print("1. Birta lista")
    print("2. Finna fjölda 4 eða færri áfanga")
    print("3. Búa utan höfuðborgarsvæði")
    print("4. Hætta")
    try:
        val = int(input("Veldu 1-4"))
        if val < 1 or val > 4:
            raise ValueError("\n -------------Verður að velja 1-4--------------")
    except ValueError as x:
        print(x)

    if val==1:
        birta(framhalskólalisti)

    elif val==2:
        print(fjoldi_afanga(framhalskólalisti))

    elif val==3:
        print(3)

    elif val==4:
        print(4)






"""
flag4 = True
while flag4:
    print("1. Birta lista")
    print("2. Finna fjölda 4 eða færri áfanga")
    print("3. Búa utan höfuðborgarsvæði")
    print("4. Hætta")
    try:
        val = int(input("Veldu 1-4"))
        if val < 1 or val > 4:
            raise ValueError("\n -------------Verður að velja 1-4--------------")
    except ValueError as x:
        print(x)

    if val == 1:
        birta(framhalskólalisti)

    elif val == 2:
        print(2)

    elif val == 3:
        print(3)

    elif val == 4:
        print(4)
"""








