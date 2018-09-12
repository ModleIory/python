from tornado import web
from tornado import ioloop
from tornado import httpserver
# for the cmd param
from tornado import options

# 输入的命令行的格式应该是 python option_learn.py --port=9999 --pray=good --array=one,two,three
# especially for cmd run
options.define("port",default=8777,type=int,help="The server port")
options.define("pray",default="good luck",type=str,help="please input your prayer")
options.define('array',default=[],type=str,multiple=True,help="test array in")

class IndexHandler(web.RequestHandler):
	def get(self):
		self.write("Hello this is option learn")


if __name__ == "__main__":
	app = web.Application([
		(r'/',IndexHandler),
	])
	#调用这个默认开启日志,关闭配置,但是感觉是不起作用的
	options.logging = None
	options.parse_command_line()
	port = options.options.port
	pray = options.options.pray
	httpserver = httpserver.HTTPServer(app)
	httpserver.listen(port)
	print("Your prayer is {} and server runs on port {}".format(pray,port))
	array = options.options.array
	print(array)
	ioloop.IOLoop.current().start()
