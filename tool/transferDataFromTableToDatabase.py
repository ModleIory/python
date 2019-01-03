import pymysql 
import xlrd
import time

# xls operation
def readExcelReturnDataList(filePath):
	data = None
	dataList = []
	extension = filePath.split(".").pop()
	table = None
	timestamp = time.localtime(time.time())
	current = time.strftime("%Y-%m-%d %H:%M:%S",timestamp)
	# print(current)
	if extension=='xls':
		table = xlrd.open_workbook(filePath)
		sheets = table.sheet_names()
		result = table.sheet_by_name(sheets[0])
		for i in range(0, result.nrows):
			eachRow = result.row(i)
			#前两项是标题
			# print(eachRow[0])
			if i>1:
				# print("*"*50)
				valType = result.cell_value(i,0)
				if valType=='单项选择题':
					title = result.cell_value(i,1)
					content = result.cell_value(i,2)
					category_id = 0
					category_pid = 0
					answer_1 = result.cell_value(i,11)
					answer_2 = result.cell_value(i,12)
					answer_3 = result.cell_value(i,13)
					answer_4 = result.cell_value(i,14)
					post_time = current
					poster = result.cell_value(i,10)
					other = ''
					answer = result.cell_value(i,3).lower()
					update_time = current
					is_trap = 0
					is_boom = 0
					if answer=='a':
						answer = 1
					elif answer=='b':
						answer = 2
					elif answer=='c':
						answer = 3
					elif answer=='d':
						answer = 4
					else:
						answer = 0

					data = {
						"title":title,
						"content":content,
						"category_pid":category_pid,
						"category_id":category_id,
						"answer_1":answer_1,
						"answer_2":answer_2,
						"answer_3":answer_3,
						"answer_4":answer_4,
						"post_time":post_time,
						"poster":poster,
						"other":other,
						"answer":answer,
						"update_time":update_time,
						"is_trap":is_trap,
						"is_boom":is_boom,
					}
					dataList.append(data)

		return dataList

	elif extension=='xlsx':
		table = xlrd.load_workbook(filePath)
	else:
		print("Your destination file is not limited!")






dataList = readExcelReturnDataList("tables/senior.xls")
# print(dataList)


# db operation
print("mysql dealing...")
db = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="answer_zs",charset="utf8")
cursor = db.cursor()
for obj in dataList:
	sql = '''
		INSERT INTO tb_subject 
		(title,content,category_id,category_pid,answer_1,
		answer_2,answer_3,answer_4,answer,poster,
		post_time,other,update_time,is_boom,is_trap) 
		VALUES 
		('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
	'''.format(obj['title'],obj['content'],obj['category_id'],obj['category_pid'],obj['answer_1'],
		obj['answer_2'],obj['answer_3'],obj['answer_4'],obj['answer'],obj['poster'],
		obj['post_time'],obj['other'],obj['update_time'],obj['is_boom'],obj['is_trap'])
	# sql = '''
	# 	INSERT INTO tb_subject 
	# 	(title,content,category_id,category_pid,answer_1,
	# 	answer_2,answer_3,answer_4,answer,poster,
	# 	post_time,other,update_time,is_boom,is_trap) 
	# 	VALUES 
	# 	('0','0','0','0','0','0','0','0','0','0','0','0','0','0','0')
	# '''
	print(sql)
	cursor.execute(sql)
	print("*"*50)
	print("SUCCESSFULLY INSERT DATA...")
db.close()
