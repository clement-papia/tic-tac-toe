def colonne(m):
    #colonnes
    for i in range(0,3):
        if(m[i][0]==m[i][1]==m[i][2]!=" "):
            print(' le joueur a gagné:',m[i][0])
            return 0

    #lignes    
    for i in range(0,3):
        if(m[0][i]==m[1][i]==m[2][i]!=" "):
            print('le joueur a gagné:',m[0][i])
            return 0

    #diagonales
    if(m[0][0]==m[1][1]==m[2][2]!=" "):
        print('le joueur a gagné:',m[1][1])
        return 0

    if(m[0][2]==m[1][1]==m[2][0]!=" "):
        print('le joueur a gagné:',m[1][1])
        return 0

    #cases a remplir
    for i in range(0,3):
        for j in range(0,3):
            if(m[i][j]==" "):
                return 1
    print("fin du jeu aucun gagnant")
    
    return 0
def draw(m):
    print("-------------")
    for i in range(0,3):
        print("|",m[i][0],"|",m[i][1],"|",m[i][2],"|")
        print("-------------")
    return 1
if __name__== "__main__":
    vide=" "
    m =[[vide,vide,vide],[vide,vide,vide],[vide,vide,vide]]
    draw(m)
    j='x'
    while(colonne(m)):
     case=int(input("Entrer un numéro de case entre 1 et 9:"))-1
     if(not(-1<case<9)):
         continue
     x=case%3
     y=int((case-x)/3)
     if(m[y][x]==' '):
         m[y][x]=j
         j='0' if j=='x' else 'x'
     draw(m)