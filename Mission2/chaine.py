t = int(input("Entrez une taille :"))
c = str(input("Entrez un caractère :"))


for i in range (t, 0, -1):
    chaine = ""
    for j in range (0 ,t ,1):
        if i % 2 == 0:
            chaine += c + " "
        else:
            chaine += " " + c
    print(chaine)
