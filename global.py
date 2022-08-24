import functions
import mysql.connector
from mysql.connector import errorcode
from logger_base import log

if __name__ == '__main__':
    for buried in range(6):
        option=1
        while option !=0:
            credentials=functions.credentialDirectory(buried)
            parameters, name = functions.treatment(credentials)
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
                log.info("privileges deleted: " + str(cursor.rowcount))
                log.info("query succefully execute")
            except mysql.connector.Error as err:
                log.error(name.center(len(name)+20,'='))
                log.error(sql)
                log.error("Something went wrong: {}".format(err))
            finally:
                cnx.commit()
                cnx.close()
            print(name)
            option=int(input("Do you want to execute another query in this database?: "))        

