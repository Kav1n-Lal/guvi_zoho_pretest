import mysql.connector as mysql
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
#Establishing connection to mysql
cnx = mysql.connect(user='root', password='AccountsandRoles@78',
                    host='127.0.0.1',
                    database='zoho_pretest',
                    use_pure=False)
cursor=cnx.cursor()

DB_NAME = 'zoho_pretest'

TABLES = {}
TABLES['user_details'] = (
    "CREATE TABLE `user_details` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `age` int(2) NOT NULL,"
    "  `email_id` varchar(50) NOT NULL,"
    "  `password` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB") 

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
    print('Database exists')
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
except mysql.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    
add_user = ("INSERT INTO user_details "
               "(first_name, last_name, gender, birth_date, age, email_id, password) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

data_user = ('Geert', 'Vanderkelen', 'M', date(1977, 6, 14),35,'asde@gmail.com','12345')
# Insert new user
cursor.execute(add_user, data_user)
cnx.commit()
cursor.close()
cnx.close()
