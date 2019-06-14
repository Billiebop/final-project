#Abraham Carrillo
#ID: 220641
print("Abraham Carrillo")
print("This is a family tree about the sped crew")
sped=["Level: Smart", "Level: Smart but barely dumb", "Level: 50/50-Stupid/Smart", "Level: retardnation sped", "Level: deadly dumb sped"]
class Parent():
    def __init__(self, name, sped_lvl, typ):
        self.name=name
        self.sped_lvl=sped_lvl
        self.typ=typ
    def ap(self):
        print("This is", self.name, "and he is at level", self.sped_lvl)
    def ty(self):
        print(self.name, "-", self.typ)
class Child(Parent):
    def __init__(self, name, sped_lvl, typ):
        Parent.__init__(self, name, sped_lvl, typ)
class Gchild(Child):
    def __init__(self, name, sped_lvl, typ):
        Parent.__init__(self, name, sped_lvl, typ)
class dchild():
    def __init__(self, name, sped_lvl, typ):
        self.name=name
        self.sped_lvl=sped_lvl
        self.typ=typ
    def ap(self):
        print("This is", self.name, "and he is at level", self.sped_lvl)
    def ty(self):
        print(self.name, "-", self.typ)
def main():
  done = False
  while not done:
    print("Menu")
    print("S - Start")
    print("Q - Quit")
    choice = input("Choice: ")
    if choice == "S":
        print("Starting...")
        print("First off lets talk about sped level first")
        for i in range(len(sped)):
            print(i, "\t", sped[i])
        print("___________________________")
        p1=Parent("Sajid", 5, "dad")
        p2=Parent("Tariq", 2.5, "mom")
        c1=Child("Abraham", 2, "son")
        c21=dchild("Mi", 3, "son from another family")
        c2=Child("Talha", 1.5, "daughter")
        g1=Gchild("Siam", 4, "grandson")
        p1.ap()
        p2.ap()
        c1.ap()
        c21.ap()
        c2.ap()
        g1.ap()
        print("Do want to continue and see the family tree?")
        oop=input("Y/N::  ")
        if oop=="N":
            done=True
        elif oop=="Y":
            print("Alright")
            p1.ty()
            p2.ty()
            c1.ty()
            c21.ty()
            c2.ty()
            g1.ty()
            print("Hit enter to continue")
            entor=input(":: ")
            if entor=="𝖛𝖋𝖋𝖊𝖜":
                done=True
            else:
                print("Ok")
        else:
            print("Invalid")
            done=True

    elif choice == "Q":
        print("Exiting Final Project!")
        print("Had a fun time in CS, cya!")
        done = True

main()