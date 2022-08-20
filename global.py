import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
from datetime import date, datetime, timedelta
import os
from contextlib import closing
from logger_base import log

load_dotenv()

def credentialDirectory(option):
    if opcion == 0:
        credential = os.getenv('DatabaseServer1')
    elif opcion == 1:
        credential = os.getenv('DatabaseServer2')
    elif opcion == 2:
        credential = os.getenv('DatabaseServer3')
    elif opcion == 3:
        credential = os.getenv('DatabaseServer4')
    elif opcion == 4:
        credential = os.getenv('DatabaseServer5')
    elif opcion == 5:
        credential = os.getenv('DatabaseServer6')
    elif opcion == 6:
        credential = os.getenv('DatabaseServer7')
    return credential

def getConexion(parameters):
    cnx = mysql.connector.connect(
        host=servidor,
        user=usuario,
        passwd=password,
        database=bd,
        port=puerto)

def treatment(credential):
    myarray = credential.split("-")
    name = myarray[5]
    parameters = {
        'host': myarray[1],
        'user': myarray[2],
        'passwd': myarray[3],
        'database': myarray[0],
        'port': myarray[4]
    }
    return parameters, name

for buried in range(6):
    option=1
    while opcion !=0:
        credentials=credentialDirectory(buried)
        parameters, name = treatment(credentials)
        try:
            cnx = mysql.connector.connect(**parameters)
            cursor = cnx.cursor()
            print(name.center(len(name)+60,'='))
            sql = input("input the query you want to execute : ")
            cursor.execute(sql)
            result = cursor.fetchall()
            log.info(name)
            log.info(sql)
            log.info(result)
            log.info("query succefully execute")
        except mysql.connector.Error as err:
            log.error(name.center(len(name)+20,'='))
            log.error(sql)
            log.error("Something went wrong: {}".format(err))
        finally:
            cnx.commit()
            cnx.close()
        print(name)
        opcion=int(input("Do you want to execute another query in this database?: "))        

