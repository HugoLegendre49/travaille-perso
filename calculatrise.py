n_1 = input("entrer un nombre : ")
n_2 = input("entrer un autre nombre : ")
symbole = input("donner un symbole : ")
resulta = 0
if n_1.isnumeric() and n_2.isnumeric():
    n_1 = int(n_1)
    n_2 = int(n_2)
    match symbole:
        case '+':
          resulta = n_2 + n_1
        case '-':
          resulta = n_1 - n_2
        case '*' :
          resulta = n_2 * n_1
        case '/' :
            if not n_2==0 :
                resulta = n_1 / n_2
            else :
               print("t qui pour essayer de diviser par 0 en fait")
        case _ :
          print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    print(resulta)
else :
    print("merci de mettre des nombre entier")