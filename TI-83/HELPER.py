from DDICT import Dict

def lprint(txt:str):
    ln = len(txt)
    tblTxt = txt.split(" ")
    txtln = 0
    if ln <= 36:
        print(txt)
        txtln += 1
    else:
        t = ""
        for i in tblTxt:
            if len(i) > 36:
                print(i)
                if (len(i) // 36) != (len(i) / 36):
                    txtln += (len(i) // 36) + 1
                else:
                    txtln += (len(i) // 36)
            else:
                if (len(i) + len(t)) < 36:
                    t = t + " " + i
                if (len(i) + len(t)) >= 36:
                    t = t.split(" ", 1)
                    t = t[1]
                    print(t)
                    t = i
                    txtln += 1
    return txtln

def cl():
    print("\n" * 10)

def defPrint(sbj, name):
    nom = Dict[sbj]["dict"][name]["name"]
    dfn = Dict[sbj]["dict"][name]["def"]
    print(nom + ":")
    print("-----------------")
    spc = lprint(dfn)
    spc = "\n" * (9 - (spc + 2))
    print(spc)

def menuPrint(a, *item):
    if len(item) > 10:
        print(" Erreur menuPrint:\n Requier moins de 10 args,", len(item),
              "ont été donnés")
    else:
        it = []
        for i in range(len(item)):
            nbr = str(int(i) + 1) + "."
            print(nbr, item[i])
            it.append(int(int(i) + 1))
        if a == 1 and len(item) < 10:
            print("\n" * (9 - len(item)))
        while True:
            answer = int(input(">>> "))
            if answer in it:
                return answer
                break
            cl()
            print("Choix invalide")

def formatParam(p):
    if len(p) > 11:
        print("Invalid length")
    else:
        for i in range(12 - len(p)):
            p = p + " "
    return p

def printTbl(nm, sy, ph, ca, nb, xp, yp):
    name = formatParam(str(nm))
    symbol = formatParam(str(sy))
    phase = formatParam(str(ph))
    category = formatParam(str(ca))
    number = formatParam(str(nb))
    xypos = str(xp) + " / " + str(yp)
    pos = formatParam(xypos)
    print("  ____________________________ \n"
          " | Nom         |", name, "|\n"
          " | Symbole     |", symbol, "|\n"
          " |_____________|______________|\n"
          " | Période/Col |", pos, "|\n"
          " | N° atomique |", number, "|\n"
          " |_____________|______________|\n"
          " | Phase       |", phase, "|\n"
          " | Categorie   |", category, "|\n"
          " |_____________|______________|")

def delAccents(ligne):
    accent = ['à', 'â', 'é', 'è', 'ê', 'î', 'ï', 'ì', 'ô', 'ù', 'û', 'ü', 'ç']
    no_acc = ['a', 'a', 'e', 'e', 'e', 'i', 'i', 'i', 'o', 'u', 'u', 'u', 'c']
    i = 0
    while i < len(accent):
        ligne = str(ligne).replace(accent[i], no_acc[i])
        i += 1
    return ligne

def linput(inline:bool,txt:str):
    if inline==True:
        input(txt+("\n"*heigth)+">>> ")
    else:
        txt = input(txt,"\n>>> ")
    return txt