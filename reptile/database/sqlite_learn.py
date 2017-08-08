import sqlite3
import os,sys

print(sys.argv)

print("sqlite是C写的 小巧轻便 可以集成到程序中 储存方式是文件 python中直接就有这个库 都不用pip 直接import")

#描述一下过程

con = sqlite3.connect('sqlite/test.db')#有则存储,没有则新建
cursor = con.cursor()#感觉和pymysql微微相像


#由于是个文件了  只能够写代码来创建表的
# if os.path.exists('test.db'):
# 	pass
# else:
sql_create_table = '''
	CREATE TABLE user (
		id int primary key,
		username varchar(20),
		password varchar(20),
		create_date date
	)
'''
try:
	cursor.execute(sql_create_table)
except Exception as e:
	# print(str(e))
	print('表已经存在了')	



sql_insert_data = '''
	INSERT INTO user(id,username,password,create_date) VALUES(3,'modle_sherlock_','_shelrock000',"2017-08-03 17:10:55")
'''
cursor.execute(sql_insert_data)

con.commit()

select_sql = '''
	SELECT * FROM user
'''
cursor.execute(select_sql)
print(cursor.fetchall())

cursor.close()
con.close()