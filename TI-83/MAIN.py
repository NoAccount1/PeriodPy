from HELPER import cl,menuPrint,printTbl,delAccents
from COMPRESS import P

while True:
    cl()
    menu = menuPrint(1,"Par numéro","Par symbole","Par nom","Par valence"," *Quitter")
    if menu == 1:
        cl()
        a = int(input("Element N°" + ("\n" * 10) + ">>> ")) - 1
        if a <= len(P):
            print()
            printTbl(P[a]["N"],P[a]["S"],P[a]["P"],P[a]["C"],P[a]["Z"],P[a]["Y"],P[a]["X"],)
        else: print("Élément introuvable")
    elif menu == 2:
        cl()
        a = input("Symbole" + ("\n" * 10) + ">>> ").lower()
        for i in P:
            if i["S"].lower() == a:
                print()
                printTbl(i["N"],i["S"],i["P"],i["C"],i["Z"],i["X"],i["Y"],)
                break
        else: print("Élément introuvable")
    elif menu == 3:
        cl()
        a = delAccents(input("Nom" + ("\n" * 10) + ">>> ").lower())
        print(a)
        for i in P:
            if delAccents(i["N"].lower()) == a:
                printTbl(i["N"],i["S"],i["P"],i["C"],i["Z"],i["X"],i["Y"],)
                break
        else: print("Élément introuvable")
    elif menu == 4:
        print("menu 4")
    elif menu == 5:
        cl()
        break
    input()
