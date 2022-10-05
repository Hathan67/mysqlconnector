import mysql.connector as m
# import os
import time


# database to backup
# db = 'python_db'

cnxn = m.connect(host='localhost', user='root',
					password='BISMILLAH', database="python_db")
# print(cnxn)
# if cnxn:
#     print("conected")
# else:
#     print("error")
hanif = cnxn.cursor()

# hey='select * from company'
# hanif.execute(hey)
# res=hanif.fetchone()
# print(res)

# # for x in hanif:
# # 	print(x)
#

hanif.execute('select * from staff')

print(hanif.column_names)
hy = hanif.fetchall()
for x in hy:
	print(x)








# table_names = []
# for record in hanif.fetchall():
# 	table_names.append(record[0])
#
# DATETIME = time.strftime('%Y%m%d-%H%M%S')
# backup_dbname = "python_db" + "_hi"
#
# try:
# 	hanif.execute(f'CREATE DATABASE {backup_dbname}')
# except:
# 	pass
#
# hanif.execute(f'USE {backup_dbname}')
#
# for table_name in table_names:
# 	hanif.execute(
# 		f'CREATE TABLE {table_name} SELECT * FROM {"python_db"}.{table_name}')

