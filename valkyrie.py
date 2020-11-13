import mariadb
import sys

#trocar as variaveis: user , password , host , port, database

client = mariadb.connect(user="admin",password="pass",host="ip",port=8080,database="valk")

cursor = client.cursor()

#A seguir estarão comandos pre definidos

#createuser = "INSERT INTO Users (user,pass,plano) VALUES ({},{},{})"
#deleteuser = "DELETE {} FROM Users WHERE user={}"


print("""

    ▄   ██   █    █  █▀ ▀▄    ▄ █▄▄▄▄ ▄█ ▄███▄   
     █  █ █  █    █▄█     █  █  █  ▄▀ ██ █▀   ▀  
█     █ █▄▄█ █    █▀▄      ▀█   █▀▀▌  ██ ██▄▄    
 █    █ █  █ ███▄ █  █     █    █  █  ▐█ █▄   ▄▀ 
  █  █     █     ▀  █    ▄▀       █    ▐ ▀███▀   
   █▐     █        ▀             ▀               
   ▐     ▀                                       


[1] Create User

[2] Delete User


""")


while(1):
    command = input("-> ")
    if command == 1:
        user = input("(user to create)-> ")
        password = input("(pass)-> ")
        plano = input("(plano)-> ")
        cursor.execute("INSERT INTO Users (user,pass,plano) VALUES ({},{},{})",user,password,plano)
    elif command == 2:
        usertoDel = input("(user to delete)-> ")
        cursor.execute("DELETE FROM Users WHERE user={}",usertoDel)
    else:
        print("Opção invalida [!] \n")
