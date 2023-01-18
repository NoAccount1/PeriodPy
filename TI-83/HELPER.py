phase = ["Solide", "Liquide", "Gazeux"]
category = ['Métaloïde', 'Gaz noble', 'Non-métal', 'Métal pauvre', 'Mt de trans', 'Alcalin', 'Halogène', 'Alc-terreu']

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

def cl(): print("\n" * 10)

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

def fParam(p):
    if len(p) > 11: print("Invalid length")
    else: return p + " "*(12-len(p))

def printTbl(nm,sy,ph,ca,nb,xp,yp):
    n,s,p,c,z,xy = fParam(str(nm)),fParam(str(sy)),fParam(str(phase[ph])),fParam(str(category[ca])),fParam(str(nb)),fParam(str(xp) + " / " + str(yp))
    print("  ____________________________ \n"
          " | Nom         |", n, "|\n"
          " | Symbole     |", s, "|\n"
          " |_____________|______________|\n"
          " | Période/Col |", xy, "|\n"
          " | N° atomique |", z, "|\n"
          " |_____________|______________|\n"
          " | Phase       |", p, "|\n"
          " | Categorie   |", c, "|\n"
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
        input(txt+("\n"*HEIGHT)+">>> ")
    else:
        txt = input(txt,"\n>>> ")
    return txt
