import pymysql
import os,sys

print('mysql basic')

class connection():
	def __init__(self,host='localhost',port='3306',user='root',password='root',db='test'):
		self.host = host
		self.port = 3306
		self.user = user
		self.password = password
		self.db = db
	def connect(self):
		config = {
			"host":self.host,
			"port":self.port,
			"user":self.user,
			"password":self.password,
			"db":self.db
		}
		# print(config)
		db = pymysql.connect(**config)
		# print(db)
		return db
	def insert(self):
		db = self.connect()
		try:
			with db.cursor() as cursor:
				sql = '''
					INSERT INTO user(username,password,type,status) VALUES(%s,%s,%s,%s) 
				'''
				cursor.execute(sql,('modle_iory','hello_world','1','2'))
				db.commit()
		except Exception as e:
			print(str(e))
			db.rollback()
		finally:
			db.close()
	def delete(self):
		db = self.connect()
		try:
			with db.cursor() as cursor:
				sql = '''
					DELETE FROM user WHERE id=%s
				'''
				cursor.execute(sql,(4,))
				db.commit()
		except Exception as e:
			print(str(e))
			db.rollback()
		finally:
			db.close()
	def update(self):
		db = self.connect()
		try:
			with db.cursor() as cursor:
				sql = '''
					UPDATE user SET password=%s WHERE id=%s
				'''
				cursor.execute(sql,('iloveyoubybe',3))
				db.commit()
		except Exception as e:
			print(str(e))
			db.rollback()
		finally:
			db.close()
	def select(self):
		db = self.connect()
		try:
			with db.cursor() as cursor:
				sql = '''
					SELECT * FROM user AS u 
					LEFT JOIN msg AS m 
					ON u.id=m.user_id 
				'''
				cursor.execute(sql)
				# result = cursor.fetchone()
				result = cursor.fetchall()
				print(result)
				db.commit()
		except Exception as e:
			print(str(e))
			db.rollback()
		finally:
			db.close()


	def __del__(self):
		pass


c= connection(password="SiNuo123456")
# c.insert()
# c.delete()
# c.update()
c.select()

