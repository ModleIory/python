import io

#存在文件里面但是仅能在一个脚本里面使用,麻皮 ,那要内存何用?

string = 'I am king'
string_b = string.encode('utf-8')

sf = io.StringIO()
sf.write(string)
sf.write('    ')
sf.write('good')
print(sf.getvalue())

bf = io.BytesIO()
bf.write(string_b)
bf.write(' fuck'.encode('utf-8'))
print(bf.getvalue())


