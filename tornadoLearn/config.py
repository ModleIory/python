from tornado import web
from tornado import ioloop
from tornado import httpserver
from tornado import options

options.define("port",default=8777,type=int,help='Come on')
options.define("arr",default=[],type=str,multiple=True,help="Come one baby!")

class IndexHandler(web.RequestHandler):
	def get(self):
		self.write("This config test")
	def post(self):
		pass

if __name__ == "__main__":
	app = web.Application([
		(r'/',IndexHandler)
	])
	# 从配置文件导入配置,作为一个小工具来说是很好的,可以方便的读取config,来作为一个强力的脚本
	# 而且配置文件,各项配置,直接写成Python的格式,直接就是赋值了
	options.parse_config_file("./config")
	httpserver = httpserver.HTTPServer(app)
	port = options.options.port
	httpserver.listen(port)
	print("run on port {}".format(port))
	print(options.options.arr)
	ioloop.IOLoop.current().start()
