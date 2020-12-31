from HELPER import cl,menuPrint,printTbl,delAccents
from DTABLE import Period

while True:
    cl()
    menu = menuPrint(1,"With number","With symbol","With name","With valence"," *Quitter")
    if menu == 1:
        cl()
        a = int(input("Element N°" + ("\n" * 10) + ">>> ")) - 1
        print()
        printTbl(
            Period[a]["Nom"],
            Period[a]["Symbole"],
            Period[a]["Phase"],
            Period[a]["Categorie"],
            Period[a]["Numéro"],
            Period[a]["Ypos"],
            Period[a]["Xpos"],
        )
    elif menu == 2:
        cl()
        a = input("Symbole" + ("\n" * 10) + ">>> ").lower()
        for i in Period:
            if i["Symbole"].lower() == a:
                print()
                printTbl(
                    i["Nom"],
                    i["Symbole"],
                    i["Phase"],
                    i["Categorie"],
                    i["Numéro"],
                    i["Xpos"],
                    i["Ypos"],
                )
                break
        else:
            print("Not found")
    elif menu == 3:
        cl()
        a = delAccents(input("Nom" + ("\n" * 10) + ">>> ").lower())
        for i in Period:
            if i["Nom"].lower() == a:
                printTbl(
                    i["Nom"],
                    i["Symbole"],
                    i["Phase"],
                    i["Categorie"],
                    i["Numéro"],
                    i["Xpos"],
                    i["Ypos"],
                )
                break
        else:
            print("Élément introuvable")
    elif menu == 4:
        print("menu 4")
    elif menu == 5:
        cl()
        break
    input()
