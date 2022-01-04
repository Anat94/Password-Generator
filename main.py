import pymysql
import random
import sys
import getpass


#system de recherche dans la bdd + interface graphique
mode = sys.argv[1]
def check_mdp():
    mdpok= "AA"
    MDP = getpass.getpass("Entrez le mdp général\n")

    if (mdpok == MDP) :
        print("Général Password ok !")
    else :
        print("Bad Général Password ")
        check_mdp()

try:
    connection = pymysql.connect(host="localhost",user="root",passwd="",database="Password-Generator")
    cursor = connection.cursor()
except ValueError:
    print("Failed to connect to database")
    exit(84)
def create_password():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbols = "&é~#'{([-|è`_\ç^à@)]=}^$£ù%*µ?,.;/:!§"

    if len(sys.argv) != 4 :
        exit(84)

    all = lower + upper + number + symbols
    length = 16
    link = sys.argv[2]
    identifier = sys.argv[3]
    password = "".join(random.sample(all, length))


    retrive = "Select Website from Informations;"
    cursor.execute(retrive)
    rows = cursor.fetchall()
    for row in rows:
        if sys.argv[2] == row[0]:
            cursor.execute("Select Identifier from Informations where Website = '%s';" %row[0])
            Ident = cursor.fetchall()
            for row2 in Ident:
                if sys.argv[3] == row2[0] :
                    print("This website is ever registred in the bdd with this account")
                    connection.close()
                    exit (84)

    insert1 = "INSERT INTO Informations(Website, Identifier, Password) VALUES('" + link  + "', '" + identifier + "','" + password  + "' );"
    cursor.execute(insert1)
    connection.commit()
    connection.close()
    print(password)
    print("Password successfuly saved in BDD")

def search_password():
    website = sys.argv[2]
    name = sys.argv[3]
    cursor.execute("Select Password from Informations where Website = '"+ website +"' and Identifier = '"+ name +"';")
    row = cursor.fetchall()
    print(row[0])


check_mdp()
if (mode == "Create") :
    create_password()
elif (mode == "Search") :
    search_password()