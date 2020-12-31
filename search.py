from helper import menuPrint,printTbl,formatParam,delAccents
from period import Period
menu=menuPrint("With number","With symbol","With name","With valence")
if menu==1:
    a=int(input("Element N°\n>>> ")) - 1
    print(Period[a]["Nom"])
    printTbl(
        Period[a]["Nom"],
        Period[a]["Symbole"],
        Period[a]["Phase"],
        Period[a]["Categorie"],
        Period[a]["Xpos"],
        Period[a]["Ypos"],
        Period[a]["Numéro"]
    )
    print("\033[H\033[J"); input()
elif menu==2:
    a=input("Symbole\n>>> ")
    for i in Period: 
        if i["Symbole"]==a:
            printTbl(
                i["Nom"],
                i["Symbole"],
                i["Phase"],
                i["Categorie"],
                i["Xpos"],
                i["Ypos"],
                i["Numéro"]
            )
elif menu==3:
    a=delAccents(input("Nom\n>>> ").lower())
    for i in Period:
        if i["Nom"].lower()==a:
            printTbl(
                i["Nom"],
                i["Symbole"],
                i["Phase"],
                i["Categorie"],
                i["Xpos"],
                i["Ypos"],
                i["Numéro"]
            )
            break
    else:
        print("Élément introuvable")
elif menu==4:
    print("menu 4")