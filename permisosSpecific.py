import functions
import mysql.connector
from mysql.connector import errorcode
from logger_base import log
import string
import random
from datetime import date, datetime, timedelta
length_of_string = 16

if __name__ == '__main__':
        functions.menu()
        mortuaire=input("choose your mortuaire: ")
        option=1
        credentials=functions.credentialDirectory(mortuaire)
        parameters, name = functions.treatment(credentials)
        try:
            cnx = mysql.connector.connect(**parameters)
            cursor = cnx.cursor()
            print(name.center(len(name)+60,'='))
            sql1 = "SELECT serie,iduser FROM system_synchronization WHERE serie ='22870050' LIMIT 1;"
            cursor.execute(sql1)
            result1 = cursor.fetchall()
            sql2 = "DELETE FROM funeraria_administracion_acciones_campos_usuarios WHERE estatus='0';"
            cursor.execute(sql2)
            log.info(name)
            log.info(sql2)
            log.info("privileges deleted: " + str(cursor.rowcount))
            now = datetime.now()
            fechaFormateada = now.strftime('%Y-%m-%d %H:%M:%S')
            reference = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
            sql3 = f"INSERT INTO `system_synchronization` (`id_log`, `Serie`, `iduser`, `idmodule`, `register`, `Type`, `Query`, `authorization`) VALUES ('{reference}', '{result1[0][0]}', '{result1[0][1]}', '202', '{fechaFormateada}', 'DELETE', 'DELETE FROM funeraria_administracion_acciones_campos_usuarios WHERE estatus=&#roro;0&#roro;', '');"
            cursor.execute(sql3)
            log.info(sql2)
            log.info("query succefully execute")
        except mysql.connector.Error as err:
            log.error(name.center(len(name)+20,'='))
            log.error(sql1)
            log.error("Something went wrong: {}".format(err))
        finally:
            cnx.commit()
            cnx.close()
        print(name)    

